from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        btn1= QPushButton("bnt1")
        btn2= QPushButton("bnt2")
        btn3= QPushButton("bnt3")
        btn4= QPushButton("bnt4")
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        self.setLayout(layout)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()