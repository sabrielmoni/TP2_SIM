# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from generadores import normal, exponencial, poisson, uniforme
from generadores import normal, exponencial, poisson, uniforme
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tabGenerador = QtWidgets.QWidget()
        self.tabGenerador.setWhatsThis("")
        self.tabGenerador.setAccessibleName("")
        self.tabGenerador.setObjectName("tabGenerador")
        self.normaLabel = QtWidgets.QLabel(self.tabGenerador)
        self.normaLabel.setGeometry(QtCore.QRect(20, 100, 121, 16))
        self.normaLabel.setObjectName("normaLabel")
        self.uniformeLabel = QtWidgets.QLabel(self.tabGenerador)
        self.uniformeLabel.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.uniformeLabel.setObjectName("uniformeLabel")
        self.expLabel = QtWidgets.QLabel(self.tabGenerador)
        self.expLabel.setGeometry(QtCore.QRect(20, 180, 151, 16))
        self.expLabel.setObjectName("expLabel")
        self.poissonLabel = QtWidgets.QLabel(self.tabGenerador)
        self.poissonLabel.setGeometry(QtCore.QRect(20, 260, 131, 16))
        self.poissonLabel.setObjectName("poissonLabel")
        self.intervalosLabel = QtWidgets.QLabel(self.tabGenerador)
        self.intervalosLabel.setGeometry(QtCore.QRect(20, 330, 61, 16))
        self.intervalosLabel.setObjectName("intervalosLabel")
        self.valoresLabel = QtWidgets.QLabel(self.tabGenerador)
        self.valoresLabel.setGeometry(QtCore.QRect(20, 370, 121, 16))
        self.valoresLabel.setObjectName("valoresLabel")
        self.aLabel = QtWidgets.QLabel(self.tabGenerador)
        self.aLabel.setGeometry(QtCore.QRect(180, 40, 16, 16))
        self.aLabel.setObjectName("aLabel")
        self.bLabel = QtWidgets.QLabel(self.tabGenerador)
        self.bLabel.setGeometry(QtCore.QRect(180, 70, 16, 16))
        self.bLabel.setObjectName("bLabel")
        self.mediaLabel = QtWidgets.QLabel(self.tabGenerador)
        self.mediaLabel.setGeometry(QtCore.QRect(180, 110, 41, 16))
        self.mediaLabel.setObjectName("mediaLabel")
        self.desviacionEstlabel = QtWidgets.QLabel(self.tabGenerador)
        self.desviacionEstlabel.setGeometry(QtCore.QRect(180, 140, 131, 16))
        self.desviacionEstlabel.setObjectName("desviacionEstlabel")
        self.lambdaExpLabel = QtWidgets.QLabel(self.tabGenerador)
        self.lambdaExpLabel.setGeometry(QtCore.QRect(180, 210, 60, 16))
        self.lambdaExpLabel.setObjectName("lambdaExpLabel")
        self.lambdaPoissonLabel = QtWidgets.QLabel(self.tabGenerador)
        self.lambdaPoissonLabel.setGeometry(QtCore.QRect(180, 280, 60, 16))
        self.lambdaPoissonLabel.setObjectName("lambdaPoissonLabel")
        self.mediaTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.mediaTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.mediaTextEdit.setGeometry(QtCore.QRect(310, 110, 104, 16))
        self.mediaTextEdit.setObjectName("mediaTextEdit")
        self.desvTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.desvTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.desvTextEdit.setGeometry(QtCore.QRect(310, 140, 104, 16))
        self.desvTextEdit.setObjectName("desvTextEdit")
        self.bTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.bTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.bTextEdit.setGeometry(QtCore.QRect(310, 70, 104, 16))
        self.bTextEdit.setObjectName("bTextEdit")
        self.aTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.aTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.aTextEdit.setGeometry(QtCore.QRect(310, 40, 104, 16))
        self.aTextEdit.setObjectName("aTextEdit")
        self.lambdaExpTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.lambdaExpTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.lambdaExpTextEdit.setGeometry(QtCore.QRect(310, 210, 104, 16))
        self.lambdaExpTextEdit.setObjectName("lambdaExpTextEdit")
        self.lambdaPoissonTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.lambdaPoissonTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.lambdaPoissonTextEdit.setGeometry(QtCore.QRect(310, 280, 104, 16))
        self.lambdaPoissonTextEdit.setObjectName("lambdaPoissonTextEdit")
        self.valoresTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.valoresTextEdit = QtWidgets.QLineEdit(self.tabGenerador)
        self.valoresTextEdit.setGeometry(QtCore.QRect(160, 370, 251, 20))
        self.valoresTextEdit.setObjectName("valoresTextEdit")
        self.intervalosComboBox = QtWidgets.QComboBox(self.tabGenerador)
        self.intervalosComboBox.setGeometry(QtCore.QRect(120, 330, 291, 22))
        self.intervalosComboBox.setObjectName("intervalosComboBox")
        self.intervalosComboBox.addItem("")
        self.intervalosComboBox.addItem("")
        self.intervalosComboBox.addItem("")
        self.intervalosComboBox.addItem("")
        self.intervalosComboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.tabGenerador)
        self.tableWidget.setGeometry(QtCore.QRect(430, 0, 351, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.generarGraficoPushButton = QtWidgets.QPushButton(
            self.tabGenerador)
        self.generarGraficoPushButton.setGeometry(
            QtCore.QRect(530, 480, 171, 26))
        self.generarGraficoPushButton = QtWidgets.QPushButton(
            self.tabGenerador)
        self.generarGraficoPushButton.setGeometry(
            QtCore.QRect(530, 480, 171, 26))
        self.generarGraficoPushButton.setObjectName("generarGraficoPushButton")
        self.generarGraficoPushButton.clicked.connect(self.generarGrafico)
        self.generarGraficoPushButton.clicked.connect(self.generarGrafico)
        self.generarPushButton = QtWidgets.QPushButton(self.tabGenerador)
        self.generarPushButton.setGeometry(QtCore.QRect(530, 440, 81, 26))
        self.generarPushButton.setObjectName("generarPushButton")
        self.generarPushButton.clicked.connect(self.generador)
        self.limpiarPushButton = QtWidgets.QPushButton(self.tabGenerador)
        self.limpiarPushButton.setGeometry(QtCore.QRect(620, 440, 81, 26))
        self.limpiarPushButton.setObjectName("limpiarPushButton")
        self.limpiarPushButton.clicked.connect(self.limpiarCampos)
        self.limpiarPushButton.clicked.connect(self.limpiarCampos)
        self.tabWidget.addTab(self.tabGenerador, "")
        self.tabChiCuadrado = QtWidgets.QWidget()
        self.tabChiCuadrado.setObjectName("tabChiCuadrado")
        self.chiTableWidget = QtWidgets.QTableWidget(self.tabChiCuadrado)
        self.chiTableWidget.setGeometry(QtCore.QRect(10, 0, 771, 421))
        self.chiTableWidget.setObjectName("chiTableWidget")
        self.chiTableWidget.setColumnCount(6)
        self.chiTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.chiTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.chiTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.chiTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.chiTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.chiTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.chiTableWidget.setHorizontalHeaderItem(5, item)
        self.chiCalculadoLabel = QtWidgets.QLabel(self.tabChiCuadrado)
        self.chiCalculadoLabel.setGeometry(QtCore.QRect(10, 440, 91, 16))
        self.chiCalculadoLabel.setObjectName("chiCalculadoLabel")
        self.chiTabuladoLabel = QtWidgets.QLabel(self.tabChiCuadrado)
        self.chiTabuladoLabel.setGeometry(QtCore.QRect(10, 470, 81, 16))
        self.chiTabuladoLabel.setObjectName("chiTabuladoLabel")
        self.chiCalculadoTextEdit = QtWidgets.QTextEdit(self.tabChiCuadrado)
        self.chiCalculadoTextEdit.setGeometry(QtCore.QRect(110, 440, 181, 21))
        self.chiCalculadoTextEdit.setObjectName("chiCalculadoTextEdit")
        self.chiTabuladoTextEdit = QtWidgets.QTextEdit(self.tabChiCuadrado)
        self.chiTabuladoTextEdit.setGeometry(QtCore.QRect(110, 470, 181, 21))
        self.chiTabuladoTextEdit.setObjectName("chiTabuladoTextEdit")
        self.resultadoChiTextEdit = QtWidgets.QTextEdit(self.tabChiCuadrado)
        self.resultadoChiTextEdit.setGeometry(QtCore.QRect(390, 450, 321, 31))
        self.resultadoChiTextEdit.setObjectName("resultadoChiTextEdit")
        self.tabWidget.addTab(self.tabChiCuadrado, "")
        self.tabKS = QtWidgets.QWidget()
        self.tabKS.setObjectName("tabKS")
        self.ksTableWidget = QtWidgets.QTableWidget(self.tabKS)
        self.ksTableWidget.setGeometry(QtCore.QRect(10, 0, 771, 421))
        self.ksTableWidget.setObjectName("ksTableWidget")
        self.ksTableWidget.setColumnCount(9)
        self.ksTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ksTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ksTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ksTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ksTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ksTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ksTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ksTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.ksTableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.ksTableWidget.setHorizontalHeaderItem(8, item)
        self.ksCalculadoLabel = QtWidgets.QLabel(self.tabKS)
        self.ksCalculadoLabel.setGeometry(QtCore.QRect(10, 440, 91, 16))
        self.ksCalculadoLabel.setObjectName("ksCalculadoLabel")
        self.ksTabuladoLabel = QtWidgets.QLabel(self.tabKS)
        self.ksTabuladoLabel.setGeometry(QtCore.QRect(10, 470, 91, 16))
        self.ksTabuladoLabel.setObjectName("ksTabuladoLabel")
        self.ksCalculadoLineEdit = QtWidgets.QTextEdit(self.tabKS)
        self.ksCalculadoLineEdit.setGeometry(QtCore.QRect(110, 440, 181, 22)) 
        self.ksCalculadoLineEdit.setObjectName("ksCalculadoLineEdit")
        self.ksTabuladoLineEdit = QtWidgets.QTextEdit(self.tabKS)
        self.ksTabuladoLineEdit.setGeometry(QtCore.QRect(110, 470, 181, 22))
        self.ksTabuladoLineEdit.setObjectName("ksTabuladoLineEdit")
        self.resultadoKsTextEdit = QtWidgets.QTextEdit(self.tabKS)
        self.resultadoKsTextEdit.setGeometry(QtCore.QRect(400, 450, 321, 31))
        self.resultadoKsTextEdit.setObjectName("resultadoKsTextEdit")
        self.tabWidget.addTab(self.tabKS, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.normaLabel.setText(_translate(
            "MainWindow", "Distribución Normal"))
        self.uniformeLabel.setText(_translate(
            "MainWindow", "Distribución Uniforme"))
        self.expLabel.setText(_translate(
            "MainWindow", "Distribución Exponencial"))
        self.poissonLabel.setText(_translate(
            "MainWindow", "Distribución Poisson"))
        self.normaLabel.setText(_translate(
            "MainWindow", "Distribución Normal"))
        self.uniformeLabel.setText(_translate(
            "MainWindow", "Distribución Uniforme"))
        self.expLabel.setText(_translate(
            "MainWindow", "Distribución Exponencial"))
        self.poissonLabel.setText(_translate(
            "MainWindow", "Distribución Poisson"))
        self.intervalosLabel.setText(_translate("MainWindow", "Intervalos"))
        self.valoresLabel.setText(_translate(
            "MainWindow", "Cantidad de Valores"))
        self.valoresLabel.setText(_translate(
            "MainWindow", "Cantidad de Valores"))
        self.aLabel.setText(_translate("MainWindow", "a"))
        self.bLabel.setText(_translate("MainWindow", "b"))
        self.mediaLabel.setText(_translate("MainWindow", "Media"))
        self.desviacionEstlabel.setText(
            _translate("MainWindow", "Desviación Estandar"))
        self.desviacionEstlabel.setText(
            _translate("MainWindow", "Desviación Estandar"))
        self.lambdaExpLabel.setText(_translate("MainWindow", "Lambda"))
        self.lambdaPoissonLabel.setText(_translate("MainWindow", "Lambda"))
        self.intervalosComboBox.setItemText(0, _translate("MainWindow", "5"))
        self.intervalosComboBox.setItemText(1, _translate("MainWindow", "10"))
        self.intervalosComboBox.setItemText(2, _translate("MainWindow", "12"))
        self.intervalosComboBox.setItemText(3, _translate("MainWindow", "15"))
        self.intervalosComboBox.setItemText(4, _translate("MainWindow", "20"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "i"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Valor"))
        self.generarGraficoPushButton.setText(
            _translate("MainWindow", "Generar Gráfico"))
        self.generarGraficoPushButton.setText(
            _translate("MainWindow", "Generar Gráfico"))
        self.generarPushButton.setText(_translate("MainWindow", "Generar"))
        self.limpiarPushButton.setText(_translate("MainWindow", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabGenerador), _translate("MainWindow", "Generador"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabGenerador), _translate("MainWindow", "Generador"))
        item = self.chiTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Desde"))
        item = self.chiTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hasta"))
        item = self.chiTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Frec.  Obtenida"))
        item = self.chiTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Frec.  Esperada"))
        item = self.chiTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "C"))
        item = self.chiTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "C(ac)"))
        self.chiCalculadoLabel.setText(
            _translate("MainWindow", "Chi Calculado"))
        self.chiTabuladoLabel.setText(_translate("MainWindow", "Chi Tabulado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabChiCuadrado), _translate("MainWindow", "Prueba Chi Cuadrado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabChiCuadrado), _translate("MainWindow", "Prueba Chi Cuadrado"))
        item = self.ksTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Desde"))
        item = self.ksTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hasta"))
        item = self.ksTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fo"))
        item = self.ksTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fe"))
        item = self.ksTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Po"))
        item = self.ksTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Pe"))
        item = self.ksTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "PoAC"))
        item = self.ksTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "PeAC"))
        item = self.ksTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "|PoAC - PeAC|"))
        self.ksCalculadoLabel.setText(
            _translate("MainWindow", "K-S Calculado"))
        self.ksCalculadoLabel.setText(
            _translate("MainWindow", "K-S Calculado"))
        self.ksTabuladoLabel.setText(_translate("MainWindow", "K-S Tabulado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabKS), _translate("MainWindow", "Prueba K-S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
