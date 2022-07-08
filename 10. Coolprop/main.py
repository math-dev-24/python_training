import CoolProp.CoolProp as CP
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QTabBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("utilisation de CoolProps")
        self.setMinimumWidth(900)
        self.setMaximumHeight(750)

        self.main_layout = QHBoxLayout(self)
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()

        # Fluide Line
        self.fluid_line = QHBoxLayout()
        self.label_fluid = QLabel("Fluide frigorigène :")
        self.input_fluid = QLineEdit()
        self.fluid_line.addWidget(self.label_fluid)
        self.fluid_line.addWidget(self.input_fluid)
        self.left_layout.addLayout(self.fluid_line)

        #Tcdr Line
        self.t_cdr_line = QHBoxLayout()
        self.label_t_cdr = QLabel("Température de condensation")
        self.label_t_cdr2 = QLabel("°C")
        self.input_t_cdr = QLineEdit()
        self.t_cdr_line.addWidget(self.label_t_cdr)
        self.t_cdr_line.addWidget(self.input_t_cdr)
        self.t_cdr_line.addWidget(self.label_t_cdr2)
        self.left_layout.addLayout(self.t_cdr_line)
        #T évap
        self.t_evp_line = QHBoxLayout()
        self.label_t_evp = QLabel("Température d'évaporation")
        self.label_t_evp2 = QLabel("°C")
        self.input_to = QLineEdit()
        self.t_evp_line.addWidget(self.label_t_evp)
        self.t_evp_line.addWidget(self.input_to)
        self.t_evp_line.addWidget(self.label_t_evp2)
        self.left_layout.addLayout(self.t_evp_line)
        # BTN Calcul
        self.btn_calcul = QPushButton("Calculer !")
        self.btn_calcul.clicked.connect(self.calcul_p)
        self.left_layout.addWidget(self.btn_calcul)

        self.result_p_cdr_line = QHBoxLayout()
        self.label_p_cdr = QLabel("Pression de condensation : ")
        self.result_p_cdr = QLabel("")
        self.result_p_cdr_line.addWidget(self.label_p_cdr)
        self.result_p_cdr_line.addWidget(self.result_p_cdr)
        self.left_layout.addLayout(self.result_p_cdr_line)

        self.result_p_evp_line = QHBoxLayout()
        self.label_p_evp = QLabel("Pression d'évaporation : ")
        self.result_p_evp = QLabel("")
        self.result_p_evp_line.addWidget(self.label_p_evp)
        self.result_p_evp_line.addWidget(self.result_p_evp)
        self.left_layout.addLayout(self.result_p_evp_line)

        #Construction des layouts généraux
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)


    def calcul_p(self):
        try:
            fluid = str(self.input_fluid.text())
            t_cdr = int(self.input_t_cdr.text())
            t_evp = int(self.input_to.text())
        except:
            self.result_p_cdr.setText("Donnèes d'entrées érronées ou manquantes")
            self.result_p_evp.setText("Donnèes d'entrées érronées ou manquantes")
        else:
            self.result_p_cdr.setText(str(round((CP.PropsSI("P","T",t_cdr+273.15,"Q",1,fluid) / 101325)*10)/10) + ' bar')
            self.result_p_evp.setText(str(round((CP.PropsSI("P","T",t_evp+273.15,"Q",0,fluid) / 101325)*10) /10) + ' bar')

app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()




