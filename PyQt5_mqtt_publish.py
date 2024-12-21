from PyQt5.QtWidgets import QWidget,QApplication,QSpinBox,QLabel
import paho.mqtt.publish as publish
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
        #label
        label1 = QLabel("Adjust Temp",self)
        label1.move(120,50)
        label1.setStyleSheet("font-size:15px;font-weight:bold;color:#2505f4")
        #qspinbox
        spinbox = QSpinBox(self)
        spinbox.setGeometry(130,80,80,50)
        estilo = "font-size:25px;font-weight:bold;color:#29d5c4"
        spinbox.setStyleSheet(estilo)
        spinbox.valueChanged.connect(self.datos)
        self.show()
    def datos(self,value):
        print(value)
        publish.single(auth = {"username":"admin", "password":clase}, topic="/v2.0/devices/device_1/temperatura1" ,hostname="industrial.api.ubidots.com",port=1883,payload=value)


clave = "1234"
aux = QApplication([])
ex = app()
sys.exit(aux.exec_())
