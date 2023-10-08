from PyQt6.QtCore import QRect, Qt
from PyQt6.QtWidgets import QSlider

class MySlider(QSlider):
    def __init__(self, window_type, min, max, setValue, valueChanged, sliderReleased, pos_x, pos_y):
        super().__init__()

        self = QSlider(window_type)
        self.setGeometry(QRect(pos_x, pos_y, 160, 20))
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(min)
        self.setMaximum(max)
        self.setValue(setValue)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.valueChanged.connect(valueChanged)
        self.sliderReleased.connect(sliderReleased)


# slider_volume = MySlider(
#     window_settings,
#     min=0,
#     max=100,
#     setValue=int(cv.music_volume*100),
#     valueChanged=change_volume,
#     sliderReleased=save_volume,
#     pos_x=slider_pos_x,
#     pos_y=slider_pos_y)


# # slider_volume.setValue(50)
# print(int(cv.music_volume*100))
# print('main: ', slider_volume.value())
    


# slider_animation_speed = MySlider(
#     window_settings,
#     min=0,
#     max=300,
#     setValue=cv.animation_speed,
#     valueChanged=change_animation_speed,
#     sliderReleased=save_animation_speed,
#     pos_x=slider_pos_x,
#     pos_y=slider_pos_y*3 - 5)

# print('main: ', slider_animation_speed.value())
