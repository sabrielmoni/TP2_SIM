from PyQt5.QtWidgets import *
import math


def tabuladoChi(n):
    if (n == 1):
        return 5.02
    elif (n == 2):
        return 7.35
    elif (n == 3):
        return 9.35
    elif (n == 4):
        return 11.1
    elif (n == 5):
        return 12.8
    elif (n == 6):
        return 14.4
    elif (n == 7):
        return 16
    elif (n == 8):
        return 17.5
    elif (n == 9):
        return 19
    elif (n == 10):
        return 20.5
    elif (n == 11):
        return 21.9


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

    def sumar():
        cantidad += 1

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

    def uniformeChi(self, datos, n):
        tabla = self.chiTableWidget
        cantidadIntervalos = len(datos)
        cantidadMuestra = n
        sumatoria = 0
        frecuenciaEsperada = cantidadMuestra/cantidadIntervalos

        for i in range(cantidadIntervalos):
            tabla.insertRow(i)
            c = math.pow(
                (float(datos[i].cantidad) - frecuenciaEsperada), 2)/frecuenciaEsperada
            tabla.setItem(i, 0, QTableWidgetItem(
                str(datos[i].desde)))
            tabla.setItem(i, 1, QTableWidgetItem(
                str(datos[i].hasta)))
            tabla.setItem(i, 2, QTableWidgetItem(
                str(datos[i].cantidad)))
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
