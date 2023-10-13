from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

import sys
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("Image")
        self.setGeometry(0, 0, 400, 300)
 
        # FIRST IMAGE - SMOOTHTRANSFORMATION
        self.label = QLabel(self)
        self.pixmap = QPixmap('skins/_icons/icon_settings.png').scaledToWidth(30, Qt.TransformationMode.SmoothTransformation)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.label.move(70, 70)

        # SECOND IMAGE
        label_2 = QLabel(self)
        pixmap_2 = QPixmap('skins/_icons/icon_settings.png').scaledToWidth(30)
        label_2.setPixmap(pixmap_2)
        label_2.resize(pixmap_2.width(),
                          pixmap_2.height())
        label_2.move(120, 70)
 

        self.move(800, 800)
        self.show()
 

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())