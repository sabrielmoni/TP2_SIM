from PyQt5.QtWidgets import *
import sys
from ui import *
import matplotlib.pyplot as plt
import numpy as np

class AppWin(QMainWindow, Ui_MainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.setupUi(self)  # Se genera la interfaz llamando al metodo setupUi

    def generador(self):
        indice = 0
        tabla = self.tableWidget

        datos = []

        if (self.mediaTextEdit.text() != "" and self.desvTextEdit.text() != ""):
            for i in range(round(int(self.valoresTextEdit.text())/2)+1):
                nom = normal
                indice = tabla.rowCount()
                tabla.insertRow(indice)

                a = nom.normal(float(self.mediaTextEdit.text()),
                               float(self.desvTextEdit.text()))

                tabla.setItem(
                    indice, 0, QtWidgets.QTableWidgetItem(str(indice+1)))
                tabla.setItem(indice, 1, QtWidgets.QTableWidgetItem(str(a[0])))


                indice = tabla.rowCount()
                tabla.insertRow(indice)

                tabla.setItem(
                    indice, 0, QtWidgets.QTableWidgetItem(str(indice+1)))
                tabla.setItem(indice, 1, QtWidgets.QTableWidgetItem(str(a[1])))

                datos.append(a[0])
                datos.append(a[1])

            plt.hist(datos, bins=int(self.intervalosComboBox.currentText()))
            plt.xlabel("Intervalos")
            plt.ylabel("Frecuencia")
            plt.show()
                

        elif (self.aTextEdit.text() != "" and self.bTextEdit.text() != ""):
            for i in range(int(self.valoresTextEdit.text())):
                uni = uniforme
                tabla.insertRow(i)
                a = uni.uniforme(float(self.aTextEdit.text()),
                                 float(self.bTextEdit.text()))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(a)))

                datos.append(a)
                

            plt.hist(datos, bins=int(self.intervalosComboBox.currentText()))
            plt.xlabel("Intervalos")
            plt.ylabel("Frecuencia")
            plt.xticks(np.arange(min(datos), max(datos)+1, ((max(datos) - min(datos)) / int(self.intervalosComboBox.currentText() ) )))
            plt.show()
            

        elif (self.lambdaExpTextEdit.text() != ""):
            for i in range(int(self.valoresTextEdit.text())):
                exp = exponencial
                tabla.insertRow(i)
                a = exp.exponencial(float(self.lambdaExpTextEdit.text()))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(a)))

        elif (self.lambdaPoissonTextEdit.text() != ""):
            for i in range(int(self.valoresTextEdit.text())):
                poi = poisson
                tabla.insertRow(i)
                a = poisson.poisson(float(self.lambdaPoissonTextEdit.text()))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(a)))

    def prueba(self):
        print("")


# se inicia pantalla y app
if __name__ == '__main__':
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop
