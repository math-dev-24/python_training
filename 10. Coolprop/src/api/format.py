class Format:

    @staticmethod
    def format_pressure(value: float, unit: str) -> str:
        if unit == "P":
            return f"{str(round(value / 101325 * 10) / 10)} bar"
        if unit == "B":
            return f"{str(round(value * 10) / 10)} bar"

    @staticmethod
    def format_temperature_C(value: float, unit: str) -> str:
        if unit == "K":
            return f"{str(round(value - 273.15 * 10) / 10)}°C"
        if unit == "T":
            return f"{str(round(value * 10) / 10)}°C"

    @staticmethod
    def format_enthalpie(value: float) -> str:
        return f"{str(round(value * 10) / 10)} kj/kg"

    @staticmethod
    def format_temperature_K(value: float, unit: str) -> str:
        if unit == "K":
            return f"{str(value)} K"
        if unit == "T":
            return f"{str(value + 273.15)} K"