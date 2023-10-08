from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class MyImage():
    def __init__(self, window_type, img_name, img_size, pos_x, pos_y):
        self = QLabel(window_type)
        self.image = QPixmap(f'skins/_icons/{img_name}').scaledToWidth(img_size, Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(self.image)
        self.resize(self.image.width(), self.image.height())
        self.move(pos_x, pos_y)