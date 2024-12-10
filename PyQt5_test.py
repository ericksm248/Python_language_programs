import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "prueba5.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.boton.clicked.connect(self.calculos)
    def calculos(self):
        precio = int(self.introduceprecio.toPlainText())
        desc = (self.descuento.value())
        pago = precio - ((desc/100)*precio)
        pago_st = "su pago es : "+ str(pago)
        self.resultado.setText(pago_st)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
