from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton
from PyQt5.QtGui import QPixmap
import sys

class app(QWidget):
    a = 1
    def __init__(self):
        super().__init__()
        self.titulo = "UMAKER"
        self.x = 300
        self.y = 300
        self.w = 600
        self.h = 300
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle(self.titulo)
        self.setGeometry(self.x,self.y,self.w,self.h)
        self.verde = QPixmap("led_verde.png")
        self.azul = QPixmap("led_azul.png")
        #creamos un texto
        self.label1 = QLabel(self)
        boton = QPushButton("click!",self)
        boton.move(150,150)
        self.label1.setPixmap(self.azul)
        self.label1.move(20,20)
        boton.clicked.connect(self.on_click)
        self.show()
    def on_click(self):
        self.a=self.a+1
        print("se presiono")
        if self.a%2==0:
            self.label1.setPixmap(self.verde)
            self.label1.move(20,20)
        else:
            self.label1.setPixmap(self.azul)
            self.label1.move(20,20)

aux = QApplication([])
ex = app()
sys.exit(aux.exec_())
