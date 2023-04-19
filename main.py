from PyQt5.QtWidgets import *
import sys
from ui import *
import matplotlib.pyplot as plt
import numpy as np
import math 

class AppWin(QMainWindow, Ui_MainWindow):

    
    def __init__(self):

        QMainWindow.__init__(self)
        self.setupUi(self)  # Se genera la interfaz llamando al metodo setupUi

    def generador(self):
        '''Funcion que se ejecuta cuando se presiona el boton Generar en la Pantalla, dependiendo de los parametros ingresados
            Calcula la distribucion correspondiente, y muestra sus valores en una tabla'''
        indice = 0
        tabla = self.tableWidget

        datos = []
        

        if (self.mediaTextEdit.text() != "" and self.desvTextEdit.text() != ""): #DATOS INGRESADOS PARA DISTRIBUCION NORMAL
            
            n = int(self.valoresTextEdit.text())
            es_impar = (n % 2 == 1 )
            
            if es_impar:
                vueltas = math.trunc(n/2) + 1
            else:
                vueltas = math.trunc(n/2)

            
            for i in range(vueltas): #Itera en la cantidad de numeros pedidos
                nom = normal                                           #Divide por dos porque como es normal, genera dos numeros 
                a = nom.normal(float(self.mediaTextEdit.text()),
                               float(self.desvTextEdit.text()))
                

                if((i == (vueltas-1)) and es_impar):

                    indice = tabla.rowCount()
                    tabla.insertRow(indice)
                    tabla.setItem(indice, 0, QtWidgets.QTableWidgetItem(str(indice+1)))
                    tabla.setItem(indice, 1, QtWidgets.QTableWidgetItem(str(a[0])))

                    datos.append(a[0])
                    
                else:

                    indice = tabla.rowCount()
                    tabla.insertRow(indice)
                    
                    tabla.setItem(indice, 0, QtWidgets.QTableWidgetItem(str(indice+1)))
                    tabla.setItem(indice, 1, QtWidgets.QTableWidgetItem(str(a[0])))


                    indice = tabla.rowCount()
                    tabla.insertRow(indice)

                    tabla.setItem(indice, 0, QtWidgets.QTableWidgetItem(str(indice+1)))
                    tabla.setItem(indice, 1, QtWidgets.QTableWidgetItem(str(a[1])))
                    
                    datos.append(a[0])
                    datos.append(a[1])


        #DISTRIBUCION UNIFORME
        elif (self.aTextEdit.text() != "" and self.bTextEdit.text() != ""): 
            for i in range(int(self.valoresTextEdit.text())):
                uni = uniforme
                tabla.insertRow(i)
                a = uni.uniforme(float(self.aTextEdit.text()),
                                 float(self.bTextEdit.text()))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(a)))

                datos.append(a)
            

        #DISTRIBUCION EXPONENCIAL
        elif (self.lambdaExpTextEdit.text() != ""): #DATOS INGRESADOS PARA DISTRIBUCION NORMAL
            for i in range(int(self.valoresTextEdit.text())):
                exp = exponencial
                tabla.insertRow(i)
                a = exp.exponencial(float(self.lambdaExpTextEdit.text()))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(a)))

                datos.append(a)


        #DISTRIBUCION POISSON
        elif (self.lambdaPoissonTextEdit.text() != ""): 
            for i in range(int(self.valoresTextEdit.text())):
                poi = poisson
                tabla.insertRow(i)
                a = poisson.poisson(float(self.lambdaPoissonTextEdit.text()))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(a)))

                datos.append(a)

        
        
    def generarGrafico(self):
        tabla = self.tableWidget
        datos = []
        n = tabla.rowCount()

        for i in range(n):
            datos.append(float(tabla.item(i,1).text()))
        
        #VER SI SE APLICAN LOS INTERVALOS EN POISSON O SE CALCULA SOLO

        if(self.lambdaPoissonTextEdit.text() != ""):
            plt.hist(datos)
        
        else:
            tics = [0] * (int(self.intervalosComboBox.currentText())+1)
            acum = min(datos)
            for i in range(len(tics)):
                tics[i] = acum
                acum += (max(datos) - min(datos)) / int(self.intervalosComboBox.currentText() )
                
            plt.hist(datos, bins=int(self.intervalosComboBox.currentText()))
            plt.xticks( tics )

        plt.xlabel("Intervalos")
        plt.ylabel("Frecuencia")
        plt.show()
        


# se inicia pantalla y app
if __name__ == '__main__':
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop
