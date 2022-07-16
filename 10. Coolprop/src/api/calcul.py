import CoolProp.CoolProp as CP
# doc : http://www.coolprop.org/v4/contents.html

# 1:Aspiration , 2S:refoulement Is , 2R: refoulement réel, 3: sortie cdr, 4: entrée détendeur, 5: sortie détendeur
# 6 sortie évaporateur
class Calcul_thermo:

    def __init__(self, fluid: str, rend_v: float, rend_is: float, tcdr: float, to: float, tsr: float, tsf: float,
                 tsrt: float, tsft: float):
        self.fluid = fluid
        self.rend_v = rend_v
        self.rend_is = rend_is
        self.t_cdr = tcdr + 273.15
        self.t_o = to + 273.15
        self.t_sr = tsr
        self.t_sf = tsf
        self.t_srt = tsrt
        self.t_sft = tsft
        self.t_out_evp = self.t_o + self.t_sf
        self.t_asp = self.t_out_evp + self.t_sft
        self.t_out_cdr = round((self.t_cdr - self.t_sr) * 10) / 10
        self.t_in_det = self.t_out_cdr - self.t_srt

        self.p_sat_cdr = CP.PropsSI("P", "Q", 0, "T", int(self.t_cdr), self.fluid)
        self.p_sat_evp = CP.PropsSI("P", "Q", 1, "T", int(self.t_o), self.fluid)
        self.s_asp = CP.PropsSI("S", "T", self.t_asp, "P", self.p_sat_evp, self.fluid)


    @property
    def pt_asp(self) -> dict:
        point_un = {
            "S": self.s_asp,
            "P": self.p_sat_evp,
            "T": self.t_asp,
            "Tvap": self._t_sat("vap", self.p_sat_evp),
            "Tliq": self._t_sat("liq", self.p_sat_evp),
            "H": CP.PropsSI("H", "P", self.p_sat_evp, "T", self.t_asp, self.fluid),
            "D": CP.PropsSI("D", "P", self.p_sat_evp, "T", self.t_asp, self.fluid)
        }
        return point_un

    @property
    def pt_ref_is(self) -> dict:
        temp = CP.PropsSI("T", "S", self.s_asp, "P", self.p_sat_cdr, self.fluid)
        point_deux_s = {
            "S": self.s_asp,
            "P": self.p_sat_cdr,
            "T": temp,
            "Tvap": self._t_sat("vap", self.p_sat_cdr),
            "Tliq": self._t_sat("liq", self.p_sat_cdr),
            "H": CP.PropsSI("H", "P", self.p_sat_cdr, "T", temp, self.fluid),
            "D": CP.PropsSI("D", "P", self.p_sat_cdr, "T", temp, self.fluid)
        }
        return point_deux_s

    @property
    def pt_ref_reel(self) -> dict:
        enthalpy = ((self.pt_ref_is["H"] - self.pt_asp['H']) / self.rend_is) + self.pt_asp['H']
        data = {
            "S": CP.PropsSI("S", "P", self.p_sat_cdr, "H", enthalpy, self.fluid),
            "P": self.p_sat_cdr,
            "T": CP.PropsSI("T", "P", self.p_sat_cdr, "H", enthalpy, self.fluid),
            "Tvap": self._t_sat("vap", self.p_sat_cdr),
            "Tliq": self._t_sat("liq", self.p_sat_cdr),
            "H": enthalpy,
            "D": CP.PropsSI("D", "P", self.p_sat_cdr, "T",
                            CP.PropsSI("T", "P", self.p_sat_cdr, "H", enthalpy, self.fluid), self.fluid)
        }
        return data

    @property
    def pt_out_cdr(self) -> dict:
        data = {
            "S": None,
            "P": self.p_sat_cdr,
            "T": self.t_out_cdr,
            "Tvap": self._t_sat("vap", self.p_sat_cdr),
            "Tliq": self._t_sat("liq", self.p_sat_cdr),
            "H": CP.PropsSI("H", "P", self.p_sat_cdr, "T", self.t_out_cdr, self.fluid),
            "D": CP.PropsSI("D", "T", self.t_out_cdr, "P", self.p_sat_cdr, self.fluid)
        }
        return data

    @property
    def pt_in_det(self) -> dict:
        data = {
            "S": None,
            "P": self.p_sat_cdr,
            "T": self.t_in_det,
            "Tvap": self._t_sat("vap", self.p_sat_cdr),
            "Tliq": self._t_sat("liq", self.p_sat_cdr),
            "H": CP.PropsSI("H", "T", self.t_in_det, "P", self.p_sat_cdr, self.fluid),
            "D": CP.PropsSI("D", "T", self.t_in_det, "P", self.p_sat_cdr, self.fluid)
        }
        return data

    @property
    def pt_out_det(self):
        data = {
            "S": None,
            "P": self.p_sat_evp,
            "T": self.t_o,
            "Tvap": self._t_sat("vap", self.p_sat_evp),
            "Tliq": self._t_sat("liq", self.p_sat_evp),
            "H": self.pt_in_det['H'],
            "D": CP.PropsSI("D", "H", self.pt_in_det['H'], "P", self.p_sat_evp, self.fluid),
            "Q": CP.PropsSI("Q", "H", self.pt_in_det['H'], "P", self.p_sat_evp, self.fluid)
        }
        return data

    @property
    def pt_out_evp(self):
        data = {
            "S": None,
            "P": self.p_sat_evp,
            "T": self.t_out_evp,
            "Tvap": self._t_sat("vap", self.p_sat_evp),
            "Tliq": self._t_sat("liq", self.p_sat_evp),
            "H": CP.PropsSI("H", "P", self.p_sat_evp, "T", self.t_out_evp, self.fluid),
            "D": CP.PropsSI("D", "P", self.p_sat_evp, "T", self.t_out_evp, self.fluid)
        }
        return data

    @property
    def p_crit(self) -> float:
        return CP.PropsSI(self.fluid, "pcrit")

    def _t_sat(self, etat: str, pressure: float) -> float:
        if etat == "liq":
            return CP.PropsSI("T", "Q", 0, "P", pressure, self.fluid)
        else:
            return CP.PropsSI("T", "Q", 1, "P", pressure, self.fluid)

    def get_data(self) -> dict:
        data = {
            "fluid": self.fluid,
            "Pcrit": self.p_crit,
            "unit": {
                "S": "J",
                "P": "Pa",
                "T": "K",
                "H": "J/kG",
                "D": "kG/m³"
            },
            "position": {
                "1": "Aspiration compresseur",
                "2S": "Refoulement Isentropique",
                "2R": "Refoulement Réel",
                "3": "Sortie condenseur",
                "4": "Entrée détendeur",
                "5": "Sortie détendeur",
                "6": "Sortie évaporateur"
            },
            "data": {
                "1": self.pt_asp,
                "2S": self.pt_ref_is,
                "2R": self.pt_ref_reel,
                "3": self.pt_out_cdr,
                "4": self.pt_in_det,
                "5": self.pt_out_det,
                "6": self.pt_out_evp
            }
        }
        return data

    def get_courbe_diagrame(self):
        pressure_max = int(round(self.p_crit / 101325))
        print(pressure_max)
        data = {
            "unit": {"Pressure (Pa)": 'Enthalpie (J/kg)'},
            "liq": {},
            "vap": {}
        }
        for i in range(1, pressure_max):
            pressure = i * 101325
            data["liq"][str(pressure)] = CP.PropsSI("H", "Q", 0, "P", pressure, self.fluid)
            data['vap'][str(pressure)] = CP.PropsSI("H", "Q", 1, "P", pressure, self.fluid)
        return data

    @staticmethod
    def fluid_custom_2(f1: str, c1: float, f2: str, c2: str):
        return f"REFPROP-MIX:{f1}[{c1}]&{f2}[{c2}]"

if __name__ == "__main__":
    simul = Calcul_thermo("R407C", 0.9, 0.6, 20, -15, 5, 10, 2, 2)
    print(simul.get_courbe_diagrame())
