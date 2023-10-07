'''
Motion in Time - PyQt6 version

Work in progress
'''

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QSlider, QComboBox
from PyQt6.QtGui import QMovie, QIcon, QPixmap, QFont
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, QTimer, QTime, Qt, QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer

import sys
from pathlib import Path

from MIT import Data, save_settings, load_info, WORKING_DIRECTORY, settings_data, skin_selected, selected_skin_folder 
cv = Data()



class Music:
    def __init__(self):
        self.path_music = Path(WORKING_DIRECTORY, 'skins', skin_selected, 'music.mp3')
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(str(self.path_music)))
        self.player.setLoops(-1) # -1=infinite
        self.audio_output.setVolume(cv.music_volume)




def music_switch_on_off():
    
    settings_data, skin_selected, selected_skin_folder = load_info()
    
    # MUSIC ON --> OFF
    if settings_data['music_on']:
        music.player.stop()
        settings_data['music_on'] = False
        button_music.setIcon(button_image_start)

    # MUSIC OFF --> ON
    else:
        music.audio_output.setVolume(cv.music_volume)
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




# MUSIC
music= Music()


''' APP '''
app = QApplication(sys.argv)

# MAIN WINDOW
window = QMainWindow()
WINDOW_WIDTH, WINDOW_HEIGHT = 720, 486
window.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.setWindowTitle(selected_skin_folder['window_title'])
window.setWindowIcon(QIcon(f'skins/{skin_selected}/icon.ico'))
window.setFixedWidth(WINDOW_WIDTH)
window.setFixedHeight(WINDOW_HEIGHT)
window.setStyleSheet(
                    "QMainWindow"
                        "{"
                        f"background-color : {cv.button_bg_color};"
                        "border-radius: 10px;"
                        "border: 6px solid black;"
                        "}"
                    "QPushButton"
                        "{"
                        f"background-color : {cv.button_bg_color};"
                        "border-radius: 6px;"          # corner roundness
                        "border: 3px solid black;"
                        "}"
                    "QPushButton::pressed"
                        "{"
                        f"background-color : {cv.button_bg_color_clicked};"
                        "}"
                    )

# MAIN WINDOW POSITION
screen = QApplication.primaryScreen()
screen_rect = screen.availableGeometry()
window_main_pos_x = int((screen_rect.width() - WINDOW_WIDTH)/2)
window_main_pos_y = int((screen_rect.height() - WINDOW_HEIGHT)/2)
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
hours_and_mins_display_2nd.setStyleSheet(f'color: black; font: {cv.time_hm_font_size}pt {cv.time_font_style}; font-weight: bold;')
hours_and_mins_display_2nd.move(cv.time_hm_pos_x+pos_diff, cv.time_hm_pos_y+pos_diff)
# SECONDS
seconds_display_2nd = QLabel(window) 
seconds_display_2nd.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
seconds_display_2nd.resize(350, 300)
seconds_display_2nd.setStyleSheet(f'color:black; font: {cv.time_sec_font_size}pt {cv.time_font_style}; font-weight: bold;')
seconds_display_2nd.move(cv.time_sec_pos_x+pos_diff, cv.time_sec_pos_y+pos_diff)
## TOP
# HOURS:MINUTES
hours_and_mins_display = QLabel(window)
hours_and_mins_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
hours_and_mins_display.resize(350, 300)
hours_and_mins_display.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_hm_font_size}pt {cv.time_font_style}; font-weight: bold;')
hours_and_mins_display.move(cv.time_hm_pos_x, cv.time_hm_pos_y)
# SECONDS
seconds_display = QLabel(window) 
seconds_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
seconds_display.resize(350, 300)
seconds_display.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_sec_font_size}pt {cv.time_font_style}; font-weight: bold;')
seconds_display.move(cv.time_sec_pos_x, cv.time_sec_pos_y) # background: black;

## BUTTONS
# BUTTON - MUSIC
button_image_start = QIcon('skins/_icons/icon_start.png')
button_image_stop = QIcon('skins/_icons/icon_stop.png')

if cv.music_on:
        music_start_stop_img = button_image_stop
else:
    music_start_stop_img = button_image_start

pos_y_diff = 33
button_music = QPushButton(window, text=None, icon=music_start_stop_img)
button_music.setIconSize(QSize(20,20))
button_music.setGeometry(cv.button_pos_x, cv.button_pos_y+pos_y_diff, 29, 29)     # pos, pos, size, size
button_music.setCursor(Qt.CursorShape.PointingHandCursor)
button_music.clicked.connect(music_switch_on_off)


# BUTTON - SETTING
window_settings = QMainWindow()
# window_settings configured later
# (window) --> SETTINGS WINDOW default launch in center of the main window
button_image_settings = QIcon('skins/_icons/icon_settings.png')
button_settings = QPushButton(window, text=None, icon=button_image_settings)
button_settings.setIconSize(QSize(20,20))       # icon sizing
button_settings.setGeometry(cv.button_pos_x, cv.button_pos_y, 30, 30)     # pos, pos, size, size
button_settings.setCursor(Qt.CursorShape.PointingHandCursor)
button_settings.clicked.connect(window_settings.show)



# ANIMATION
movie = QMovie(f'skins/{skin_selected}/GIF.GIF')
label_animation.setMovie(movie)
label_animation.resize(720,486)
movie.start()
movie.setSpeed(cv.animation_speed)




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
window_settings.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Sheet)
WINDOW_SETTINGS_WIDTH, WINDOW_SETTINGS_HEIGHT = 250, 223
window_settings.resize(WINDOW_SETTINGS_WIDTH, WINDOW_SETTINGS_HEIGHT)
window_settings.setFixedWidth(WINDOW_SETTINGS_WIDTH)
window_settings.setFixedHeight(WINDOW_SETTINGS_HEIGHT)
window_settings.setWindowTitle('Settings')
window_settings.setWindowIcon(QIcon(f'skins/icon_settings.ico'))
window_settings.setStyleSheet(
                            "QMainWindow"
                                "{"
                                f"background-color : {cv.button_bg_color};"
                                "border-radius: 10px;"
                                "border: 4px solid black;"
                                "}"

                            "QPushButton"
                                "{"
                                f"background-color : {cv.button_bg_color};"
                                "border-radius: 5px;"          # corner roundness
                                "border: 2px solid black;"
                                "}"

                            "QPushButton::pressed"
                                "{"
                                f"background-color : {cv.button_bg_color_clicked};"
                                "}"

                            "QSlider::handle"
                                "{"
                                f"background-color : 'black';"
                                "}"
                            )


# SETTINGS WINDOW - POSITION
window_settings_pos_x = window_main_pos_x + cv.window_settings_pos_x_diff
window_settings_pos_y = window_main_pos_y + 57 + cv.window_settings_pos_y_diff
window_settings.move(window_settings_pos_x, window_settings_pos_y)



## SETTINGS WINDOW - IMAGES AND TEXT
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
# A - ADVANCED
label_A = QLabel(window_settings, text='A')
label_A.move(pos_x+3, pos_y + pos_y_diff*3)
label_A.setFont(QFont('Times', 30, 800))   # style, size, bold


## SETTINGS WINDOW - SLIDERS
# In this scale we can use only one function to save
# the two parameters together at the same/every time
# if one of them is changed - pros/kons
def save_volume():
    settings_data, skin_selected, selected_skin_folder = load_info()
    selected_skin_folder['music_volume'] = slider_volume.value()/100
    save_settings(settings_data)

def save_animation_speed():
    settings_data, skin_selected, selected_skin_folder = load_info()
    selected_skin_folder['animation_speed'] = slider_animation_speed.value()
    save_settings(settings_data)

# VOLUME
# music volume [0.0 - 1.0] <-- slider [0 - 100], default pos. change: 10
def change_volume():
    music.audio_output.setVolume(slider_volume.value()/100)
    

slider_pos_x = 60
slider_pos_y = 27
slider_volume = QSlider(window_settings)
slider_volume.setGeometry(QtCore.QRect(slider_pos_x, slider_pos_y, 160, 20))
slider_volume.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_volume.setMinimum(0)
slider_volume.setMaximum(100)
slider_volume.setValue(int(cv.music_volume*100))
slider_volume.setCursor(Qt.CursorShape.PointingHandCursor)
slider_volume.valueChanged.connect(change_volume)
slider_volume.sliderReleased.connect(save_volume)


# ANIMATION SPEED
def change_animation_speed():
    movie.setSpeed(slider_animation_speed.value())


slider_animation_speed = QSlider(window_settings)
slider_animation_speed.setGeometry(QtCore.QRect(slider_pos_x, slider_pos_y*3 - 5, 160, 20))
slider_animation_speed.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_animation_speed.setMinimum(0)
slider_animation_speed.setMaximum(300)
slider_animation_speed.setValue(cv.animation_speed)
slider_animation_speed.setCursor(Qt.CursorShape.PointingHandCursor)
slider_animation_speed.valueChanged.connect(change_animation_speed)
slider_animation_speed.sliderReleased.connect(save_animation_speed)



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
combobox_skins.setFont(QFont('Times', 10))

## SETTINGS WINDOW - ADVANCED BUTTON
def button_advanced_launch():
    window_settings.hide()
    for size_incr in range(0, WINDOW_SETTINGS_WIDTH, 2):
        window.setFixedWidth(WINDOW_WIDTH + size_incr)

button_advanced = QPushButton(window_settings, text='ADVANCED')
button_advanced.setGeometry(slider_pos_x, slider_pos_y*6 + 12, 160, 25)
button_advanced.setCursor(Qt.CursorShape.PointingHandCursor)
button_advanced.clicked.connect(button_advanced_launch)
button_advanced.setFont(QFont('Times', 11, 600))


window.show()
if cv.music_on: music.player.play()

sys.exit(app.exec())