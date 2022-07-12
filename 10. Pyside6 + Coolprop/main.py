from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from list import ListFluid
from calcul import CalculSysteme

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation fluide frigorigène")
        self.setMinimumWidth(700)
        self.setMaximumHeight(750)

        self.main_layout = QHBoxLayout(self)
        self.label_layout = QVBoxLayout()
        self.input_result_layout = QVBoxLayout()

        # Fluide Line
        self.label_fluid = QLabel("Fluide frigorigène :")
        self.input_fluid = ListFluid()
        self.label_layout.addWidget(self.label_fluid)
        self.input_result_layout.addWidget(self.input_fluid)

        # Tcdr Line
        self.label_t_cdr = QLabel("Température de condensation : (°C)")
        self.input_t_cdr = QLineEdit()
        self.label_layout.addWidget(self.label_t_cdr)
        self.input_result_layout.addWidget(self.input_t_cdr)

        # Tsous_ref
        self.label_t_sr = QLabel("Sous-refroidissement : (K)")
        self.input_t_sr = QLineEdit()
        self.label_layout.addWidget(self.label_t_sr)
        self.input_result_layout.addWidget(self.input_t_sr)

        # T évap
        self.label_t_evp = QLabel("Température d'évaporation : (°C)")
        self.input_to = QLineEdit()
        self.label_layout.addWidget(self.label_t_evp)
        self.input_result_layout.addWidget(self.input_to)

        # BTN Calcul
        self.btn_calcul = QPushButton("Calculer !")
        self.btn_calcul.clicked.connect(self.calcul_p)
        self.input_result_layout.addWidget(self.btn_calcul)

        # result pcrit
        self.label_t_crit = QLabel("Pression critique :")
        self.result_p_crit = QLabel("")
        self.label_layout.addWidget(self.label_t_crit)
        self.input_result_layout.addWidget(self.result_p_crit)

        # result CDR
        self.label_p_cdr = QLabel("Pression de condensation : ")
        self.result_p_cdr = QLabel("")
        self.label_layout.addWidget(self.label_p_cdr)
        self.input_result_layout.addWidget(self.result_p_cdr)
        # result evp
        self.label_p_evp = QLabel("Pression d'évaporation : ")
        self.result_p_evp = QLabel("")
        self.label_layout.addWidget(self.label_p_evp)
        self.input_result_layout.addWidget(self.result_p_evp)

        # Construction des layouts généraux
        self.main_layout.addLayout(self.label_layout)
        self.main_layout.addLayout(self.input_result_layout)

    def calcul_p(self):
        try:
            fluid = str(self.input_fluid.currentText())
            t_cdr = int(self.input_t_cdr.text())
            t_evp = int(self.input_to.text())
            t_sr = int(self.input_t_sr.text())
            t_sf = 0

        except:
            error = "Donnèes d'entrées érronées ou manquantes"
            self.result_p_crit.setText(error)
            self.result_p_cdr.setText(error)
            self.result_p_evp.setText(error)
        else:
            Cp = CalculSysteme(fluid, t_cdr, t_evp, t_sr, t_sf)
            self.result_p_crit.setText(Cp.get_p_crit())
            self.result_p_cdr.setText(Cp.get_p_sat_cdr())
            self.result_p_evp.setText(Cp.get_p_sat_evp())



if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()
