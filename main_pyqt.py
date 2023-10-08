'''

Motion in Time - PyQt6 version

Work in progress

'''

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QSlider
from PyQt6.QtGui import QMovie, QIcon, QFont
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, QTimer, QTime, Qt, QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer

import sys
from pathlib import Path

from MIT import Data, MyImage, MySlider, MyComboBoxSkins, MyComboBoxWidgetUpdate
from MIT import save_settings, load_info, WORKING_DIRECTORY, skin_selected, selected_skin_folder 
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

'''
########################################
              MAIN WINDOW                                      
########################################
'''
window_main = QMainWindow()
WINDOW_WIDTH, WINDOW_HEIGHT = 720, 486
window_main.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
window_main.setWindowTitle(selected_skin_folder['window_title'])
window_main.setWindowIcon(QIcon(f'skins/{skin_selected}/icon.ico'))
window_main.setFixedWidth(WINDOW_WIDTH)
window_main.setFixedHeight(WINDOW_HEIGHT)
window_main.setStyleSheet(
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
                    "QSlider::handle"
                        "{"
                        f"background-color : 'black';"
                        "}"
                    )

# MAIN WINDOW POSITION
SCREEN = QApplication.primaryScreen()
SCREEN_RECT = SCREEN.availableGeometry()
WINDOW_MAIN_POS_X = int((SCREEN_RECT.width() - WINDOW_WIDTH)/2)
WINDOW_MAIN_POS_Y = int((SCREEN_RECT.height() - WINDOW_HEIGHT)/2)
window_main.move(WINDOW_MAIN_POS_X, WINDOW_MAIN_POS_Y)

# ANIMATION LABEL - before the TIME and BUTTONS
label_animation = QLabel(window_main)
    

#### TIME
timer = QTimer()
timer.timeout.connect(time_display)
timer.start()

## BACK - SHADOWS
# HOURS:MINUTES
pos_diff = 4
hours_and_mins_display_2nd = QLabel(window_main)
hours_and_mins_display_2nd.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
hours_and_mins_display_2nd.resize(350, 300)
hours_and_mins_display_2nd.setStyleSheet(f'color: black; font: {cv.time_hm_font_size}pt {cv.time_font_style}; font-weight: bold;')
hours_and_mins_display_2nd.move(cv.time_hm_pos_x+pos_diff, cv.time_hm_pos_y+pos_diff)
# SECONDS
seconds_display_2nd = QLabel(window_main) 
seconds_display_2nd.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
seconds_display_2nd.resize(350, 300)
seconds_display_2nd.setStyleSheet(f'color:black; font: {cv.time_sec_font_size}pt {cv.time_font_style}; font-weight: bold;')
seconds_display_2nd.move(cv.time_sec_pos_x+pos_diff, cv.time_sec_pos_y+pos_diff)
## TOP
# HOURS:MINUTES
hours_and_mins_display = QLabel(window_main)
hours_and_mins_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
hours_and_mins_display.resize(350, 300)
hours_and_mins_display.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_hm_font_size}pt {cv.time_font_style}; font-weight: bold;')
hours_and_mins_display.move(cv.time_hm_pos_x, cv.time_hm_pos_y)
# SECONDS
seconds_display = QLabel(window_main) 
seconds_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
seconds_display.resize(350, 300)
seconds_display.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_sec_font_size}pt {cv.time_font_style}; font-weight: bold;')
seconds_display.move(cv.time_sec_pos_x, cv.time_sec_pos_y) # background: black;

## BUTTONS
# BUTTON - MUSIC
button_image_start = QIcon('skins/_images/start.png')
button_image_stop = QIcon('skins/_images/stop.png')

if cv.music_on:
        music_start_stop_img = button_image_stop
else:
    music_start_stop_img = button_image_start

pos_y_diff = 33
button_music = QPushButton(window_main, text=None, icon=music_start_stop_img)
button_music.setIconSize(QSize(20,20))
button_music.setGeometry(cv.button_pos_x, cv.button_pos_y+pos_y_diff, 29, 29)     # pos, pos, size, size
button_music.setCursor(Qt.CursorShape.PointingHandCursor)
button_music.clicked.connect(music_switch_on_off)


# BUTTON - SETTING
window_settings = QMainWindow()
# window_settings configured later
# (window) --> SETTINGS WINDOW default launch in center of the main window
button_image_settings = QIcon('skins/_images/settings.png')
button_settings = QPushButton(window_main, text=None, icon=button_image_settings)
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
########################################
            SETTINGS WINDOW                
########################################
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
window_settings.setWindowIcon(QIcon(f'skins/_images/window_settings.ico'))
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
window_settings_pos_x = WINDOW_MAIN_POS_X + cv.window_settings_pos_x_diff
window_settings_pos_y = WINDOW_MAIN_POS_Y + 57 + cv.window_settings_pos_y_diff
window_settings.move(window_settings_pos_x, window_settings_pos_y)



## SETTINGS WINDOW - IMAGES AND TEXT
image_size = 30
pos_x = 20
pos_y = 20
pos_y_diff = image_size + 20

# VOLUME
MyImage(window_settings, 'volume.png', image_size, pos_x, pos_y)

# ANIMATION SPEED
MyImage(window_settings, 'animation_speed.png', image_size, pos_x, pos_y+pos_y_diff)

# SKIN SWITCH
MyImage(window_settings, 'skin_switch.png', image_size+8, pos_x-3, pos_y+pos_y_diff*2-3)

# A - ADVANCED
label_A = QLabel(window_settings, text='A')
label_A.move(pos_x+3, pos_y + pos_y_diff*3)
# label_A.resize(30,30)
label_A.setFont(QFont('Times', 30, 800))   # style, size, bold


## SETTINGS WINDOW - SLIDERS
slider_pos_x = 60
slider_pos_y = 27


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
    
slider_volume = MySlider(
    window_settings,
    min=0,
    max=100,
    setValue=int(cv.music_volume*100),
    valueChanged=change_volume,
    sliderReleased=save_volume,
    pos_x=slider_pos_x,
    pos_y=slider_pos_y)



# ANIMATION SPEED
def change_animation_speed():
    movie.setSpeed(slider_animation_speed.value())

slider_animation_speed = MySlider(
    window_settings,
    min=0,
    max=300,
    setValue=cv.animation_speed,
    valueChanged=change_animation_speed,
    sliderReleased=save_animation_speed,
    pos_x=slider_pos_x,
    pos_y=slider_pos_y*3 - 5)




## SETTINGS WINDOW - SKIN SWITCH - COMBOBOX
MyComboBoxSkins(window_settings, slider_pos_x, slider_pos_y*5 - 9)



## SETTINGS WINDOW - ADVANCED BUTTON
def button_advanced_launch():
    window_settings.hide()
    button_settings.setEnabled(False)
    for size_incr in range(0, WINDOW_SETTINGS_WIDTH, 2):
        window_main.setFixedWidth(WINDOW_WIDTH + size_incr)
    
button_advanced = QPushButton(window_settings, text='ADVANCED')
button_advanced.setGeometry(slider_pos_x, slider_pos_y*6 + 12, 160, 25)
button_advanced.setCursor(Qt.CursorShape.PointingHandCursor)
button_advanced.clicked.connect(button_advanced_launch)
button_advanced.setFont(QFont('Times', 11, 600))


'''
########################################
        ADVANCED SETTINGS WINDOW                
########################################
'''

''' IMAGES AND TEXT '''
image_size = 30
adv_img_pos_x = WINDOW_WIDTH + 15
adv_img_pos_y = 20
adv_img_pos_y_diff = image_size + 20

# SKIN SWITCH
MyImage(window_main, 'skin_switch.png', image_size+8, adv_img_pos_x, adv_img_pos_y)

# SETTINGS
MyImage(window_main, 'settings.png', image_size, adv_img_pos_x, adv_img_pos_y+adv_img_pos_y_diff)

# X
label_X = QLabel(window_main, text='X')
label_X.move(adv_img_pos_x, adv_img_pos_y+adv_img_pos_y_diff*2)
label_X.setFont(QFont('Times', 28, 800))   # style, size, bold

# X
label_X = QLabel(window_main, text='Y')
label_X.move(adv_img_pos_x, adv_img_pos_y+adv_img_pos_y_diff*3)
label_X.setFont(QFont('Times', 28, 800)) 



''' WIDGETS '''
adv_non_img_pos_x = adv_img_pos_x + 40
adv_non_img_pos_y = 30
adv_non_img_pos_y_diff = 50

### COMBOBOX
## SKIN SWITCH - COMBOBOX
MyComboBoxSkins(window_main, adv_non_img_pos_x, adv_non_img_pos_y)


## WIDGETS UPDATE - COMBOBOX
widget_dic = {
            'Play/Stop button': button_music,
            'Settings button': button_settings,
            'Settings window': window_settings,
            'HRS:MINS': hours_and_mins_display,
            'HRS:MINS - Shadow': hours_and_mins_display_2nd,
            'SEC': seconds_display,
            'SEC - Shadow': seconds_display_2nd
            }

widget_list = list(widget_dic.keys())

def selected_widget_action():
    if widget_dic[selected_widgets.currentText()] == window_settings:
        window_settings.setEnabled(False)
        window_settings.show()
        slider_pos_x.setMaximum(SCREEN_RECT.width() - WINDOW_SETTINGS_WIDTH)
        slider_pos_y.setMaximum(SCREEN_RECT.height() - WINDOW_SETTINGS_HEIGHT)
    else:
        window_settings.hide()
        slider_pos_x.setMaximum(WINDOW_WIDTH - 30)
        slider_pos_y.setMaximum(WINDOW_HEIGHT - 30) 


selected_widgets = MyComboBoxWidgetUpdate(
                                    window_main,
                                    widget_list,
                                    selected_widget_action,
                                    adv_non_img_pos_x,
                                    adv_non_img_pos_y+adv_non_img_pos_y_diff
                                    )



### SLIDERS
adv_slider_pos_x = adv_img_pos_x + 15

## X - SLIDER
def update_xy():
    for title in widget_dic:
        if title == selected_widgets.currentText():   #  Play/Stop button 
            widget_dic[title].move(slider_pos_x.value(), slider_pos_y.value())
            

slider_pos_x = QSlider(window_main)
slider_pos_x.setGeometry(QtCore.QRect(adv_non_img_pos_x, adv_non_img_pos_y + adv_non_img_pos_y_diff*2, 160, 20))
slider_pos_x.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_pos_x.setMinimum(0)
slider_pos_x.setMaximum(WINDOW_WIDTH - 30)
# slider_pos_x.setValue(cv.animation_speed)
slider_pos_x.setCursor(Qt.CursorShape.PointingHandCursor)
slider_pos_x.valueChanged.connect(update_xy)
# slider_pos_x.sliderReleased.connect(save_animation_speed)


## Y - SLIDER
slider_pos_y = QSlider(window_main)
slider_pos_y.setGeometry(QtCore.QRect(adv_non_img_pos_x, adv_non_img_pos_y + adv_non_img_pos_y_diff*3, 160, 20))
slider_pos_y.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_pos_y.setMinimum(0)
slider_pos_y.setMaximum(WINDOW_HEIGHT - 30)
# slider_pos_y.setValue(cv.animation_speed)
slider_pos_y.setCursor(Qt.CursorShape.PointingHandCursor)
slider_pos_y.valueChanged.connect(update_xy)
# slider_pos_y.sliderReleased.connect(save_animation_speed)






window_main.show()
if cv.music_on: music.player.play()

sys.exit(app.exec())