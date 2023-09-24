'''
Original from: https://pythonpyqt.com/pyqt-gif/
Cheers lads!
'''

from PyQt6.QtCore import QDir
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QMovie
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        self.movie = QMovie(image_path)
        self.label.setMovie(self.movie)
        self.movie.start()
        self.movie.setSpeed(100)    # =%


# IMAGE PATH
skin_selected = 'terminator'

def new_path(skin_selected):
    image_path = QDir(f'skins/{skin_selected}/GIF.GIF').path()
    return image_path
image_path = new_path(skin_selected)


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(window)

    # CHANGE ANIMATION
    image_path = new_path('donnie_darko')
    ui.movie = QMovie(image_path)
    ui.label.setMovie(ui.movie)
    ui.movie.start()

    # CHANGE ANIMATION SPEED
    ui.movie.setSpeed(50)
    
    window.show()
    sys.exit(app.exec())