from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
import sys
from ui import *
import matplotlib.pyplot as plt
import numpy as np
import math
from pruebasAjuste import Prueba


class AppWin(QMainWindow, Ui_MainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.setupUi(self)  # Se genera la interfaz llamando al metodo setupUi

    def generador(self):
        '''Funcion que se ejecuta cuando se presiona el boton Generar en la Pantalla, dependiendo de los parametros ingresados
            Calcula la distribucion correspondiente, y muestra sus valores en una tabla'''
        indice = 0
        tabla = self.tableWidget

        n = int(self.valoresTextEdit.text())  # cantidad de valores a generar

        datos = []

        # DISTRIBUCION NORMAL
        # DATOS INGRESADOS PARA DISTRIBUCION NORMAL
        if (self.mediaTextEdit.text() != "" and self.desvTextEdit.text() != ""):

            es_impar = (n % 2 == 1)

            if es_impar:
                vueltas = math.trunc(n/2) + 1
            else:
                vueltas = math.trunc(n/2)

            for i in range(vueltas):  # Itera en la cantidad de numeros pedidos
                nom = normal  # Divide por dos porque como es normal, genera dos numeros
                a = nom.normal(float(self.mediaTextEdit.text()),
                               float(self.desvTextEdit.text()))

                # Si es la ultima vuelta y la cantidad es impar, guarda uno de los dos numeros
                if ((i == (vueltas-1)) and es_impar):

                    indice = tabla.rowCount()
                    tabla.insertRow(indice)
                    tabla.setItem(
                        indice, 0, QtWidgets.QTableWidgetItem(str(indice+1)))
                    tabla.setItem(
                        indice, 1, QtWidgets.QTableWidgetItem(str(a[0])))

                    datos.append(a[0])

                else:  # si no es la ultima vuelta en impar, o si es un numero par de vueltas, agrega los dos

                    indice = tabla.rowCount()
                    tabla.insertRow(indice)

                    tabla.setItem(
                        indice, 0, QtWidgets.QTableWidgetItem(str(indice+1)))
                    tabla.setItem(
                        indice, 1, QtWidgets.QTableWidgetItem(str(a[0])))

                    indice = tabla.rowCount()
                    tabla.insertRow(indice)

                    tabla.setItem(
                        indice, 0, QtWidgets.QTableWidgetItem(str(indice+1)))
                    tabla.setItem(
                        indice, 1, QtWidgets.QTableWidgetItem(str(a[1])))

                    datos.append(a[0])
                    datos.append(a[1])
            # generarPruebaCHI()

            self.generarPruebaChi("normal", datos)

        # DISTRIBUCION UNIFORME
        elif (self.aTextEdit.text() != "" and self.bTextEdit.text() != ""):
            intervalos = [0] * int(self.intervalosComboBox.currentText())
            desde = int(self.aTextEdit.text())
            hasta = int(self.bTextEdit.text())
            paso = (hasta-desde) / int(self.intervalosComboBox.currentText())

            for i in range(len(intervalos)):  # genera los intervalos

                intervalos[i] = Prueba(desde, desde+paso - 0.0001, 0)
                desde += paso

            for i in range(n):  # genera los numeros
                uni = uniforme
                tabla.insertRow(i)
                a = uni.uniforme(float(self.aTextEdit.text()),
                                 float(self.bTextEdit.text()))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(a)))

                # por cada numero, verifica en que intervalo se encuentra
                for j in range(len(intervalos)):

                    if ((a >= intervalos[j].desde) and (a <= intervalos[j].hasta)):
                        intervalos[j].cantidad += 1

                        break

                datos.append(a)
            self.generarPruebaChi("uniforme", intervalos)

        # DISTRIBUCION EXPONENCIAL
        elif (self.lambdaExpTextEdit.text() != ""):  # DATOS INGRESADOS PARA DISTRIBUCION NORMAL
            for i in range(n):  # genera los numeros
                exp = exponencial
                tabla.insertRow(i)
                a = exp.exponencial(float(self.lambdaExpTextEdit.text()))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(a)))

                datos.append(a)
            self.generarPruebaChi("exponencial", datos)

        # DISTRIBUCION POISSON
        elif (self.lambdaPoissonTextEdit.text() != ""):
            for i in range(n):  # genera los numeros
                poi = poisson
                tabla.insertRow(i)
                a = poisson.poisson(float(self.lambdaPoissonTextEdit.text()))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(a)))

                datos.append(a)
            self.generarPruebaChi("poisson", datos)

    def generarGrafico(self):
        '''Genera el grafico para la distribucion generada'''
        tabla = self.tableWidget
        datos = []
        n = tabla.rowCount()

        if (n != 0):  # verifica que se hayan generados datos primero, sino no genera el grafico

            # agrega los RND generados al vector que luego se usa para generar el grafico
            for i in range(n):
                datos.append(float(tabla.item(i, 1).text()))

            # CHECKEA SI ES POISSON, VIENDO SI EL PARAMETRO ES != ""
            if (self.lambdaPoissonTextEdit.text() != ""):
                plt.hist(datos)
            else:
                # TICS = CANTIDAD DE MARCAS DE INTERVALO EN EL GRAFICO
                tics = [0] * (int(self.intervalosComboBox.currentText())+1)
                acum = min(datos)

                # genera vector con los valores a poner en las marcas delgrafico
                for i in range(len(tics)):
                    tics[i] = acum
                    acum += (max(datos) - min(datos)) / \
                        int(self.intervalosComboBox.currentText())

                plt.hist(datos, bins=int(
                    self.intervalosComboBox.currentText()))
                plt.xticks(tics)

            plt.xlabel("Intervalos")
            plt.ylabel("Frecuencia")
            plt.show()

    def limpiarCampos(self):
        '''Limpia todos los campos y las tablas en cada pantalla'''
        self.aTextEdit.setText("")
        self.bTextEdit.setText("")
        self.mediaTextEdit.setText("")
        self.desvTextEdit.setText("")
        self.lambdaExpTextEdit.setText("")
        self.lambdaPoissonTextEdit.setText("")
        self.valoresTextEdit.setText("")
        self.tableWidget.setRowCount(0)
        self.chiTableWidget.setRowCount(0)
        self.ksTableWidget.setRowCount(0)
        self.resultadoKsTextEdit.setText("")
        self.ksCalculadoLineEdit.setText("")
        self.ksTabuladoLineEdit.setText("")
        self.resultadoChiTextEdit.setText("")
        self.chiTabuladoTextEdit.setText("")
        self.chiCalculadoTextEdit.setText("")

    def generarPruebaChi(self, tipo, datos):
        '''Genera las pruebas dependiendo del tipo de distribucion cargada'''
        if (tipo == "uniforme"):
            Prueba.uniformeChi(self, datos)
        elif (tipo == "normal"):
            Prueba.normalChi(self, datos)
        elif (tipo == "exponencial"):
            Prueba.exponencialChi(self, datos)
        else:
            Prueba.poissonChi(self, datos)


# se inicia pantalla y app
if __name__ == '__main__':
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop
