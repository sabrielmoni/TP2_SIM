from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import sys

class AppWin(QMainWindow, Ui_MainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.setupUi(self)

        # Se genera la interfaz llamando al metodo setupUi
        
if __name__ == '__main__':
    app = QApplication(sys.argv) # create an instance of the application
    window = QWidget() # create an instance of a window
    window.show() # to make the window visible
    app.exec() # to start up the event loop
