'''
Motion in Time - PyQt6 version

Work in progress
'''

import sys
from pathlib import Path

from json import load, dump
from pathlib import Path


from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QSlider, QComboBox
from PyQt6.QtGui import QMovie, QIcon, QPixmap
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, QTimer, QTime, Qt, QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer



class Music:
    def __init__(self):
        self.path_music = Path(working_directory, 'skins', skin_selected, 'music.mp3')
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(str(self.path_music)))
        self.player.setLoops(-1) # -1=infinite
        self.on = settings_data['music_on']
        self.volume = selected_skin_folder['music_volume']
        self.audio_output.setVolume(self.volume)


class Animation:
    def __init__(self, speed):
        self.speed = speed
    



def open_settings():
    f = open(path_json)
    settings_data = load(f)
    return settings_data


def save_settings(settings_data):
    with open(path_json, 'w') as f:
        dump(settings_data, f, indent=2)
    return


def load_info():
    settings_data = open_settings()
    skin_selected = settings_data['skin_selected']                                  
    selected_skin_folder = settings_data['skins'][skin_selected]
    return settings_data, skin_selected, selected_skin_folder


def music_switch_on_off():
    
    settings_data, skin_selected, selected_skin_folder = load_info()
    
    # MUSIC ON --> OFF
    if settings_data['music_on']:
        music.player.stop()
        settings_data['music_on'] = False
        button_music.setIcon(button_image_start)

    # MUSIC OFF --> ON
    else:
        music.audio_output.setVolume(music.volume)
        music.player.play()
        settings_data['music_on'] = True
        button_music.setIcon(button_image_stop)

    save_settings(settings_data)



def time_display():
    
    # CURRENT TIME
    current_time = QTime.currentTime()
    
    # TIMES
    hours_and_mins = current_time.toString('hh:mm')
    seconds = current_time.toString(':ss')
    
    # TOP
    hours_and_mins_display.setText(hours_and_mins)
    seconds_display.setText(seconds)
    
    # BACk - SHADOW
    hours_and_mins_display_2nd.setText(hours_and_mins)
    seconds_display_2nd.setText(seconds)

    # TIME REFRESH - 1000=1sec
    timer.setInterval(1000)


# DIRECTORY AND JSON PATH
working_directory = Path(__file__).parent
path_json = Path(working_directory, 'settings_db_pyqt.json')

# JSON / SETTINGS / SKIN - LOAD INFO
settings_data, skin_selected, selected_skin_folder = load_info()

# MUSIC
music= Music()

# ANIMATION
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

# WINDOW SETTINGS - POSITIONING
window_settings_pos_x_diff = selected_skin_folder['window_settings_pos_x_diff']
window_settings_pos_y_diff = selected_skin_folder['window_settings_pos_y_diff']




''' APP '''
app = QApplication(sys.argv)

# MAIN WINDOW
window = QMainWindow()
window_width, window_height = 720, 486
window.resize(window_width, window_height)
window.setWindowTitle(selected_skin_folder['window_title'])
window.setWindowIcon(QIcon(f'skins/{skin_selected}/icon.ico'))
window.setFixedWidth(window_width)
window.setFixedHeight(window_height)
window.setStyleSheet(
                    "QPushButton"
                        "{"
                        f"background-color : {button_bg_color};"
                        "border-radius: 6px;"          # corner roundness
                        "border: 3px solid black;"
                        "}"
                    "QPushButton::pressed"
                        "{"
                        f"background-color : {button_bg_color_clicked};"
                        "}"
                    )

# MAIN WINDOW POSITION
screen = QApplication.primaryScreen()
screen_rect = screen.availableGeometry()
window_main_pos_x = int((screen_rect.width() - window_width)/2)
window_main_pos_y = int((screen_rect.height() - window_height)/2)
window.move(window_main_pos_x, window_main_pos_y)


# ANIMATION LABEL - before the TIME and BUTTONS
label_animation = QLabel(window)
    

#### TIME
timer = QTimer()
timer.timeout.connect(time_display)
timer.start()

## BACK - SHADOWS
# HOURS:MINUTES
pos_diff = 4
hours_and_mins_display_2nd = QLabel(window)
hours_and_mins_display_2nd.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
hours_and_mins_display_2nd.resize(350, 300)
hours_and_mins_display_2nd.setStyleSheet(f'color: black; font: {time_hm_font_size}pt {time_font_style}; font-weight: bold;')
hours_and_mins_display_2nd.move(time_hm_pos_x+pos_diff, time_hm_pos_y+pos_diff)
# SECONDS
seconds_display_2nd = QLabel(window) 
seconds_display_2nd.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
seconds_display_2nd.resize(350, 300)
seconds_display_2nd.setStyleSheet(f'color:black; font: {time_sec_font_size}pt {time_font_style}; font-weight: bold;')
seconds_display_2nd.move(time_sec_pos_x+pos_diff, time_sec_pos_y+pos_diff)
## TOP
# HOURS:MINUTES
hours_and_mins_display = QLabel(window)
hours_and_mins_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
hours_and_mins_display.resize(350, 300)
hours_and_mins_display.setStyleSheet(f'color:{time_font_color}; font: {time_hm_font_size}pt {time_font_style}; font-weight: bold;')
hours_and_mins_display.move(time_hm_pos_x, time_hm_pos_y)
# SECONDS
seconds_display = QLabel(window) 
seconds_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
seconds_display.resize(350, 300)
seconds_display.setStyleSheet(f'color:{time_font_color}; font: {time_sec_font_size}pt {time_font_style}; font-weight: bold;')
seconds_display.move(time_sec_pos_x, time_sec_pos_y) # background: black;

## BUTTONS
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
button_music.setCursor(Qt.CursorShape.PointingHandCursor)
button_music.clicked.connect(music_switch_on_off)


# BUTTON - SETTING
window_settings = QMainWindow() # configured later
button_image_settings = QIcon('skins/_icons/icon_settings.png')
button_settings = QPushButton(window, text=None, icon=button_image_settings)
button_settings.setIconSize(QSize(20,20))       # icon sizing
button_settings.setGeometry(button_pos_x, button_pos_y, 30, 30)     # pos, pos, size, size
button_settings.setCursor(Qt.CursorShape.PointingHandCursor)
button_settings.clicked.connect(window_settings.show)



# ANIMATION
movie = QMovie(f'skins/{skin_selected}/GIF.GIF')
label_animation.setMovie(movie)
label_animation.resize(720,486)
movie.start()
movie.setSpeed(animation.speed)




'''
SETTINGS WINDOW, TRIGGERED BY THE SETTINGS BUTTON ON MAIN WINDOW
'''
'''
Qt.WindowType:

Sheet: closing the main window --> closing settings window as well
WindowStaysOnTopHint: settings window stays on top
    - even when clicked elsewhere
    - even when the main window get minimized
'''
# window_settings object created in the SETTINGS BUTTON section
window_settings.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Sheet )
window_settings_width, window_settings_height = 250, 200
window_settings.resize(window_settings_width, window_settings_height)
window_settings.setFixedWidth(window_settings_width)
window_settings.setFixedHeight(window_settings_height)
window_settings.setWindowTitle('Settings')
window_settings.setWindowIcon(QIcon(f'skins/icon_settings.ico'))
window_settings.setStyleSheet(
                            "QMainWindow"
                                "{"
                                f"background-color : {button_bg_color};"
                                "border-radius: 10px;"
                                "border: 4px solid black;"
                                "}"

                            "QPushButton"
                                "{"
                                f"background-color : {button_bg_color};"
                                "border-radius: 5px;"          # corner roundness
                                "border: 2px solid black;"
                                "}"

                            "QPushButton::pressed"
                                "{"
                                f"background-color : {button_bg_color_clicked};"
                                "}"

                            "QSlider::handle"
                                "{"
                                f"background-color : 'black';"
                                "}"
                            )


# SETTINGS WINDOW - POSITION
window_settings_pos_x = window_main_pos_x + window_settings_pos_x_diff
window_settings_pos_y = window_main_pos_y + 57 + window_settings_pos_y_diff
window_settings.move(window_settings_pos_x, window_settings_pos_y)



## SETTINGS WINDOW - IMAGES
image_size = 30
pos_x = 20
pos_y = 20
pos_y_diff = image_size + 20
# VOLUME
label_volume = QLabel(window_settings)
image_volume = QPixmap('skins/_icons/icon_volume.png').scaledToWidth(image_size, Qt.TransformationMode.SmoothTransformation)
label_volume.setPixmap(image_volume)
label_volume.resize(image_volume.width(), image_volume.height())
label_volume.move(pos_x, pos_y)
# ANIMATION SPEED
label_animation_speed = QLabel(window_settings)
image_animation_speed = QPixmap('skins/_icons/icon_animation_speed.png').scaledToWidth(image_size, Qt.TransformationMode.SmoothTransformation)
label_animation_speed.setPixmap(image_animation_speed)
label_animation_speed.resize(image_animation_speed.width(), image_animation_speed.height())
label_animation_speed.move(pos_x, pos_y + pos_y_diff)
# SKIN SWITCH
label_skin_switch = QLabel(window_settings)
image_skin_switch = QPixmap('skins/_icons/icon_skin_switch.png').scaledToWidth(image_size+8, Qt.TransformationMode.SmoothTransformation)
label_skin_switch.setPixmap(image_skin_switch)
label_skin_switch.resize(image_skin_switch.width(), image_skin_switch.height())
label_skin_switch.move(pos_x-3, pos_y + pos_y_diff*2)



## SETTINGS WINDOW - SLIDERS
def save_change():
    save_settings(settings_data)

# VOLUME
# music volume [0.0 - 1.0] <-- slider [0 - 100], default pos. change: 10
def change_volume():
    music.audio_output.setVolume(slider_volume.value()/100)
    selected_skin_folder['music_volume'] = slider_volume.value()/100

slider_pos_x = 60
slider_pos_y = 27
slider_volume = QSlider(window_settings)
slider_volume.setGeometry(QtCore.QRect(slider_pos_x, slider_pos_y, 160, 20))
slider_volume.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_volume.setMinimum(0)
slider_volume.setMaximum(100)
slider_volume.setValue(int(music.volume*100))
slider_volume.setCursor(Qt.CursorShape.PointingHandCursor)
slider_volume.valueChanged.connect(change_volume)
slider_volume.sliderReleased.connect(save_change)


# ANIMATION SPEED
def change_animation_speed():
    movie.setSpeed(slider_animation_speed.value())
    selected_skin_folder['animation_speed'] = slider_animation_speed.value()

slider_animation_speed = QSlider(window_settings)
slider_animation_speed.setGeometry(QtCore.QRect(slider_pos_x, slider_pos_y*3 - 5, 160, 20))
slider_animation_speed.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_animation_speed.setMinimum(0)
slider_animation_speed.setMaximum(300)
slider_animation_speed.setValue(animation.speed)
slider_animation_speed.setCursor(Qt.CursorShape.PointingHandCursor)
slider_animation_speed.valueChanged.connect(change_animation_speed)
slider_animation_speed.sliderReleased.connect(save_change)



## SETTINGS WINDOW - SKIN SWITCH - COMBOBOX
def restart():
    QtCore.QCoreApplication.quit()
    QtCore.QProcess.startDetached(sys.executable, sys.argv)


def change_skin():
    
    settings_data, skin_selected, selected_skin_folder = load_info()

    for selected_title in skins_dic:
                
        # SELECTED TITLE(Back to the Future I.) --> FOLDER NAME(back_to_the_future) = skin_selected
        if skins_dic[selected_title]['title'] == combobox_skins.currentText():
            settings_data['skin_selected'] = selected_title
            save_settings(settings_data)
            restart()

# LIST OF MOVIE TITLES
skins_dic = settings_data['skins']
skins_options = []
for _ in skins_dic:
    skins_options.append(settings_data['skins'][_]['title'])

combobox_skins = QComboBox(window_settings)
combobox_skins.addItems(skins_options)
combobox_skins.setCurrentText(skins_dic[skin_selected]['title'])
combobox_skins.setGeometry(slider_pos_x, slider_pos_y*5 - 5, 160, 20)
combobox_skins.currentTextChanged.connect(change_skin)
combobox_skins.setCursor(Qt.CursorShape.PointingHandCursor)




window.show()
if music.on: music.player.play()

sys.exit(app.exec())