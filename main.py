import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ConverGui import Ui_MainWindow
import pandas as pd


class Converter(QMainWindow):
    def __init__(self):
        # Inicializar el frame
        super(Converter, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Botones
        self.ui.DoBut.clicked.connect(self.intercambio)

    def intercambio(self):
        self.mon1 = self.ui.ComboDinero1.currentText()
        self.mon2 = self.ui.ComboDinero2.currentText()

        self.leer_datos()

        cantidad = float(self.ui.Cantidad.toPlainText())
        cantidad = cantidad * self.locate
        self.ui.Resultado.setText(str(cantidad))

    def leer_datos(self):

        df = pd.read_csv('Divisa.csv')

        self.locate = float((df.loc[(df['Divisa1'] == self.mon1) & (df['Divisa2'] == self.mon2)])['Cambio'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Converter()
    window.show()
    sys.exit(app.exec_())
