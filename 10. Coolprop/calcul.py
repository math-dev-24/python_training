import CoolProp.CoolProp as CP


class CalculSysteme():
    def __init__(self, fluid, tcdr, to, tsr, tsf):
        self.fluid = fluid
        self.tcdr = tcdr
        self.to = to
        self.tsr = tsr
        self.tsf = tsf
        self.v_aspi = 12
        self.v_ll = 1
        self.v_ref = 15


    def get_p_crit(self):
        return self.format_pressure(CP.PropsSI(self.fluid, "pcrit"))
    def get_p_sat_cdr(self):
        return self.format_pressure(CP.PropsSI("P", "Q",1, "T", int(self.tcdr) + 273.15, self.fluid))
    def get_p_sat_evp(self):
        return self.format_pressure(CP.PropsSI("P", "Q", 0, "T", int(self.to) + 273.15, self.fluid))


    def format_pressure(self, value):
        return str(round(value / 101325 * 10)/10) + " bar"
    def format_temperature(self, value):
        return str(round(value - 273.15 * 10)/10) + " °C"
