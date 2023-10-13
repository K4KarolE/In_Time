'''
Original from: https://pythonpyqt.com/pyqt-gif/
Cheers lads!
'''

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QMovie

import sys


class Ui_MainWindow:
    def setupUi(self, MainWindow, skin_selected):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 486)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(5, 5, 5, 5))
        # self.label.setMinimumSize(QtCore.QSize(800, 600))
        # self.label.setMaximumSize(QtCore.QSize(800, 600))
        # self.label.setObjectName("label")

        # add label to main window
        MainWindow.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie(f'skins/{skin_selected}/GIF.GIF')
        self.label.setMovie(self.movie)
        self.movie.start()
        self.movie.setSpeed(100)    # =%



if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()


    skin_selected = 'terminator'
    ui.setupUi(window, skin_selected)
    
    ui.movie.start()
    window.show()

    sys.exit(app.exec())

    