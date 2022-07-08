from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout, QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To Do")
        self.setMinimumWidth(500)
        self.setMaximumHeight(750)

        self.main_layout = QVBoxLayout(self)

        self.lw_todos = QListWidget()
        self.tw_todos = QLineEdit()
        self.tw_todos.setPlaceholderText("Ajoutez todo")
        self.bw_todos = QPushButton("Tout Supprimer")

        self.main_layout.addWidget(self.lw_todos)
        self.main_layout.addWidget(self.tw_todos)
        self.main_layout.addWidget(self.bw_todos)

        self.tw_todos.returnPressed.connect(self.add_todo)
        self.bw_todos.clicked.connect(self.lw_todos.clear)
        self.lw_todos.itemDoubleClicked.connect(self.delete_todo)

    def add_todo(self):
        self.lw_todos.addItem(self.tw_todos.text())
        self.tw_todos.clear()

    def delete_todo(self, item):
        self.lw_todos.takeItem(self.lw_todos.row(item))


app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
