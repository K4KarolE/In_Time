import sys
from pathlib import Path

from PyQt6.QtCore import QDir
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QToolButton, QWidget, QVBoxLayout, QLabel, QMainWindow

image_path = QDir('skins/terminator/GIF.GIF').path()

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Display Image")

        c_widget = QWidget()
        layout = QVBoxLayout(c_widget)

        pixmap = QPixmap(image_path)

        label = QLabel()
        label.setPixmap(pixmap)

        layout.addWidget(label)

        self.setCentralWidget(c_widget)

app = QApplication(sys.argv)
window = MyApp()
window.show()
app.exec()