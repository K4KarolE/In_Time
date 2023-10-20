from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSlider


class MySlider(QSlider):
    def __init__(self, window_type, min, max, setValue, valueChanged, width, pos_x, pos_y):
        super().__init__()
        
        self.setParent(window_type)
        self.setGeometry(pos_x, pos_y, width, 20)
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(min)
        self.setMaximum(max)
        self.setValue(setValue)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.valueChanged.connect(valueChanged)


class MySliderSettingsWindow(MySlider):
    def __init__(self, window_type, min, max, setValue, valueChanged, width, pos_x, pos_y, sliderReleased):
        super().__init__(window_type, min, max, setValue, valueChanged, width, pos_x, pos_y)
        self.sliderReleased.connect(sliderReleased)


