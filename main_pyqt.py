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

from MIT import Data, MyImage, MySlider
from MIT import MyComboBoxSkins, MyComboBoxWidgetUpdate, MyComboBoxFont
from MIT import save_settings, load_info
from MIT import WORKING_DIRECTORY, settings_data, skin_selected, selected_skin_folder 
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
    hours_and_mins_time = current_time.toString('hh:mm')
    seconds_time = current_time.toString(':ss')
    
    # TOP
    hours_and_mins.setText(hours_and_mins_time)
    hours_and_mins.adjustSize()
    seconds.setText(seconds_time)
    seconds.adjustSize()
    
    # BACk - SHADOW
    hours_and_mins_shadow.setText(hours_and_mins_time)
    hours_and_mins_shadow.adjustSize()
    seconds_shadow.setText(seconds_time)
    seconds_shadow.adjustSize()

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
                        # "border: 6px solid black;"
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
if SCREEN_RECT.width() < cv.window_main_pos_x or SCREEN_RECT.height() < cv.window_main_pos_y:
    WINDOW_MAIN_POS_X = int((SCREEN_RECT.width() - WINDOW_WIDTH)/2)
    WINDOW_MAIN_POS_Y = int((SCREEN_RECT.height() - WINDOW_HEIGHT)/2)
    window_main.move(WINDOW_MAIN_POS_X, WINDOW_MAIN_POS_Y)
    ''' error message needed - window pos saving needed'''
else:
    window_main.move(cv.window_main_pos_x, cv.window_main_pos_y)

# ANIMATION LABEL - before the TIME and BUTTONS
label_animation = QLabel(window_main)
    

#### TIME
timer = QTimer()
timer.timeout.connect(time_display)
timer.start()

## BACK - SHADOWS
# HOURS:MINUTES
hours_and_mins_shadow = QLabel(window_main)
hours_and_mins_shadow.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
hours_and_mins_shadow.setStyleSheet(f'color: black; font: {cv.time_hm_shad_font_size}pt {cv.time_font_style}; font-weight: bold;')
hours_and_mins_shadow.move(cv.time_hm_shadow_pos_x, cv.time_hm_shadow_pos_y)
# SECONDS
seconds_shadow = QLabel(window_main) 
seconds_shadow.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
seconds_shadow.setStyleSheet(f'color:black; font: {cv.time_sec_shad_font_size}pt {cv.time_font_style}; font-weight: bold;')
seconds_shadow.move(cv.time_sec_shadow_pos_x, cv.time_sec_shadow_pos_y)
## TOP
# HOURS:MINUTES
hours_and_mins = QLabel(window_main)
hours_and_mins.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
hours_and_mins.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_hm_font_size}pt {cv.time_font_style}; font-weight: bold;')
hours_and_mins.move(cv.time_hm_pos_x, cv.time_hm_pos_y)

# SECONDS
seconds = QLabel(window_main) 
seconds.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
seconds.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_sec_font_size}pt {cv.time_font_style}; font-weight: bold;')
seconds.move(cv.time_sec_pos_x, cv.time_sec_pos_y) # background: black;

## BUTTONS
# BUTTON - MUSIC
button_image_start = QIcon('skins/_images/start.png')
button_image_stop = QIcon('skins/_images/stop.png')

if cv.music_on:
        music_start_stop_img = button_image_stop
else:
    music_start_stop_img = button_image_start


button_music = QPushButton(window_main, text=None, icon=music_start_stop_img)
button_music.setIconSize(QSize(20,20))
button_music.setGeometry(cv.button_music_pos_x, cv.button_music_pos_y, 29, 29)     # pos, pos, size, size
button_music.setCursor(Qt.CursorShape.PointingHandCursor)
button_music.clicked.connect(music_switch_on_off)


# BUTTON - SETTING
window_settings = QMainWindow()
# window_settings configured later
# (window) --> SETTINGS WINDOW default launch in center of the main window
button_image_settings = QIcon('skins/_images/settings.png')
button_settings = QPushButton(window_main, text=None, icon=button_image_settings)
button_settings.setIconSize(QSize(20,20))       # icon sizing
button_settings.setGeometry(cv.button_settings_pos_x, cv.button_settings_pos_y, 30, 30)     # pos, pos, size, size
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
########################################

            SETTINGS WINDOW         

########################################
########################################
'''
'''
Qt.WindowType:

Sheet: closing the main window --> closing settings window as well
WindowStaysOnTopHint: settings window stays on top
    - even when clicked elsewhere
    - even when the main window get minimized
'''
SETT_WIDGETS_WIDTH = 160
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
window_settings.move(cv.window_settings_pos_x, cv.window_settings_pos_y)



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
label_A.setStyleSheet("color:'black';font: 30pt 'Times'; font-weight: bold;")
# another solution, no color info: label_A.setFont(QFont('Times', 30, 800))   # style, size, bold


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
    width=SETT_WIDGETS_WIDTH,
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
    width=SETT_WIDGETS_WIDTH,
    pos_x=slider_pos_x,
    pos_y=slider_pos_y*3 - 5)



## SETTINGS WINDOW - SKIN SWITCH - COMBOBOX
MyComboBoxSkins(window_settings, SETT_WIDGETS_WIDTH, False, slider_pos_x, slider_pos_y*5 - 9)



## SETTINGS WINDOW - ADVANCED BUTTON
def button_advanced_launch():
    window_settings.hide()
    button_settings.setEnabled(False)
    for size_incr in range(0, WINDOW_ADVANCED_ADD_WIDTH, 2):
        window_main.setFixedWidth(WINDOW_WIDTH + size_incr)
    
button_advanced = QPushButton(window_settings, text='ADVANCED')
button_advanced.setGeometry(slider_pos_x, slider_pos_y*6 + 12, 160, 25)
button_advanced.setCursor(Qt.CursorShape.PointingHandCursor)
button_advanced.clicked.connect(button_advanced_launch)
button_advanced.setFont(QFont('Times', 11, 600))


'''
########################################
########################################

        ADVANCED SETTINGS WINDOW*       

########################################
########################################
* still in main       
'''
WINDOW_ADVANCED_ADD_WIDTH = 300
WINDOW_ADVANCED_WIDTH = WINDOW_WIDTH + WINDOW_ADVANCED_ADD_WIDTH
ADV_WIDGETS_WIDTH = 200

def butt_and_win_settings_enable(value):
    window_settings.setEnabled(value)
    button_settings.setEnabled(value)
    if value:
        label_A.setStyleSheet("color:'black';font: 30pt 'Times'; font-weight: bold;")
    else:
        label_A.setStyleSheet("color:'#5E5E5D';font: 30pt 'Times'; font-weight: bold;")

''' 
#######################
    IMAGES AND TEXT      
#######################
'''
image_size = 30
adv_img_pos_x = WINDOW_WIDTH + 15
adv_img_pos_y = 20
adv_img_pos_y_diff = image_size + 20

# SKIN SWITCH
MyImage(window_main, 'skin_switch.png', image_size+8, adv_img_pos_x, adv_img_pos_y)

# SETTINGS
MyImage(window_main, 'settings.png', image_size, adv_img_pos_x, adv_img_pos_y+adv_img_pos_y_diff)

## LABELS
font_size = 28
# X
label_X = QLabel(window_main, text='X')
label_X.move(adv_img_pos_x, adv_img_pos_y+adv_img_pos_y_diff*2)
label_X.setFont(QFont('Times', font_size, 800))   # style, size, bold

# Y
label_Y = QLabel(window_main, text='Y')
label_Y.move(adv_img_pos_x, adv_img_pos_y+adv_img_pos_y_diff*3)
label_Y.setFont(QFont('Times', font_size, 800)) 

# S
label_S = QLabel(window_main, text='S')
label_S.move(adv_img_pos_x, adv_img_pos_y+adv_img_pos_y_diff*4)
label_S.setFont(QFont('Times', font_size, 800))
label_S.hide() 



'''
#########################
    COMBOBOXES - ADV               
#########################
'''
adv_non_img_pos_x = adv_img_pos_x + 40
adv_non_img_pos_y = 30
adv_non_img_pos_y_diff = 50


''' SKIN SWITCH - COMBOBOX - ADV '''
# RELAUNCHING THE ADVENCED SETTINGS "WINDOW"
# AFTER ADVANCED SKIN SWITCH
if settings_data['is_skin_switch_advanced']:
    window_main.setFixedWidth(WINDOW_WIDTH+WINDOW_ADVANCED_ADD_WIDTH)
    butt_and_win_settings_enable(False)
    settings_data['is_skin_switch_advanced'] = False
    save_settings(settings_data)

MyComboBoxSkins(window_main, ADV_WIDGETS_WIDTH, True, adv_non_img_pos_x, adv_non_img_pos_y)

''' WIDGETS UPDATE - COMBOBOX - ADV '''
widget_dic = {
            'Button: Settings': {
                "widget": button_settings,
                "name": "button_settings",
                "x": cv.button_settings_pos_x,
                "y": cv.button_settings_pos_y,
                },
            'Button: Play/Stop': {
                "widget": button_music,
                "name": "button_music",
                "x": cv.button_music_pos_x,
                "y": cv.button_music_pos_y
                },
            'Window: Main': {
                "widget": window_main,
                "name": "window_main",
                "x": cv.window_main_pos_x,
                "y": cv.window_main_pos_y
                },
            'Window: Settings ': {
                "widget": window_settings,
                "name": "window_settings",
                "x": cv.window_settings_pos_x,
                "y": cv.window_settings_pos_y
                },
            'Time: HRS:MINS': {
                "widget": hours_and_mins,
                "name": "hours_and_mins",
                "x": cv.time_hm_pos_x,
                "y": cv.time_hm_pos_y,
                "size": cv.time_hm_font_size,
                "color": cv.time_font_color,
                "style": cv.time_font_style
                },
            'Time: HRS:MINS - Shadow': {
                "widget": hours_and_mins_shadow,
                "name": "hours_and_mins_shadow",
                "x": cv.time_hm_shadow_pos_x,
                "y": cv.time_hm_shadow_pos_y,
                "size": cv.time_hm_shad_font_size,
                "color": 'black'
                },
            'Time: SEC': {
                "widget": seconds,
                "name": "seconds",
                "x": cv.time_sec_pos_x,
                "y": cv.time_sec_pos_y,
                "size": cv.time_sec_font_size,
                "color": cv.time_font_color
                },
            'Time: SEC - Shadow':  {
                "widget": seconds_shadow,
                "name": "seconds_shadow",
                "x": cv.time_sec_shadow_pos_x,
                "y": cv.time_sec_shadow_pos_y,
                "size": cv.time_sec_shad_font_size,
                "color": 'black'
                }
            }

widget_list = list(widget_dic.keys())

def selected_widget_action():

    # NO SLIDER UPDATE AFTER WIDGET SELECTION COMBOBOX CHANGE
    cv.selected_widg_changed = True

    selected_widget = select_widget_cb.currentText()

    ## ADJUSTING THE SLIDERS` MIN, MAX
    # WINDOW MAIN
    if selected_widget == widget_list[2]:
        slider_pos_x.setMaximum(SCREEN_RECT.width() - WINDOW_ADVANCED_WIDTH)
        slider_pos_y.setMaximum(SCREEN_RECT.height() - WINDOW_HEIGHT)

        slider_pos_x.setOrientation(QtCore.Qt.Orientation.Vertical)
        slider_pos_x.setGeometry(QtCore.QRect(WINDOW_ADVANCED_WIDTH - 30,
                                              30,
                                              20,
                                              ADV_WIDGETS_WIDTH))
        label_X.move(WINDOW_ADVANCED_WIDTH - 60, adv_img_pos_y+adv_img_pos_y_diff*2)
    
    if selected_widget != widget_list[2]:
        slider_pos_x.setOrientation(QtCore.Qt.Orientation.Horizontal)
        slider_pos_x.setGeometry(QtCore.QRect(adv_non_img_pos_x,
                                              adv_non_img_pos_y + adv_non_img_pos_y_diff*2,
                                              ADV_WIDGETS_WIDTH,
                                              20))
        label_X.move(adv_img_pos_x, adv_img_pos_y+adv_img_pos_y_diff*2)
    
    # WINDOW SETTINGS
    if selected_widget == widget_list[3]:
        butt_and_win_settings_enable(False)
        window_settings.show()
        slider_pos_x.setMaximum(SCREEN_RECT.width() - WINDOW_SETTINGS_WIDTH)
        slider_pos_y.setMaximum(SCREEN_RECT.height() - WINDOW_SETTINGS_HEIGHT + 8)

    if selected_widget != widget_list[3]:
        window_settings.hide()
    
    # NOT MAIN, SETTING WINDOW
    if selected_widget in [widget_list[0], widget_list[1]]:
        slider_pos_x.setMaximum(WINDOW_WIDTH - 30)
        slider_pos_y.setMaximum(WINDOW_HEIGHT - 30)
    
    ## TIME
    if selected_widget in widget_list[4:8]:
        slider_time_size.setValue(widget_dic[selected_widget]['size'])
        slider_time_size.show()
        label_S.show()
        slider_pos_x.setMaximum(WINDOW_WIDTH - widget_dic[selected_widget]['widget'].size().width())
        slider_pos_y.setMaximum(WINDOW_HEIGHT - widget_dic[selected_widget]['widget'].size().height())
    
    if selected_widget not in widget_list[4:8]:
        slider_time_size.hide()
        label_S.hide()

    # MOVE THE HANDLE TO THE LATEST POSITION
    # HAS TO BE AFTER THE SLIDER RANGE ADJUSTMENT
    slider_pos_x.setValue(widget_dic[selected_widget]['x'])
    slider_pos_y.setValue(widget_dic[selected_widget]['y']) 

    cv.selected_widg_changed = False


select_widget_cb = MyComboBoxWidgetUpdate(
                                        window_main,
                                        widget_list,
                                        selected_widget_action,
                                        ADV_WIDGETS_WIDTH,
                                        adv_non_img_pos_x,
                                        adv_non_img_pos_y+adv_non_img_pos_y_diff
                                        )

''' FONT UPDATE - COMBOBOX '''
def selected_font_action():

    cv.time_font_style = select_font_cb.currentText()
    widget_dic[widget_list[4]]['style'] = select_font_cb.currentText()
    
    hours_and_mins.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_hm_font_size}pt {cv.time_font_style}; font-weight: bold;')
    hours_and_mins_shadow.setStyleSheet(f'color: black; font: {cv.time_hm_font_size}pt {cv.time_font_style}; font-weight: bold;')
    seconds.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_sec_font_size}pt {cv.time_font_style}; font-weight: bold;')
    seconds_shadow.setStyleSheet(f'color:black; font: {cv.time_sec_font_size}pt {cv.time_font_style}; font-weight: bold;')

    for item in widget_list[4:8]:
        widget_dic[item]['widget'].adjustSize()


select_font_cb = MyComboBoxFont(
                                window_main,
                                selected_font_action,
                                ADV_WIDGETS_WIDTH,
                                adv_non_img_pos_x,
                                adv_non_img_pos_y+adv_non_img_pos_y_diff*5
                                )



'''
#####################
    SLIDERS - ADV
#####################
'''
adv_slider_pos_x = adv_img_pos_x + 15

''' X - SLIDER '''
def update_xy():
    # NO SLIDER UPDATE AFTER WIDGET SELECTION COMBOBOX CHANGE
    if not cv.selected_widg_changed:
        selected_widget = select_widget_cb.currentText()
        widget_dic[selected_widget]['widget'].move(slider_pos_x.value(), slider_pos_y.value())
        widget_dic[selected_widget]['x'] = slider_pos_x.value()
        widget_dic[selected_widget]['y'] = slider_pos_y.value()


slider_pos_x = QSlider(window_main)
slider_pos_x.setGeometry(QtCore.QRect(adv_non_img_pos_x, adv_non_img_pos_y + adv_non_img_pos_y_diff*2, ADV_WIDGETS_WIDTH, 20))
slider_pos_x.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_pos_x.setMinimum(0)
slider_pos_x.setMaximum(WINDOW_WIDTH - 30)
slider_pos_x.setValue(cv.button_settings_pos_x)
slider_pos_x.setCursor(Qt.CursorShape.PointingHandCursor)
slider_pos_x.valueChanged.connect(update_xy)


''' Y - SLIDER '''
slider_pos_y = QSlider(window_main)
slider_pos_y.setGeometry(QtCore.QRect(adv_non_img_pos_x, adv_non_img_pos_y + adv_non_img_pos_y_diff*3, ADV_WIDGETS_WIDTH, 20))
slider_pos_y.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_pos_y.setMinimum(0)
slider_pos_y.setMaximum(WINDOW_HEIGHT - 30)
slider_pos_y.setValue(cv.button_settings_pos_y)
slider_pos_y.setCursor(Qt.CursorShape.PointingHandCursor)
slider_pos_y.valueChanged.connect(update_xy)


''' S - SLIDER '''
def update_size():
    
    if not cv.selected_widg_changed:

        selected_widget = select_widget_cb.currentText()
        
        if selected_widget in widget_list[4:8]:
            
            widget_dic[selected_widget]['widget'].setStyleSheet(
                f"color:{widget_dic[selected_widget]['color']};font: {slider_time_size.value()}pt {cv.time_font_style}; font-weight: bold;")
        
            # SLIDER --> VARIABLE
            widget_dic[selected_widget]['size'] = slider_time_size.value()
            
            # RESIZE TEXT LABEL
            widget_dic[selected_widget]['widget'].adjustSize()

            # AVAILABLE POSITION UPDATE
            slider_pos_x.setMaximum(WINDOW_WIDTH - widget_dic[selected_widget]['widget'].size().width())
            slider_pos_y.setMaximum(WINDOW_HEIGHT - widget_dic[selected_widget]['widget'].size().height())


slider_time_size = QSlider(window_main)
slider_time_size.setGeometry(QtCore.QRect(adv_non_img_pos_x, adv_non_img_pos_y + adv_non_img_pos_y_diff*4, ADV_WIDGETS_WIDTH, 20))
slider_time_size.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_time_size.setMinimum(20)
slider_time_size.setMaximum(100)
slider_time_size.setValue(cv.button_settings_pos_y)
slider_time_size.setCursor(Qt.CursorShape.PointingHandCursor)
slider_time_size.valueChanged.connect(update_size)
slider_time_size.hide()

'''
#######################
    BUTTONS - ADV   
#######################
'''
''' BUTTON - CLOSE - ADV '''
def close_advanced_window():

    butt_and_win_settings_enable(True)

    for size_decr in range(0, WINDOW_ADVANCED_ADD_WIDTH+2, 2):
        window_main.setFixedWidth(WINDOW_ADVANCED_WIDTH - size_decr)


button_image_close = QIcon('skins/_images/close.png')
button_close = QPushButton(window_main, text=None, icon=button_image_close)
button_close.setIconSize(QSize(15,15))
button_close.setGeometry(WINDOW_ADVANCED_WIDTH-32, 12, 20, 20)     # pos, pos, size, size
button_close.setCursor(Qt.CursorShape.PointingHandCursor)
button_close.clicked.connect(close_advanced_window)


# ''' BUTTON - SAVE - ADV '''
def save_advanced_settings():
    
    settings_data, skin_selected, selected_skin_folder = load_info()

    for index, item in enumerate(widget_list):
        
        widget_name = widget_dic[item]['name']
        
        # BUTTONS(MUSIC, SETTINGS), TIMES
        if index not in [2, 3]:      # no window main
                    
            for var_name in selected_skin_folder['json_widg_params'][widget_name]:
                selected_skin_folder['json_widg_params'][widget_name][var_name] = widget_dic[item][var_name]

        # MAIN AND SETTINGS WINDOW
        if index in [2, 3]:
             for var_name in settings_data[widget_name]:
                settings_data[widget_name][var_name] = widget_dic[item][var_name]


    # BUTTONS COLOR
    selected_skin_folder['button_bg_color'] = cv.button_bg_color
    selected_skin_folder['button_bg_color_clicked'] = cv.button_bg_color_clicked

    save_settings(settings_data)


button_save_adv_sett = QPushButton(window_main, text='SAVE SETTINGS')
button_save_adv_sett.setGeometry(
    adv_non_img_pos_x,
    adv_non_img_pos_y + adv_non_img_pos_y_diff *6,
    ADV_WIDGETS_WIDTH,
    30
    )
button_save_adv_sett.setCursor(Qt.CursorShape.PointingHandCursor)
button_save_adv_sett.clicked.connect(save_advanced_settings)
button_save_adv_sett.setFont(QFont('Times', 11, 600))



window_main.show()
if cv.music_on: music.player.play()

sys.exit(app.exec())