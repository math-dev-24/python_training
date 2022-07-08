from PySide6.QtWidgets import QComboBox


class ListFluid(QComboBox):
    def __init__(self):
        super(ListFluid, self).__init__()
        self.fluids = (
            'R134a',"R404A",'R407C','R22',"CO2","R22","R123a"
        )
        for fluid in self.fluids:
            self.addItem(fluid)