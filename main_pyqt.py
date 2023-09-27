'''
Motion in Time - PyQt6 version

Work in progress
'''

import sys
from pathlib import Path

from time import strftime
from json import load, dump
from pathlib import Path
from pygame import mixer


from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QMovie, QIcon, QPixmap, QPalette, QColor, QFont
from PyQt6.QtCore import QSize, QDir



class Music:
    def __init__(self, on, volume):
        self.on = on
        self.volume = volume

class Animation:
    def __init__(self, speed):
        self.speed = speed
    
class Params:
    def __init__(self, value):
        self.value = value


def open_settings():
    f = open(path_json)
    settings_data = load(f)
    return settings_data

def save_settings(settings_data):
    with open(path_json, 'w') as f:
        dump(settings_data, f, indent=2)
    return





# DIRECTORY AND JSON PATH
working_directory = Path(__file__).parent
path_json = Path(working_directory, 'settings_db_pyqt.json')

# MIXER
mixer.init()



########################################################################


def load_info():
        settings_data = open_settings()
        skin_selected = settings_data['skin_selected']                                  
        selected_skin_folder = settings_data['skins'][skin_selected]
        return settings_data, skin_selected, selected_skin_folder


# def time_display():
    # TIME
    # hours_and_mins = strftime('%H:%M')
    # seconds = strftime(':%S')
    # TOP
    
    # canvas.itemconfig(hours_and_mins_display, text=hours_and_mins)
    # canvas.itemconfig(seconds_display, text=seconds)
    # BACK - "SHADOW"
    # canvas.itemconfig(hours_and_mins_display_2nd, text=hours_and_mins)
    # canvas.itemconfig(seconds_display_2nd, text=seconds)
    # # CALLBACK
    # canvas.after(1000, lambda:time_display())



# MUSIC
def music_stop():
    mixer.music.fadeout(0)


def music_load_play():
    mixer.music.load(Path(working_directory, 'skins', skin_selected, 'music.mp3'))
    mixer.music.set_volume(music.volume)
    mixer.music.play(loops=-1)


def music_switch_on_off():
    
    settings_data, skin_selected, selected_skin_folder = load_info()
    
    # MUSIC ON --> OFF
    if settings_data['music_on']:
        music_stop()
        settings_data['music_on'] = False
        button_music.setIcon(button_image_start)

    # MUSIC OFF --> ON
    else:
        music_load_play()
        settings_data['music_on'] = True
        button_music.setIcon(button_image_stop)

    selected_skin_folder['music_volume'] = music.volume
    save_settings(settings_data)





# JSON / SETTINGS / SKIN - LOAD INFO
settings_data, skin_selected, selected_skin_folder = load_info()

# MUSIC
music = Music(settings_data['music_on'], selected_skin_folder['music_volume'])

# ANIMATION
count = 0
animation = Animation(selected_skin_folder['animation_speed'])  # 100% = original

# BUTTONS
button_bg_color = selected_skin_folder['button_bg_color']
button_bg_color_clicked = selected_skin_folder['button_bg_color_clicked']
button_pos_x = selected_skin_folder['button_pos_x']
button_pos_y = selected_skin_folder['button_pos_y']

# TIME
time_font_color = selected_skin_folder['time_font_color']
time_font_style = selected_skin_folder['time_font_style']
time_hm_font_size = selected_skin_folder['time_hm_font_size']
time_sec_font_size = selected_skin_folder['time_sec_font_size']

# HOURS & MINUTES
time_hm_pos_x = selected_skin_folder['time_hm_pos_x']
time_hm_pos_y = selected_skin_folder['time_hm_pos_y']

# SECONDS
time_sec_pos_x = selected_skin_folder['time_sec_pos_x']
time_sec_pos_y = selected_skin_folder['time_sec_pos_y']

# CANVAS 2nd - SETTINGS
canvas_settings_orentation = selected_skin_folder['canvas_settings_orentation']
canvas_settings_pos_x_diff = selected_skin_folder['canvas_settings_pos_x_diff']








##################################################################################

# if __name__ == "__main__":

# APP / WINDOW
app = QApplication(sys.argv)
window = QMainWindow()
window.resize(720, 486)
window.setWindowTitle(selected_skin_folder['window_title'])
window.setWindowIcon(QIcon(f'skins/{skin_selected}/icon.ico'))


# ANIMATION LABEL
label_animation = QLabel(window)
    
       
# BUTTON - SETTINGS
button_image_settings = QIcon('skins/_icons/icon_settings.png')
button_settings = QPushButton(window, text=None, icon=button_image_settings)
button_settings.setIconSize(QSize(20,20))       # icon sizing
button_settings.setGeometry(button_pos_x, button_pos_y, 30, 30)     # pos, pos, size, size


# TIME
hours_and_mins_display = QLabel(window, text=strftime('%H:%M')) #strftime('%H:%M')
hours_and_mins_display.setGeometry(20, 20, 720, 486)
hours_and_mins_display.setStyleSheet(f'color:{time_font_color}; background: black; font: 10pt {time_font_style};')


# BUTTON - MUSIC
button_image_start = QIcon('skins/_icons/icon_start.png')
button_image_stop = QIcon('skins/_icons/icon_stop.png')

if music.on:
        music_start_stop_img = button_image_stop
else:
    music_start_stop_img = button_image_start

pos_y_diff = 33
button_music = QPushButton(window, text=None, icon=music_start_stop_img)
button_music.setIconSize(QSize(20,20))
button_music.setGeometry(button_pos_x, button_pos_y+pos_y_diff, 29, 29)     # pos, pos, size, size
button_music.clicked.connect(music_switch_on_off)


# WIDGETS STYLE
# Simplified example, just for a button:
# button_color = 'red'
# button_example.setStyleSheet(f"background-color: {button_color}; border: 2px solid red;")
window.setStyleSheet("QPushButton"
                        # DEFAULT
                        "{"
                        f"background-color : {button_bg_color};"
                        "border-radius: 5px;"          # corner roundness
                        "border: 2px solid black;"
                        "}"
                        # CLICKED
                        "QPushButton::pressed"
                        "{"
                        f"background-color : {button_bg_color_clicked};"
                        "}"
                        )



# ANIMATION
# movie = QMovie(f'skins/{skin_selected}/GIF.GIF')
# label_animation.setMovie(movie)
# label_animation.resize(720,486)
# movie.start()
# movie.setSpeed(animation.speed)

window.show()


if music.on: music_load_play()

sys.exit(app.exec())