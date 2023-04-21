from PyQt5.QtWidgets import *
import math


def tabuladoChi(v):
    '''Devuelve el valor de Chi tabulado para un determinado valor de libertad'''
    tabuladoChi = [3.84, 5.99, 7.81, 9.49, 11.1, 12.6, 14.1, 15.5, 16.9,
                   18.3, 19.7, 21.0, 22.4, 23.7, 25.0, 26.3, 27.6, 28.9,
                   30.1, 31.4, 32.7, 33.9, 35.2, 36.4, 37.7, 38.9, 40.1, 41.3, 42.6, 43.8]
    return tabuladoChi[v-1]


def tabuladoKS(n):
    '''Devuelve el valor de KS tabulado para un determinado valor de libertad'''
    tabuladoKS = [0.975, 0.84189, 0.70760, 0.62394, 0.56328, 0.51926, 0.48342, 0.45427,
                  0.43001, 0.40925, 0.39122, 0.37543, 0.36143, 0.3489, 0.3375, 0.32733,
                  0.31796, 0.30936, 0.30143, 0.29408, 0.28724, 0.28087, 0.2749, 0.26931,
                  0.26404, 0.25908, 0.25438, 0.24993, 0.24571, 0.24170, 0.23788, 0.23424,
                  0.23076, 0.22743, 0.22425]
    if (n > 34):
        tabuladoKS = 1.36/math.sqrt(n)
    else:
        tabuladoKS = tabuladoKS[n-1]
    return tabuladoKS


def validacion(calculado, tabulado):
    '''Compara los calculados y tabulados y devuelve el resultado de la prueba'''
    if (calculado <= tabulado):
        return "NO SE RECHAZA LA HIPOTESIS"
    else:
        return "SE RECHAZA LA HIPOTESIS"


class Prueba:
    def __init__(self, desde, hasta, cantidad):
        self.desde = desde
        self.hasta = hasta
        self.cantidad = cantidad

    def uniformeChi(self, intervalos):
        '''Calcula chi cuadrado y KS para la distribucion uniforme
            entran intervalos con fo'''
        tablaChi = self.chiTableWidget
        tablaKS = self.ksTableWidget

        cantidadIntervalos = len(intervalos)
        cantidadMuestra = int(self.valoresTextEdit.text())
        sumatoria = 0
        frecuenciaEsperada = cantidadMuestra/cantidadIntervalos
        probabilidadEsperada = 1/cantidadIntervalos
        poAc = 0
        peAc = 0
        maximo = 0

        for i in range(cantidadIntervalos):
            tablaChi.insertRow(i)
            tablaKS.insertRow(i)

            probabilidadObservada = intervalos[i].cantidad / cantidadMuestra
            c = math.pow(
                (float(intervalos[i].cantidad) - frecuenciaEsperada), 2)/frecuenciaEsperada
            tablaChi.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde)))
            tablaChi.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta)))
            tablaChi.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad)))
            tablaChi.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada)))
            tablaChi.setItem(i, 4, QTableWidgetItem(str(c)))
            if (i > 0):
                sumatoria += float(tablaChi.item(i, 4).text())
            else:
                sumatoria = c
            tablaChi.setItem(i, 5, QTableWidgetItem(str(sumatoria)))

            tablaKS.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde)))
            tablaKS.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta)))
            tablaKS.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad)))
            tablaKS.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada)))
            tablaKS.setItem(i, 4, QTableWidgetItem(
                str(probabilidadObservada)))
            tablaKS.setItem(i, 5, QTableWidgetItem(
                str(probabilidadEsperada)))
            if (i > 0):
                poAc += float(tablaKS.item(i, 4).text())
                peAc += float(tablaKS.item(i, 5).text())
            else:
                poAc = probabilidadObservada
                peAc = probabilidadEsperada
            tablaKS.setItem(i, 6, QTableWidgetItem(
                str(poAc)))
            tablaKS.setItem(i, 7, QTableWidgetItem(
                str(peAc)))
            valorAbs = abs(poAc-peAc)
            tablaKS.setItem(i, 8, QTableWidgetItem(
                str(valorAbs)))

            if maximo < valorAbs:
                maximo = valorAbs

        v = cantidadIntervalos - 1 - 0
        tabuladochi = tabuladoChi(v)
        self.chiCalculadoTextEdit.setPlainText(str(sumatoria))
        self.chiTabuladoTextEdit.setPlainText(str(tabuladochi))
        self.resultadoChiTextEdit.setPlainText(
            validacion(sumatoria, tabuladochi))

        tabuladoks = tabuladoKS(cantidadMuestra)
        self.ksCalculadoLineEdit.setPlainText(str(maximo))
        self.ksTabuladoLineEdit.setPlainText(str(tabuladoks))
        self.resultadoKsTextEdit.setPlainText(validacion(maximo, tabuladoks))

    def normalChi(self, datos):
        '''Calcula KS y chi cuadrado para la distribucion normal
            entra vector de datos '''
        
        #incializa tabla y variables
        tablaChi = self.chiTableWidget
        tablaKS = self.ksTableWidget

        minimo = min(datos)
        maximo = max(datos)
        media = float(self.mediaTextEdit.text())
        desviacionEstandar = float(self.desvTextEdit.text())
        cantidadIntervalos = int(self.intervalosComboBox.currentText())
        intervalos = [0] * cantidadIntervalos
        cantidadMuestra = int(self.valoresTextEdit.text())
        paso = ((maximo - minimo) / cantidadIntervalos)
        maximoKS = 0
        peAc = 0
        poAc = 0

        #Realiza el calculo de los intervals y cuenta los valores en cada uno
        for i in range(len(intervalos)):

            intervalos[i] = Prueba(minimo, minimo+paso - 0.0001, 0)
            minimo += paso

        for i in range(len(datos)): #recorre los RND y los agrega en el intervalo correspondiente.
            for j in range(len(intervalos)): #para cada RND recorre los intervalos y verifica donde se encuentra
                if ((datos[i] >= intervalos[j].desde) and (datos[i] <= intervalos[j].hasta)):
                    intervalos[j].cantidad += 1
                    break

        for i in range(cantidadIntervalos): #por cada intervalo, agrega fila con valores correspondientes en tablas de chi y ks
            tablaChi.insertRow(i)
            tablaKS.insertRow(i)

            # Calcula datos a ingresar en filas
            x = (intervalos[i].desde + intervalos[i].hasta)/2
            probabilidadEsperada = (math.pow(math.e, (-0.5*(math.pow((x-media)/desviacionEstandar, 2)))))/(
                desviacionEstandar*math.sqrt(2*math.pi)) * paso
            probabilidadObservada = intervalos[i].cantidad / cantidadMuestra
            frecuenciaEsperada = probabilidadEsperada * cantidadMuestra
            c = math.pow(
                (float(intervalos[i].cantidad) - frecuenciaEsperada), 2)/frecuenciaEsperada

            
            tablaChi.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde))) #limite inferior del intervalo en la fila
            tablaChi.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta))) #limite superior del intervalo en la fila
            tablaChi.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad))) #freq Observada del intervalo en la fila
            tablaChi.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada))) #freq esperada del intervalo en la fila
            tablaChi.setItem(i, 4, QTableWidgetItem(str(c))) #valor C del intervalo en la fila
            if (i > 0):
                sumatoria += float(tablaChi.item(i, 4).text())
            else:
                sumatoria = c
            tablaChi.setItem(i, 5, QTableWidgetItem(str(sumatoria))) #Ingresa CAcumulado del intervalo en la fila

            tablaKS.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde))) # limite inferior del intervalo en la fila
            tablaKS.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta))) # limite superior del intervalo en la fila
            tablaKS.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad))) # freq Observada del intervalo en la fila
            tablaKS.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada))) # freq esperada del intervalo en la fila
            tablaKS.setItem(i, 4, QTableWidgetItem(
                str(probabilidadObservada))) # probabilidad observada del intervalo en la fila
            tablaKS.setItem(i, 5, QTableWidgetItem(
                str(probabilidadEsperada))) # probabilidad esperada del intervalo en la fila
            if (i > 0):
                poAc += float(tablaKS.item(i, 4).text())
                peAc += float(tablaKS.item(i, 5).text())
            else:
                poAc = probabilidadObservada
                peAc = probabilidadEsperada
            tablaKS.setItem(i, 6, QTableWidgetItem(
                str(poAc))) # prob Obs. acumulada del intervalo en la fila
            tablaKS.setItem(i, 7, QTableWidgetItem(
                str(peAc))) # prob Esp. acumulada del intervalo en la fila
            valorAbs = abs(poAc-peAc)
            tablaKS.setItem(i, 8, QTableWidgetItem(
                str(valorAbs))) # Valor absoluto de las dos acumuladas

            if maximoKS < valorAbs:
                maximoKS = valorAbs

        v = cantidadIntervalos - 1 - 2

        #calcula resultado de chi 
        tabulado = tabuladoChi(v)
        self.chiCalculadoTextEdit.setPlainText(str(sumatoria))
        self.chiTabuladoTextEdit.setPlainText(str(tabulado))
        self.resultadoChiTextEdit.setPlainText(validacion(sumatoria, tabulado))

        #calcula resultado de ks
        tabuladoks = tabuladoKS(cantidadMuestra)
        self.ksCalculadoLineEdit.setPlainText(str(maximoKS))
        self.ksTabuladoLineEdit.setPlainText(str(tabuladoks))
        self.resultadoKsTextEdit.setPlainText(validacion(maximoKS, tabuladoks))

    def exponencialChi(self, datos):
        '''Calcula KS y chi cuadrado para la distribucion exponencial
            entra vector de datos '''
        
        #Inicializa las variables y las tablas
        tablaChi = self.chiTableWidget
        tablaKS = self.ksTableWidget

        minimo = min(datos)
        maximo = max(datos)
        lmbd = float(self.lambdaExpTextEdit.text())
        cantidadIntervalos = int(self.intervalosComboBox.currentText())
        intervalos = [0] * cantidadIntervalos
        cantidadMuestra = int(self.valoresTextEdit.text())
        paso = ((maximo - minimo) / cantidadIntervalos)
        maximoKS = 0
        peAc = 0
        poAc = 0

        #Realiza el calculo de los intervals y cuenta los valores en cada uno
        for i in range(len(intervalos)):

            intervalos[i] = Prueba(minimo, minimo+paso - 0.0001, 0)
            minimo += paso

        for i in range(len(datos)): #recorre los RND y los agrega en el intervalo correspondiente.
            for j in range(len(intervalos)):
                if ((datos[i] >= intervalos[j].desde) and (datos[i] <= intervalos[j].hasta)):
                    intervalos[j].cantidad += 1
                    break

        for i in range(cantidadIntervalos): #por cada intervalo, agrega fila con valores correspondientes en tablas de chi y ks
            tablaChi.insertRow(i)
            tablaKS.insertRow(i)

            #calcula valores para tabla chi
            probabilidadEsperada = (1-math.pow(math.e, -lmbd*intervalos[i].hasta)) - (
                1-math.pow(math.e, -lmbd*intervalos[i].desde))
            probabilidadObservada = intervalos[i].cantidad / cantidadMuestra
            frecuenciaEsperada = probabilidadEsperada * cantidadMuestra
            c = math.pow(
                (float(intervalos[i].cantidad) - frecuenciaEsperada), 2)/frecuenciaEsperada

            tablaChi.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde))) #limite inferior del intervalo en la fila
            tablaChi.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta)))#limite superior del intervalo en la fila
            tablaChi.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad))) # freq Observada del intervalo en la fila
            tablaChi.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada))) # freq esperada  del intervalo en la fila
            tablaChi.setItem(i, 4, QTableWidgetItem(str(c))) # valor C del intervalo en la fila

            if (i > 0):
                sumatoria += float(tablaChi.item(i, 4).text())
            else:
                sumatoria = c
            tablaChi.setItem(i, 5, QTableWidgetItem(str(sumatoria))) # CAcum del intervalo en la fila

            tablaKS.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde))) #limite inferior del intervalo en la fila
            tablaKS.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta))) #limite superior del intervalo en la fila
            tablaKS.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad))) # freq Observada del intervalo en la fila
            tablaKS.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada))) # freq esperada del intervalo en la fila
            tablaKS.setItem(i, 4, QTableWidgetItem(
                str(probabilidadObservada))) # prob Observada del intervalo en la fila
            tablaKS.setItem(i, 5, QTableWidgetItem(
                str(probabilidadEsperada))) # prob esperada del intervalo en la fila
            if (i > 0):
                poAc += float(tablaKS.item(i, 4).text())
                peAc += float(tablaKS.item(i, 5).text())
            else:
                poAc = probabilidadObservada
                peAc = probabilidadEsperada
            tablaKS.setItem(i, 6, QTableWidgetItem(
                str(poAc))) # prob Obs acum del intervalo en la fila
            tablaKS.setItem(i, 7, QTableWidgetItem(
                str(peAc))) # prob Esp acum del intervalo en la fila
            valorAbs = abs(poAc-peAc)
            tablaKS.setItem(i, 8, QTableWidgetItem(
                str(valorAbs))) # absoluto de dif de probs del intervalo en la fila

            if maximoKS < valorAbs:
                maximoKS = valorAbs

        v = cantidadIntervalos - 1 - 1

        #calcular resultado de chi
        tabulado = tabuladoChi(v)
        self.chiCalculadoTextEdit.setPlainText(str(sumatoria))
        self.chiTabuladoTextEdit.setPlainText(str(tabulado))
        self.resultadoChiTextEdit.setPlainText(validacion(sumatoria, tabulado))

        #calcular resultado de KS
        tabuladoks = tabuladoKS(cantidadMuestra)
        self.ksCalculadoLineEdit.setPlainText(str(maximoKS))
        self.ksTabuladoLineEdit.setPlainText(str(tabuladoks))
        self.resultadoKsTextEdit.setPlainText(validacion(maximoKS, tabuladoks))

    def poissonChi(self, datos):
        '''Calcula chi cuadrado para la distribucion exponencial
            entra vector de datos '''
        
        tablaChi = self.chiTableWidget
        tablaKS = self.ksTableWidget

        minimo = min(datos)
        maximo = max(datos)
        lmbd = float(self.lambdaPoissonTextEdit.text())
        cantidadIntervalos = (maximo - minimo)
        intervalos = [0] * cantidadIntervalos
        cantidadMuestra = int(self.valoresTextEdit.text())
        paso = 1

        for i in range(len(intervalos)):

            intervalos[i] = Prueba(minimo, minimo, 0)
            minimo += paso

        for i in range(len(datos)):
            for j in range(len(intervalos)):
                if (datos[i] == intervalos[j].desde):
                    intervalos[j].cantidad += 1
                    break

        for i in range(cantidadIntervalos):
            tablaChi.insertRow(i)
            tablaKS.insertRow(i)

            probabilidadEsperada = (math.pow(
                lmbd, intervalos[i].desde) * math.pow(math.e, -lmbd))/math.factorial(intervalos[i].desde)
            frecuenciaEsperada = round(probabilidadEsperada * cantidadMuestra)
            c = math.pow(
                (float(intervalos[i].cantidad) - frecuenciaEsperada), 2)/frecuenciaEsperada
            tablaChi.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde)))
            tablaChi.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta)))
            tablaChi.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad)))
            tablaChi.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada)))
            tablaChi.setItem(i, 4, QTableWidgetItem(str(c)))
            if (i > 0):
                sumatoria += float(tablaChi.item(i, 4).text())
            else:
                sumatoria = c
            tablaChi.setItem(i, 5, QTableWidgetItem(str(sumatoria)))

            tablaKS.setItem(i, 0, QTableWidgetItem(
                str(intervalos[i].desde)))
            tablaKS.setItem(i, 1, QTableWidgetItem(
                str(intervalos[i].hasta)))
            tablaKS.setItem(i, 2, QTableWidgetItem(
                str(intervalos[i].cantidad)))
            tablaKS.setItem(i, 3, QTableWidgetItem(
                str(frecuenciaEsperada)))
            tablaKS.setItem(i, 4, QTableWidgetItem(
                str(probabilidadEsperada)))

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
