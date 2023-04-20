from PyQt5.QtWidgets import *
import math


def tabuladoChi(v):
    tabuladoChi = [3.84, 5.99, 7.81, 9.49, 11.1, 12.6, 14.1, 15.5, 16.9,
                   18.3, 19.7, 21.0, 22.4, 23.7, 25.0, 26.3, 27.6, 28.9,
                 30.1, 31.4, 32.7, 33.9, 35.2, 36.4, 37.7, 38.9, 40.1, 41.3, 42.6, 43.8]
    return tabuladoChi[v-1]


def validacion(calculado, tabulado):
    if (calculado <= tabulado):
        return "No se rechaza"
    else:
        return "Se rechaza"


class Intervalo:
    def __init__(self, desde, hasta, cantidad):
        self.desde = desde
        self.hasta = hasta
        self.cantidad = cantidad

    def generarPruebaChi(tipo, datos):
        if (tipo == "uniforme"):
            # calculo con intervalos de uniforme
            pass
        elif (tipo == "normal"):
            # calculo con datos de normal
            pass
        elif (tipo == "exponencial"):
            # calculo con datos de exponencial
            pass
        else:
            # calculo con datos de poisson
            pass

    def uniformeChi(self, intervalos, n):
        '''Calcula chi cuadrado para la distribucion uniforme
            entran intervalos con fo'''
        tabla = self.chiTableWidget
        cantidadIntervalos = len(intervalos)
        cantidadMuestra = n
        sumatoria = 0
        frecuenciaEsperada = cantidadMuestra/cantidadIntervalos

        for i in range(cantidadIntervalos):
            tabla.insertRow(i)
            c = math.pow(
                (float(intervalos[i].cantidad) - frecuenciaEsperada), 2)/frecuenciaEsperada
            tabla.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde)))
            tabla.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta)))
            tabla.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad)))
            tabla.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada)))
            tabla.setItem(i, 4, QTableWidgetItem(str(c)))
            if (i > 0):
                sumatoria += float(tabla.item(i, 4).text())
            else:
                sumatoria = c
            tabla.setItem(i, 5, QTableWidgetItem(str(sumatoria)))

        v = cantidadIntervalos - 1 - 0
        tabulado = tabuladoChi(v)
        self.chiCalculadoTextEdit.setPlainText(str(sumatoria))
        self.chiTabuladoTextEdit.setPlainText(str(tabulado))
        self.resultadoChiTextEdit.setPlainText(validacion(sumatoria, tabulado))

    def normalChi(self, datos):
        tabla = self.chiTableWidget
        minimo = min(datos)
        maximo = max(datos)
        media = float(self.mediaTextEdit.text())
        desviacionEstandar = float(self.desvTextEdit.text())
        cantidadIntervalos = int(self.intervalosComboBox.currentText())
        intervalos = [0] * cantidadIntervalos
        cantidadMuestra = int(self.valoresTextEdit.text())
        paso = ((maximo - minimo) / cantidadIntervalos)

        for i in range(len(intervalos)):

            intervalos[i] = Intervalo(minimo, minimo+paso - 0.0001, 0)
            minimo += paso

        for i in range(len(datos)):
            for j in range(len(intervalos)):
                if ((datos[i] >= intervalos[j].desde) and (datos[i] <= intervalos[j].hasta)):
                    intervalos[j].cantidad += 1
                    break
        
        for i in range(cantidadIntervalos):
            tabla.insertRow(i)
            x = (intervalos[i].desde + intervalos[i].hasta)/2
            probabilidadEsperada = (math.pow(math.e, (-0.5*(math.pow((x-media)/desviacionEstandar, 2)))))/(
                desviacionEstandar*math.sqrt(2*math.pi)) * paso
            frecuenciaEsperada = probabilidadEsperada * cantidadMuestra
            c = math.pow(
                (float(intervalos[i].cantidad) - frecuenciaEsperada), 2)/frecuenciaEsperada
            tabla.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde)))
            tabla.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta)))
            tabla.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad)))
            tabla.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada)))
            tabla.setItem(i, 4, QTableWidgetItem(str(c)))
            if (i > 0):
                sumatoria += float(tabla.item(i, 4).text())
            else:
                sumatoria = c
            tabla.setItem(i, 5, QTableWidgetItem(str(sumatoria)))

        v = cantidadIntervalos - 1 - 2
        tabulado = tabuladoChi(v)
        self.chiCalculadoTextEdit.setPlainText(str(sumatoria))
        self.chiTabuladoTextEdit.setPlainText(str(tabulado))
        self.resultadoChiTextEdit.setPlainText(validacion(sumatoria, tabulado))

    def exponencialChi(self, datos):
        tabla = self.chiTableWidget
        minimo = min(datos)
        maximo = max(datos)
        lmbd = float(self.lambdaExpTextEdit.text())
        cantidadIntervalos = int(self.intervalosComboBox.currentText())
        intervalos = [0] * cantidadIntervalos
        cantidadMuestra = int(self.valoresTextEdit.text())
        paso = ((maximo - minimo) / cantidadIntervalos)

        for i in range(len(intervalos)):

            intervalos[i] = Intervalo(minimo, minimo+paso - 0.0001, 0)
            minimo += paso

        for i in range(len(datos)):
            for j in range(len(intervalos)):
                if ((datos[i] >= intervalos[j].desde) and (datos[i] <= intervalos[j].hasta)):
                    intervalos[j].cantidad += 1
                    break

        for i in range(cantidadIntervalos):
            tabla.insertRow(i)
            probabilidadEsperada = (1-math.pow(math.e, -lmbd*intervalos[i].hasta)) - (
                1-math.pow(math.e, -lmbd*intervalos[i].desde))
            frecuenciaEsperada = probabilidadEsperada * cantidadMuestra
            c = math.pow(
                (float(intervalos[i].cantidad) - frecuenciaEsperada), 2)/frecuenciaEsperada
            tabla.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde)))
            tabla.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta)))
            tabla.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad)))
            tabla.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada)))
            tabla.setItem(i, 4, QTableWidgetItem(str(c)))
            if (i > 0):
                sumatoria += float(tabla.item(i, 4).text())
            else:
                sumatoria = c
            tabla.setItem(i, 5, QTableWidgetItem(str(sumatoria)))

        v = cantidadIntervalos - 1 - 1
        tabulado = tabuladoChi(v)
        self.chiCalculadoTextEdit.setPlainText(str(sumatoria))
        self.chiTabuladoTextEdit.setPlainText(str(tabulado))
        self.resultadoChiTextEdit.setPlainText(validacion(sumatoria, tabulado))

    def poissonChi(self, datos):
        tabla = self.chiTableWidget
        minimo = min(datos)
        maximo = max(datos)
        lmbd = float(self.lambdaPoissonTextEdit.text())
        cantidadIntervalos = (maximo - minimo)
        intervalos = [0] * cantidadIntervalos
        cantidadMuestra = int(self.valoresTextEdit.text())
        paso = 1

        for i in range(len(intervalos)):

            intervalos[i] = Intervalo(minimo, minimo, 0)
            minimo += paso

        for i in range(len(datos)):
            for j in range(len(intervalos)):
                if (datos[i] == intervalos[j].desde):
                    intervalos[j].cantidad += 1
                    break

        for i in range(cantidadIntervalos):
            tabla.insertRow(i)
            probabilidadEsperada = (math.pow(
                lmbd, intervalos[i].desde) * math.pow(math.e, -lmbd))/math.factorial(intervalos[i].desde)
            frecuenciaEsperada = round(probabilidadEsperada * cantidadMuestra)
            c = math.pow(
                (float(intervalos[i].cantidad) - frecuenciaEsperada), 2)/frecuenciaEsperada
            tabla.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde)))
            tabla.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta)))
            tabla.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad)))
            tabla.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada)))
            tabla.setItem(i, 4, QTableWidgetItem(str(c)))
            if (i > 0):
                sumatoria += float(tabla.item(i, 4).text())
            else:
                sumatoria = c
            tabla.setItem(i, 5, QTableWidgetItem(str(sumatoria)))

        v = cantidadIntervalos - 1 - 1
        tabulado = tabuladoChi(v)
        self.chiCalculadoTextEdit.setPlainText(str(sumatoria))
        self.chiTabuladoTextEdit.setPlainText(str(tabulado))
        self.resultadoChiTextEdit.setPlainText(validacion(sumatoria, tabulado))

        # vec = []
        # var = False
        # ind = -2
        # for i in range(cantidadIntervalos):
        #     if(ind != -1):
        #         if(intervalos[i].cantidad < 5):
        #             if (var):
        #                 intervalos[ind].cantidad += intervalos[i].cantidad
        #                 self.
        #                 intervalos[ind].hasta = intervalos[cantidadIntervalos].hasta
        #             else:
        #                 if(i != 0):
        #                     ind = i-1
        #                 else:
        #                     ind = -1
        #                 var = True
        #     else:
        #         if(intervalos[i].cantidad < 5):
        #             pass
        #         else:
        #             ind = i

        #     else:
        #         for j in range(cantidadIntervalos-i):
        #             contador += intervalos[j+i].cantidad
        #         if(contador < 5):
        #             intervalos[i-1].cantidad += intervalos[i].cantidad
        #             intervalos[i-1].hasta = intervalos[i].hasta
        #         else:
        #             intervalos[i].cantidad = contador
        #             intervalos[i].hasta = intervalos[cantidadIntervalos-1]

        # for i in range(cantidadIntervalos):
        #     for j in vec:
        #         if (j == i and j>2):
        #             intervalos[j]

        #         contador = 0
        #         for j in range(cantidadIntervalos-i):
        #             contador += datos[j+i].cantidad
        #         if(contador < 5):
        #             datos[i-1].cantidad += datos[i].cantidad
        #             datos[i-1].hasta = datos[i].hasta
        #         else:
        #             datos[i].cantidad = contador
        #             datos[i].hasta = datos[cantidadIntervalos-1]
