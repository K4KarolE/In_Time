from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

from .cons_and_vars import skin_selected, selected_skin_folder


def window_main_set_style(self, button_color, button_color_clicked):
    self.setStyleSheet(
                    "QMainWindow"
                        "{"
                        f"background-color : {button_color};"
                        "border-radius: 10px;"
                        "}"
                    "QPushButton"
                        "{"
                        f"background-color : QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 0.3 {button_color}, stop: 0.6 {button_color}, stop: 1 {button_color_clicked});"
                        "border-radius: 6px;"
                        "border: 3px solid black;"
                        "}"
                    "QPushButton::pressed"
                        "{"
                        f"background-color : {button_color_clicked};"
                        "}"
                    "QSlider::handle"
                        "{"
                        f"background-color : 'black';"
                        "}"
                    )


class MyMainWindow(QMainWindow):
    def __init__(self, button_color, button_color_clicked, width, height):
        super().__init__()

        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setWindowTitle(selected_skin_folder['window_title'])
        self.setWindowIcon(QIcon(f'skins/{skin_selected}/icon.ico'))
        window_main_set_style(self, button_color, button_color_clicked)
