from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class MyImage(QLabel):
    def __init__(self, window_type, img_name, img_size, pos_x, pos_y):
        super().__init__()
        
        self.setParent(window_type)
        self.image = QPixmap(f'skins/_images/{img_name}').scaledToWidth(img_size, Qt.TransformationMode.SmoothTransformation)
        self.setPixmap(self.image)
        self.resize(self.image.width(), self.image.height())
        self.move(pos_x, pos_y)