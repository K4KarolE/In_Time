from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSlider

class MySlider(QSlider):
    def __init__(self, window_type, min, max, setValue, valueChanged, sliderReleased, width, pos_x, pos_y):
        super().__init__()
        
        self.setParent(window_type)
        self.setGeometry(pos_x, pos_y, width, 20)
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(min)
        self.setMaximum(max)
        self.setValue(setValue)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.valueChanged.connect(valueChanged)
        self.sliderReleased.connect(sliderReleased)


