'''

Motion in Time - PyQt6 version

'''

from PyQt6.QtWidgets import QApplication, QTabWidget, QLabel, QPushButton
from PyQt6.QtWidgets import QSlider, QLineEdit, QWidget, QFileDialog
from PyQt6.QtGui import QMovie, QIcon, QFont
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, QTimer, QTime, Qt, QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer

import sys
import shutil
import os
from pathlib import Path

from MIT import MySettingsWindow, MyMainWindow, window_main_set_style, window_skin_set_style
from MIT import window_settings_set_style, button_set_style
from MIT import Data, MyImage, MySlider, MyMessageBoxConfReq, MyMessageBoxConfirmation
from MIT import MyComboBoxSkins, MyComboBoxWidgetUpdate, MyComboBoxFont, MyMessageBoxError
from MIT import save_settings, load_info, restart
from MIT import WORKING_DIRECTORY, settings_data, skin_selected, selected_skin_folder




class Music:
    def __init__(self):
        self.path_music = Path(WORKING_DIRECTORY, 'skins', skin_selected, 'music.mp3')
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(str(self.path_music)))
        self.player.setLoops(-1) # -1=infinite
        self.audio_output.setVolume(cv.music_volume)



def skin_deletion_confirmaiton():
    # DELETING SKIN STATUS AFTER RESTART
    if settings_data['delete_skin']['enabled']:

        if settings_data['delete_skin']['del_proc_completed']:
            MyMessageBoxConfirmation(
                'Skin deleted.',
                WINDOW_CENTER_X,
                WINDOW_CENTER_Y
                )
        else:
            MyMessageBoxError(
            'Sorry, something went wrong.',
            WINDOW_CENTER_X,
            WINDOW_CENTER_Y
            )
        
        settings_data['delete_skin']['enabled'] = False
        save_settings(settings_data)  



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
    seconds.setText(seconds_time)
    
    # BACk - SHADOW
    hours_and_mins_shadow.setText(hours_and_mins_time)
    seconds_shadow.setText(seconds_time)


    time_repositioning()


    # TIME REFRESH - 1000=1sec
    timer.setInterval(1000)



# LOADING DATA FROM JSON
cv = Data()

# MUSIC
music= Music()

## CONSTANTS
# WINDOW MAIN
WINDOW_WIDTH, WINDOW_HEIGHT = 720, 486
WINDOW_CENTER_X = cv.window_main_pos_x + int(WINDOW_WIDTH/2) - 50
WINDOW_CENTER_Y = cv.window_main_pos_y + int(WINDOW_HEIGHT/2) - 50

# WINDWO ADVANCED (STILL IN MAIN)
WINDOW_ADVANCED_ADD_WIDTH = 305
WINDOW_ADVANCED_WIDTH = WINDOW_WIDTH + WINDOW_ADVANCED_ADD_WIDTH
ADV_WIDGETS_WIDTH = 200
FONT_WIDG_GROUP_Y_DIFF = 20

IMAGE_SIZE = 25
ADV_IMG_POS_X = WINDOW_WIDTH + 25
ADV_IMG_POS_Y = 23
ADV_IMG_POS_Y_DIFF = IMAGE_SIZE + 20

ADV_NON_IMG_POS_X = ADV_IMG_POS_X + 40
ADV_NON_IMG_POS_Y = 30
ADV_NON_IMG_POS_Y_DIFF = 40

BUTTON_ADV_HEIGHT = 28
BUTTON_ADV_TEXT_SIZE = 10


# WINDOW SETTINGS
SETT_WIDGETS_WIDTH = 160
WINDOW_SETTINGS_WIDTH, WINDOW_SETTINGS_HEIGHT = 250, 223


# WINDOW ADD SKIN
WINDOW_SKIN_WIDTH, WINDOW_SKIN_HEIGHT = 245, 350



''' APP '''
app = QApplication(sys.argv)

''' DELETING SKIN - CONFIRMATION MESSAGE '''
skin_deletion_confirmaiton()

'''
###########################
###########################

        MAIN WINDOW

###########################
###########################
'''

window_main = MyMainWindow(
                        cv.button_bg_color,
                        cv.button_bg_color_clicked,
                        WINDOW_WIDTH,
                        WINDOW_HEIGHT,
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



'''
################################## 
##################################

    WINDOW SETTINGS - CREATION 

##################################
##################################
'''    
window_settings = MySettingsWindow(
                                    'Settings',
                                    cv.button_bg_color,
                                    cv.button_bg_color_clicked,
                                    WINDOW_SETTINGS_WIDTH,
                                    WINDOW_SETTINGS_HEIGHT,
                                    cv.window_settings_pos_x,
                                    cv.window_settings_pos_y) 


'''
################################## 
##################################

    WINDOW SKIN - CREATION 

##################################
##################################
'''    
window_skin = MySettingsWindow(
                                    'Skins',
                                    cv.button_bg_color,
                                    cv.button_bg_color_clicked,
                                    WINDOW_SKIN_WIDTH,
                                    WINDOW_SKIN_HEIGHT,
                                    cv.window_settings_pos_x,
                                    cv.window_settings_pos_y) 



''' 
#############################
#############################

    WINDOW MAIN - WIDGETS   

#############################
#############################
'''

''' 
#########################
        ANIMATION                   
#########################
'''
label_animation = QLabel(window_main)
movie = QMovie(f'skins/{skin_selected}/GIF.GIF')
label_animation.setMovie(movie)
label_animation.resize(720,486)
movie.start()
movie.setSpeed(cv.animation_speed)  


''' 
####################
        TIME                    
####################
'''
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

''' 
#######################
        BUTTONS              
#######################
'''
ICON_SIZE = 15  # ICON/PICTURE IN THE BUTTONS

''' BUTTON - MUSIC '''
button_image_start = QIcon('skins/_images/start.png')
button_image_stop = QIcon('skins/_images/stop.png')

if cv.music_on:
        music_start_stop_img = button_image_stop
else:
    music_start_stop_img = button_image_start


button_music = QPushButton(window_main, text=None, icon=music_start_stop_img)
button_music.setIconSize(QSize(ICON_SIZE, ICON_SIZE))
button_music.setGeometry(cv.button_music_pos_x, cv.button_music_pos_y, 29, 29)     # pos, pos, size, size
button_music.setCursor(Qt.CursorShape.PointingHandCursor)
button_music.clicked.connect(music_switch_on_off)
button_set_style(button_music, cv.button_bg_color, cv.button_bg_color_clicked)


''' BUTTON - SETTING '''
# button(window) --> SETTINGS WINDOW default launch in center of the main window
button_image_settings = QIcon('skins/_images/settings.png')
button_settings = QPushButton(window_main, text=None, icon=button_image_settings)
button_settings.setIconSize(QSize(ICON_SIZE, ICON_SIZE))       # icon sizing
button_settings.setGeometry(cv.button_settings_pos_x, cv.button_settings_pos_y, 30, 30)     # pos, pos, size, size
button_settings.setCursor(Qt.CursorShape.PointingHandCursor)
button_settings.clicked.connect(window_settings.show)
button_set_style(button_settings, cv.button_bg_color, cv.button_bg_color_clicked)






'''
########################################
########################################

        SETTINGS WINDOW - WIDGETS                  

#######################################
#######################################
'''
''' 
#############################
    IMAGES AND TEXT - SETT        
#############################
'''
IMAGE_SIZE = 30
pos_x = 20
pos_y = 20
pos_y_diff = IMAGE_SIZE + 20

# VOLUME - IMAGE - SETT
MyImage(window_settings, 'volume.png', IMAGE_SIZE, pos_x, pos_y)

# ANIMATION SPEED - IMAGE
MyImage(window_settings, 'animation_speed.png', IMAGE_SIZE, pos_x, pos_y+pos_y_diff)

# SKIN SWITCH - IMAGE - SETT
MyImage(window_settings, 'skin_switch.png', IMAGE_SIZE+8, pos_x-3, pos_y+pos_y_diff*2-3)

# A - ADVANCED - TEXT- SETT
label_A = QLabel(window_settings, text='A')
label_A.move(pos_x+3, pos_y + pos_y_diff*3)
label_A.setStyleSheet("color:'black';font: 30pt 'Times'; font-weight: bold;")
# another solution, no color info: label_A.setFont(QFont('Times', 30, 800))   # style, size, bold


''' 
######################
    SLIDERS - SETT        
######################
'''
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


''' VOLUME - SLIDER - SETT '''
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



''' ANIMATION SPEED - SLIDER - SETT '''
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



'''
#####################################
    SWITCH SKIN - COMBOBOX - SETT               
#####################################
'''
select_skin_cb = MyComboBoxSkins(window_settings, SETT_WIDGETS_WIDTH, False, slider_pos_x, slider_pos_y*5 - 9)



'''
##############################
    ADVANCED BUTTON - SETT               
##############################
'''
def button_advanced_launch():

    # SETTINGS WINDOW BEHAVIOUR IF IT WAS ALREADY CHOSEN
    # IN THE ADVANCED WINDOW
    if select_widget_cb.currentText() != widget_list[3]:
        window_settings.hide()
        button_settings.setEnabled(False)
    else:
        butt_and_win_settings_enable(False)

    for size_incr in range(0, WINDOW_ADVANCED_ADD_WIDTH, 2):
        window_main.setFixedWidth(WINDOW_WIDTH + size_incr)
    
button_advanced = QPushButton(window_settings, text='ADVANCED')
button_advanced.setGeometry(slider_pos_x, slider_pos_y*6 + 12, 160, 25)
button_advanced.setCursor(Qt.CursorShape.PointingHandCursor)
button_advanced.clicked.connect(button_advanced_launch)
button_advanced.setFont(QFont('Times', 10, 600))


'''
#########################################
#########################################

        ADVANCED SETTINGS WINDOW*       

#########################################
#########################################
* still in main window       
'''


def butt_and_win_settings_enable(value):
    window_settings.setEnabled(value)
    button_settings.setEnabled(value)
    if value:
        label_A.setStyleSheet("color:'black';font: 30pt 'Times'; font-weight: bold;")
    else:
        label_A.setStyleSheet("color:'#5E5E5D';font: 30pt 'Times'; font-weight: bold;")

''' 
###################
    FRAME - ADV      
###################
'''
frame_adv_window = QLabel(window_main)
frame_adv_window.setGeometry(ADV_IMG_POS_X-15, ADV_IMG_POS_Y-15, WINDOW_ADVANCED_ADD_WIDTH - 20, WINDOW_HEIGHT - ADV_IMG_POS_Y+10)
frame_adv_window.setStyleSheet("border: 2px solid black; border-radius: 5px;")


''' 
#############################
    IMAGES AND TEXT - ADV        
#############################
'''

# SKIN SWITCH
MyImage(window_main, 'skin_switch.png', IMAGE_SIZE+8, ADV_IMG_POS_X-3, ADV_IMG_POS_Y)

# SETTINGS
MyImage(window_main, 'settings.png', IMAGE_SIZE, ADV_IMG_POS_X, ADV_IMG_POS_Y+ADV_IMG_POS_Y_DIFF)

# LEFT-RIGHT ARROW
image_arrow_left_right_x = ADV_IMG_POS_X-2
image_arrow_left_right_y = ADV_IMG_POS_Y+ADV_IMG_POS_Y_DIFF*2-9
image_arrow_left_right = MyImage(window_main, 'left_right.png', IMAGE_SIZE+5, image_arrow_left_right_x, image_arrow_left_right_y)

# UP-DOWN ARROW
MyImage(window_main, 'up_down.png', IMAGE_SIZE, ADV_IMG_POS_X, ADV_IMG_POS_Y+ADV_IMG_POS_Y_DIFF*3-12)

# SIZE ARROWS
image_arrow_size = MyImage(window_main, 'size.png', IMAGE_SIZE, ADV_IMG_POS_X, ADV_IMG_POS_Y+ADV_IMG_POS_Y_DIFF*4-15)
image_arrow_size.setDisabled(True)

# FONT
MyImage(window_main, 'font.png', IMAGE_SIZE, ADV_IMG_POS_X-2, ADV_IMG_POS_Y+ADV_IMG_POS_Y_DIFF*5 - FONT_WIDG_GROUP_Y_DIFF)

# COLOR
MyImage(window_main, 'color.png', IMAGE_SIZE-3, ADV_IMG_POS_X, ADV_IMG_POS_Y+ADV_IMG_POS_Y_DIFF*6 - FONT_WIDG_GROUP_Y_DIFF-15)



'''
#########################
    COMBOBOXES - ADV               
#########################
'''

''' SKIN SWITCH - COMBOBOX - ADV '''
# RELAUNCHING THE ADVENCED SETTINGS "WINDOW"
# AFTER ADVANCED SKIN SWITCH
if settings_data['is_skin_switch_advanced']:
    window_main.setFixedWidth(WINDOW_WIDTH+WINDOW_ADVANCED_ADD_WIDTH)
    butt_and_win_settings_enable(False)
    settings_data['is_skin_switch_advanced'] = False
    save_settings(settings_data)

MyComboBoxSkins(window_main, ADV_WIDGETS_WIDTH, True, ADV_NON_IMG_POS_X, ADV_NON_IMG_POS_Y)



''' WIDGETS UPDATE - COMBOBOX - ADV '''
widget_dic = {
            'Button: Settings': {               #0     
                "widget": button_settings,
                "name": "button_settings",
                "x": cv.button_settings_pos_x,
                "y": cv.button_settings_pos_y,
                },
            'Button: Play/Stop': {              #1
                "widget": button_music,
                "name": "button_music",
                "x": cv.button_music_pos_x,
                "y": cv.button_music_pos_y
                },
            'Window: Main': {                   #2
                "widget": window_main,
                "name": "window_main",
                "x": cv.window_main_pos_x,
                "y": cv.window_main_pos_y
                },
            'Window: Settings ': {              #3
                "widget": window_settings,
                "name": "window_settings",
                "x": cv.window_settings_pos_x,
                "y": cv.window_settings_pos_y
                },
            'Time: HRS:MINS': {                 #4
                "widget": hours_and_mins,
                "name": "hours_and_mins",
                "x": cv.time_hm_pos_x,
                "y": cv.time_hm_pos_y,
                "size": cv.time_hm_font_size,
                "color": cv.time_font_color,
                "style": cv.time_font_style
                },
            'Time: HRS:MINS - Shadow': {        #5
                "widget": hours_and_mins_shadow,
                "name": "hours_and_mins_shadow",
                "x": cv.time_hm_shadow_pos_x,
                "y": cv.time_hm_shadow_pos_y,
                "size": cv.time_hm_shad_font_size,
                "color": 'black'
                },
            'Time: SEC': {                      #6
                "widget": seconds,
                "name": "seconds",
                "x": cv.time_sec_pos_x,
                "y": cv.time_sec_pos_y,
                "size": cv.time_sec_font_size,
                "color": cv.time_font_color
                },
            'Time: SEC - Shadow':  {            #7
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
        SLIDER_POS_X_DIFF = 30
        slider_pos_x.setGeometry(WINDOW_ADVANCED_WIDTH - SLIDER_POS_X_DIFF - 5,
                                40,
                                20,
                                ADV_WIDGETS_WIDTH)
        
    
    if selected_widget != widget_list[2]:
        slider_pos_x.setOrientation(QtCore.Qt.Orientation.Horizontal)
        slider_pos_x.setGeometry(ADV_NON_IMG_POS_X,
                                ADV_NON_IMG_POS_Y + ADV_NON_IMG_POS_Y_DIFF*2,
                                ADV_WIDGETS_WIDTH,
                                20)
    
    
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
        slider_time_size.setDisabled(False)
        image_arrow_size.setDisabled(False)
        slider_pos_x.setMaximum(WINDOW_WIDTH - widget_dic[selected_widget]['widget'].size().width())
        slider_pos_y.setMaximum(WINDOW_HEIGHT - widget_dic[selected_widget]['widget'].size().height())
    
    if selected_widget not in widget_list[4:8]:
        slider_time_size.setDisabled(True)
        image_arrow_size.setDisabled(True)

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
                                        ADV_NON_IMG_POS_X,
                                        ADV_NON_IMG_POS_Y+ADV_NON_IMG_POS_Y_DIFF
                                        )


''' FONT UPDATE - COMBOBOX - ADV '''
def time_repositioning():
    ''' 
    IF THE TIME GET BIGGER FROM:
        - FONT STYLE UPDATE OR
        - TIME CHANGE: 11:11-->12:24
    IT CAN OVERREACH THE MAIN WINDOW:
    REPOSITION + SAVE NEW VALUE
    '''
    for item in widget_list[4:8]:
            widget_dic[item]['widget'].adjustSize()
            new_format_width = widget_dic[item]['widget'].size().width()
            new_format_height = widget_dic[item]['widget'].size().height()

            if (new_format_width + widget_dic[item]['x']) > WINDOW_WIDTH:
                widget_dic[item]['widget'].move(WINDOW_WIDTH - new_format_width, widget_dic[item]['y'])
                widget_dic[item]['x'] = WINDOW_WIDTH - new_format_width
            
            if (new_format_height + widget_dic[item]['y']) > WINDOW_HEIGHT:
                widget_dic[item]['widget'].move(widget_dic[item]['x'], WINDOW_HEIGHT - new_format_height)
                widget_dic[item]['y'] = WINDOW_HEIGHT - new_format_height



def selected_font_action():

    cv.time_font_style = select_font_cb.currentText()
    widget_dic[widget_list[4]]['style'] = select_font_cb.currentText()
    
    hours_and_mins.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_hm_font_size}pt {cv.time_font_style}; font-weight: bold;')
    hours_and_mins_shadow.setStyleSheet(f'color: black; font: {cv.time_hm_font_size}pt {cv.time_font_style}; font-weight: bold;')
    seconds.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_sec_font_size}pt {cv.time_font_style}; font-weight: bold;')
    seconds_shadow.setStyleSheet(f'color:black; font: {cv.time_sec_font_size}pt {cv.time_font_style}; font-weight: bold;')

    # POSITION UPDATE
    time_repositioning()

    # SLIDER UPDATE
    selected_widget = select_widget_cb.currentText()
    if selected_widget in widget_list[4:8]:
        slider_time_size.setValue(widget_dic[selected_widget]['size'])
        slider_pos_x.setMaximum(WINDOW_WIDTH - widget_dic[selected_widget]['widget'].size().width())
        slider_pos_y.setMaximum(WINDOW_HEIGHT - widget_dic[selected_widget]['widget'].size().height())
        slider_pos_x.setValue(widget_dic[selected_widget]['x'])
        slider_pos_y.setValue(widget_dic[selected_widget]['y'])


select_font_cb = MyComboBoxFont(
                                window_main,
                                selected_font_action,
                                ADV_WIDGETS_WIDTH,
                                ADV_NON_IMG_POS_X,
                                ADV_NON_IMG_POS_Y+ADV_NON_IMG_POS_Y_DIFF*5
                                )



''' COLOR UPDATE - COMBOBOX - ADV '''
color_dic = {
            'Color: Clock': {"color": cv.time_font_color},
            'Color: Buttons, windows': {"color": cv.button_bg_color},
            'Color: Buttons clicked': {"color": cv.button_bg_color_clicked}
            }   

color_list = list(color_dic.keys())

def select_color_action():
    
    input_field_color.setText(color_dic[select_color_cb.currentText()]['color'])


select_color_cb = MyComboBoxWidgetUpdate(
                                        window_main,
                                        color_list,
                                        select_color_action,
                                        ADV_WIDGETS_WIDTH,
                                        ADV_NON_IMG_POS_X,
                                        ADV_NON_IMG_POS_Y+ADV_NON_IMG_POS_Y_DIFF*6-FONT_WIDG_GROUP_Y_DIFF+10
                                        )



'''
#####################
    SLIDERS - ADV
#####################
'''
adv_slider_pos_x = ADV_IMG_POS_X + 15

''' X - MOVE - SLIDER - ADV '''
def update_xy():
    # NO SLIDER UPDATE AFTER WIDGET SELECTION COMBOBOX CHANGE
    if not cv.selected_widg_changed:
        selected_widget = select_widget_cb.currentText()
        widget_dic[selected_widget]['widget'].move(slider_pos_x.value(), slider_pos_y.value())
        widget_dic[selected_widget]['x'] = slider_pos_x.value()
        widget_dic[selected_widget]['y'] = slider_pos_y.value()


slider_pos_x = QSlider(window_main)
slider_pos_x.setGeometry(ADV_NON_IMG_POS_X, ADV_NON_IMG_POS_Y + ADV_NON_IMG_POS_Y_DIFF*2, ADV_WIDGETS_WIDTH, 20)
slider_pos_x.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_pos_x.setMinimum(0)
slider_pos_x.setMaximum(WINDOW_WIDTH - 30)
slider_pos_x.setValue(cv.button_settings_pos_x)
slider_pos_x.setCursor(Qt.CursorShape.PointingHandCursor)
slider_pos_x.valueChanged.connect(update_xy)


''' Y - MOVE - SLIDER - ADV '''
slider_pos_y = QSlider(window_main)
slider_pos_y.setGeometry(ADV_NON_IMG_POS_X, ADV_NON_IMG_POS_Y + ADV_NON_IMG_POS_Y_DIFF*3, ADV_WIDGETS_WIDTH, 20)
slider_pos_y.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_pos_y.setMinimum(0)
slider_pos_y.setMaximum(WINDOW_HEIGHT - 30)
slider_pos_y.setValue(cv.button_settings_pos_y)
slider_pos_y.setCursor(Qt.CursorShape.PointingHandCursor)
slider_pos_y.valueChanged.connect(update_xy)


''' SIZE - SLIDER - ADV '''
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
slider_time_size.setGeometry(ADV_NON_IMG_POS_X, ADV_NON_IMG_POS_Y + ADV_NON_IMG_POS_Y_DIFF*4, ADV_WIDGETS_WIDTH, 20)
slider_time_size.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_time_size.setMinimum(20)
slider_time_size.setMaximum(100)
slider_time_size.setValue(cv.button_settings_pos_y)
slider_time_size.setCursor(Qt.CursorShape.PointingHandCursor)
slider_time_size.valueChanged.connect(update_size)
slider_time_size.setDisabled(True)


'''
#######################
    INPUT FIELD - ADV   
#######################
'''
INPUT_FIELD_COLOR_WIDTH = ADV_WIDGETS_WIDTH-100
input_field_color = QLineEdit(window_main, text=cv.time_font_color)
input_field_color.setGeometry(
    ADV_NON_IMG_POS_X,
    ADV_NON_IMG_POS_Y+ADV_NON_IMG_POS_Y_DIFF*7-FONT_WIDG_GROUP_Y_DIFF,
    INPUT_FIELD_COLOR_WIDTH,
    20
    )
input_field_color.setCursor(Qt.CursorShape.PointingHandCursor)
input_field_color.setFont(QFont('Times', 10, 500))



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
button_close.setIconSize(QSize(10,10))
button_close.setGeometry(WINDOW_ADVANCED_WIDTH-30, 12, 16, 16)     # pos, pos, size, size
button_close.setCursor(Qt.CursorShape.PointingHandCursor)
button_close.clicked.connect(close_advanced_window)
button_close.setStyleSheet("border-radius: 4px; border: 2px solid black;")




''' BUTTON - UPDATE COLOR - ADV '''
def update_color():

    selected_widgets = select_color_cb.currentText()
    
    if selected_widgets == color_list[0]:
        cv.time_font_color = input_field_color.text()
        hours_and_mins.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_hm_font_size}pt {cv.time_font_style}; font-weight: bold;')
        seconds.setStyleSheet(f'color:{cv.time_font_color}; font: {cv.time_sec_font_size}pt {cv.time_font_style}; font-weight: bold;')
    
        widget_dic[widget_list[4]]['color'] = cv.time_font_color
        widget_dic[widget_list[6]]['color'] = cv.time_font_color
    
    else:
        # BUTTONS, WINDOWS
        if selected_widgets == color_list[1]:
            cv.button_bg_color = input_field_color.text()
        # BUTTON CLICKED ON MAIN WINDOW
        if selected_widgets == color_list[2]:
            cv.button_bg_color_clicked = input_field_color.text()
        
        window_main_set_style(window_main, cv.button_bg_color, cv.button_bg_color_clicked)
        window_settings_set_style(window_settings, cv.button_bg_color, cv.button_bg_color_clicked)
        button_set_style(button_settings, cv.button_bg_color, cv.button_bg_color_clicked)
        button_set_style(button_music, cv.button_bg_color, cv.button_bg_color_clicked)
   
    
     
button_update_color = QPushButton(window_main, text='UPDATE')
button_update_color.setGeometry(
    ADV_NON_IMG_POS_X + INPUT_FIELD_COLOR_WIDTH + 10,
    ADV_NON_IMG_POS_Y + ADV_NON_IMG_POS_Y_DIFF *7 - FONT_WIDG_GROUP_Y_DIFF - 2,
    ADV_WIDGETS_WIDTH - INPUT_FIELD_COLOR_WIDTH - 10,
    BUTTON_ADV_HEIGHT
    )
button_update_color.setCursor(Qt.CursorShape.PointingHandCursor)
button_update_color.clicked.connect(update_color)
button_update_color.setFont(QFont('Times', 10, 600))



''' BUTTON - SAVE - ADV '''
def save_advanced_settings():

    try:
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
    
        MyMessageBoxConfirmation(
            'Settings saved',
            WINDOW_CENTER_X,
            WINDOW_CENTER_Y
            )
        

    except:
        MyMessageBoxError(
            'Sorry, something went wrong.\n\nChanges are not saved!',
            WINDOW_CENTER_X,
            WINDOW_CENTER_Y
            )





# MESSAGE BOX - SAVING
def messagebox_save_adv_sett():

    MyMessageBoxConfReq(
                        'Saving changes?',
                        save_advanced_settings,
                        WINDOW_CENTER_X,
                        WINDOW_CENTER_Y
                        )


button_save_adv_sett = QPushButton(window_main, text='SAVE SETTINGS')
button_save_adv_sett.setGeometry(
    ADV_NON_IMG_POS_X,
    ADV_NON_IMG_POS_Y + ADV_NON_IMG_POS_Y_DIFF*8-FONT_WIDG_GROUP_Y_DIFF,
    ADV_WIDGETS_WIDTH,
    BUTTON_ADV_HEIGHT
    )
button_save_adv_sett.setCursor(Qt.CursorShape.PointingHandCursor)
button_save_adv_sett.clicked.connect(messagebox_save_adv_sett)
button_save_adv_sett.setFont(QFont('Times', BUTTON_ADV_TEXT_SIZE, 600))



''' BUTTON - DELETE SKIN - ADV '''
def delete_skin_setup():
    settings_data['delete_skin']['enabled'] = True
    settings_data['delete_skin']['target_skin'] = settings_data['skin_selected']

    if settings_data['delete_skin']['target_skin'] == list(settings_data['skins'].keys())[0]:
        settings_data['skin_selected'] = list(settings_data['skins'].keys())[1]

    else:
        settings_data['skin_selected'] = list(settings_data['skins'].keys())[0]

    save_settings(settings_data)
    restart()



# MESSAGE BOX - DELETE SKIN
def messagebox_delete_skin():

    if len(list(settings_data['skins'].keys())) == 1:
    
        MyMessageBoxError(
                        'Sorry, not allowed to delete the last skin.  ',
                        WINDOW_CENTER_X - 100,
                        WINDOW_CENTER_Y
                        )
    else:

        MyMessageBoxConfReq(
                            "Are you sure you want to delete the current skin?\n\n"
                            f"                       {select_skin_cb.currentText()}\n\n"
                            "The skin`s folder will be permanently deleted:\n"
                            f"{Path(WORKING_DIRECTORY, 'skins', settings_data['skin_selected'])}    ",
                            delete_skin_setup,
                            WINDOW_CENTER_X - 100,
                            WINDOW_CENTER_Y
                            )



button_delete_skin = QPushButton(window_main, text='DELETE SKIN')
button_delete_skin.setGeometry(
    ADV_NON_IMG_POS_X,
    ADV_NON_IMG_POS_Y + ADV_NON_IMG_POS_Y_DIFF *9 + 15,
    ADV_WIDGETS_WIDTH,
    BUTTON_ADV_HEIGHT
    )
button_delete_skin.setCursor(Qt.CursorShape.PointingHandCursor)
button_delete_skin.clicked.connect(messagebox_delete_skin)
button_delete_skin.setFont(QFont('Times', BUTTON_ADV_TEXT_SIZE, 600))



''' BUTTON - ADD NEW SKIN - ADV '''
def save_new_skin():
    pass

button_save_new_skin = QPushButton(window_main, text='ADD / EDIT SKIN')
button_save_new_skin.setGeometry(
    ADV_NON_IMG_POS_X,
    WINDOW_HEIGHT - BUTTON_ADV_HEIGHT - 20,
    ADV_WIDGETS_WIDTH,
    BUTTON_ADV_HEIGHT
    )
button_save_new_skin.setCursor(Qt.CursorShape.PointingHandCursor)
button_save_new_skin.clicked.connect(window_skin.show)
button_save_new_skin.setFont(QFont('Times', BUTTON_ADV_TEXT_SIZE, 600))



''' 
#################################
#################################

    WINDOW SKIN - WIDGETS   

#################################
#################################
'''

TABS_POS_X = 20
TABS_POS_Y = 20
SKIN_WIDGET_POS_X = 20
SKIN_WIDEGT_POS_Y = 20
SKIN_WIDEGT_POS_Y_diff = 40
SKIN_WIDGET_WIDTH = 160
BUTTON_SKIN_HEIGHT = 25

tabs = QTabWidget(window_skin)
tab_add_skin = QWidget() 
tab_edit_skin = QWidget() 
tabs.addTab(tab_add_skin, ' Add Skin ')
tabs.addTab(tab_edit_skin, 'Edit Current Skin')
tabs.resize(WINDOW_SKIN_WIDTH-TABS_POS_X*2, WINDOW_SKIN_HEIGHT-TABS_POS_Y*2) 
tabs.move(20, 20)
tabs.setTabShape(QTabWidget.TabShape.Triangular)
tabs.setFont(QFont('Times', 10, 500))
window_skin_set_style(tabs, 'lightgrey', 'darkgrey')


'''
###################################
    EDIT CURRENT SKIN - WIDGETS   
###################################
'''

''' SKIN NAME - TEXT '''
skin_name_lable = QLabel(tab_edit_skin, text='Name of the skin')
skin_name_lable.move(SKIN_WIDGET_POS_X, SKIN_WIDEGT_POS_Y)
skin_name_lable.setFont(QFont('Times', 10, 600))


''' SKIN NAME - INPUT FIELD '''
input_field_skin_name = QLineEdit(tab_edit_skin)
input_field_skin_name.setText(select_skin_cb.currentText())
input_field_skin_name.setGeometry(
    SKIN_WIDGET_POS_X,
    SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff-22, 
    SKIN_WIDGET_WIDTH,
    20)
input_field_skin_name.setFont(QFont('Times', 10, 500))
input_field_skin_name.setCursor(Qt.CursorShape.PointingHandCursor)


''' WINDOW TITLE - TEXT '''
skin_window_title_lable = QLabel(tab_edit_skin, text='Window Title')
skin_window_title_lable.move(
    SKIN_WIDGET_POS_X,
    SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff + 10)
skin_window_title_lable.setFont(QFont('Times', 10, 600))


''' WINDOW TITLE - INPUT FIELD '''
input_field_window_title = QLineEdit(tab_edit_skin)
input_field_window_title.setText(selected_skin_folder['window_title'])
input_field_window_title.setGeometry(
    SKIN_WIDGET_POS_X,
    SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff * 2 - 10, 
    SKIN_WIDGET_WIDTH,
    20)
input_field_window_title.setFont(QFont('Times', 10, 500))
input_field_window_title.setCursor(Qt.CursorShape.PointingHandCursor)

skin_dic = {
            'gif': {
                    'button_title': 'ANIMATION - GIF',
                    'path': ''
                    },
            'music': {
                    'button_title': 'MUSIC - MP3',
                    'path': ''
                    },
            'icon': {
                    'button_title': 'ICON - PNG',
                    'path': ''
                    }
            }


''' BUTTON - GIF UPDATE '''
def button_gif_update_clicked():
    dialog_gif_update = QFileDialog()
    dialog_gif_update.setWindowTitle("Select a GIF file")
    dialog_gif_update.setNameFilter("GIF files (*.gif)")
    dialog_gif_update.exec()
    if dialog_gif_update.exec:
        skin_dic['gif']['path'] = dialog_gif_update.selectedFiles()
        button_gif_update.setText(f"{skin_dic['gif']['button_title']} \u2713")

button_gif_update = QPushButton(tab_edit_skin, text=skin_dic['gif']['button_title'])
button_gif_update.setGeometry(
    SKIN_WIDGET_POS_X,
    int(SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff*2.7),
    SKIN_WIDGET_WIDTH,
    BUTTON_SKIN_HEIGHT
    )
button_gif_update.setCursor(Qt.CursorShape.PointingHandCursor)
button_gif_update.clicked.connect(button_gif_update_clicked)
button_gif_update.setFont(QFont('Times', 10, 600))



''' BUTTON - MUSIC UPDATE '''
def button_music_update_clicked():
    dialog_music_update = QFileDialog()
    dialog_music_update.setWindowTitle("Select an MP3 file")
    dialog_music_update.setNameFilter("MP3 files (*.mp3)")
    dialog_music_update.exec()
    if dialog_music_update.exec:
        skin_dic['music']['path'] = dialog_music_update.selectedFiles()
        button_music_update.setText(f"{skin_dic['music']['button_title']} \u2713")

button_music_update = QPushButton(tab_edit_skin, text=skin_dic['music']['button_title'])
button_music_update.setGeometry(
    SKIN_WIDGET_POS_X,
    int(SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff*3.5),
    SKIN_WIDGET_WIDTH,
    BUTTON_SKIN_HEIGHT
    )
button_music_update.setCursor(Qt.CursorShape.PointingHandCursor)
button_music_update.clicked.connect(button_music_update_clicked)
button_music_update.setFont(QFont('Times', 10, 600))



''' BUTTON - WINDOW ICON UPDATE '''
def button_icon_update_clicked():
    dialog_icon_update = QFileDialog()
    dialog_icon_update.setWindowTitle("Select a PNG file")
    dialog_icon_update.setNameFilter("PNG files (*.png)")
    dialog_icon_update.exec()
    if dialog_icon_update.exec:
        skin_dic['icon']['path'] = dialog_icon_update.selectedFiles()
        button_icon_update.setText(f"{skin_dic['icon']['button_title']} \u2713")

button_icon_update = QPushButton(tab_edit_skin, text=skin_dic['icon']['button_title'])
button_icon_update.setGeometry(
    SKIN_WIDGET_POS_X,
    int(SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff*4.3),
    SKIN_WIDGET_WIDTH,
    BUTTON_SKIN_HEIGHT
    )
button_icon_update.setCursor(Qt.CursorShape.PointingHandCursor)
button_icon_update.clicked.connect(button_icon_update_clicked)
button_icon_update.setFont(QFont('Times', 10, 600))


''' BUTTON - UPDATE '''
def update_skin_action():
    any_change = False
    db_save_needed = False

    settings_data, skin_selected, selected_skin_folder = load_info()
    
    ''' SKIN NAME '''
    if input_field_skin_name.text() != selected_skin_folder['title']:
        if len(input_field_skin_name.text().strip()) > 0:
            selected_skin_folder['title'] = input_field_skin_name.text()[0:30]
            any_change = True
            db_save_needed = True

        else:
            MyMessageBoxError(
                'The name field can not be empty!  ',
                WINDOW_CENTER_X,
                WINDOW_CENTER_Y
                )
    

    ''' WINDOW TITLE '''
    if input_field_window_title.text() != selected_skin_folder['window_title']:
        selected_skin_folder['window_title'] = input_field_window_title.text()[0:108]
        any_change = True
        db_save_needed = True
    
    if not input_field_window_title.text():
        selected_skin_folder['window_title'] = 'It`s Python baby!'
        any_change = True
        db_save_needed = True


    ''' GIF '''
    if skin_dic['gif']['path']:
        shutil.copy(skin_dic['gif']['path'][0], f'skins/{skin_selected}/GIF.GIF')
        print(skin_dic['gif']['path'])
        any_change = True
    
    ''' MUSIC '''
    if skin_dic['music']['path']:
        shutil.copy(skin_dic['music']['path'][0], f'skins/{skin_selected}/music.mp3')
        any_change = True

    ''' ICON '''
    if skin_dic['icon']['path']:
        shutil.copy(skin_dic['icon']['path'][0], f'skins/{skin_selected}/icon.png')
        any_change = True


    if db_save_needed:
        save_settings(settings_data)

    if any_change:
        restart()



button_skin_update = QPushButton(tab_edit_skin, text='UPDATE')
button_skin_update.setGeometry(
    SKIN_WIDGET_POS_X,
    int(SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff*5.6),
    SKIN_WIDGET_WIDTH,
    BUTTON_SKIN_HEIGHT
    )
button_skin_update.setCursor(Qt.CursorShape.PointingHandCursor)
button_skin_update.clicked.connect(update_skin_action)
button_skin_update.setFont(QFont('Times', 10, 600))



'''
###################################
    ADD NEW SKIN - WIDGETS   
###################################
'''

''' SKIN NAME - TEXT '''
skin_name_lable_add = QLabel(tab_add_skin, text='Name of the skin')
skin_name_lable_add.move(SKIN_WIDGET_POS_X, SKIN_WIDEGT_POS_Y)
skin_name_lable_add.setFont(QFont('Times', 10, 600))


''' SKIN NAME - INPUT FIELD '''
input_field_skin_name_add = QLineEdit(tab_add_skin)
input_field_skin_name_add.setGeometry(
    SKIN_WIDGET_POS_X,
    SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff-22, 
    SKIN_WIDGET_WIDTH,
    20)
input_field_skin_name_add.setFont(QFont('Times', 10, 500))
input_field_skin_name_add.setCursor(Qt.CursorShape.PointingHandCursor)


''' WINDOW TITLE - TEXT '''
skin_window_title_lable_add = QLabel(tab_add_skin, text='Window Title')
skin_window_title_lable_add.move(
    SKIN_WIDGET_POS_X,
    SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff + 10)
skin_window_title_lable_add.setFont(QFont('Times', 10, 600))


''' WINDOW TITLE - INPUT FIELD '''
input_field_window_title_add = QLineEdit(tab_add_skin)
input_field_window_title_add.setGeometry(
    SKIN_WIDGET_POS_X,
    SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff * 2 - 10, 
    SKIN_WIDGET_WIDTH,
    20)
input_field_window_title_add.setFont(QFont('Times', 10, 500))
input_field_window_title_add.setCursor(Qt.CursorShape.PointingHandCursor)


''' BUTTON - ADD GIF '''
def button_gif_update_clicked():
    dialog_gif_add = QFileDialog()
    dialog_gif_add.setWindowTitle("Select a GIF file")
    dialog_gif_add.setNameFilter("GIF files (*.gif)")
    dialog_gif_add.exec()
    if dialog_gif_add.exec:
        skin_dic['gif']['path'] = dialog_gif_add.selectedFiles()
        button_gif_add.setText(f"{skin_dic['gif']['button_title']} \u2713")

button_gif_add = QPushButton(tab_add_skin, text=skin_dic['gif']['button_title'])
button_gif_add.setGeometry(
    SKIN_WIDGET_POS_X,
    int(SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff*2.7),
    SKIN_WIDGET_WIDTH,
    BUTTON_SKIN_HEIGHT
    )
button_gif_add.setCursor(Qt.CursorShape.PointingHandCursor)
button_gif_add.clicked.connect(button_gif_update_clicked)
button_gif_add.setFont(QFont('Times', 10, 600))


''' BUTTON - ADD MUSIC '''
def button_music_update_clicked():
    dialog_music_add = QFileDialog()
    dialog_music_add.setWindowTitle("Select an MP3 file")
    dialog_music_add.setNameFilter("MP3 files (*.mp3)")
    dialog_music_add.exec()
    if dialog_music_add.exec:
        skin_dic['music']['path'] = dialog_music_add.selectedFiles()
        button_music_add.setText(f"{skin_dic['music']['button_title']} \u2713")

button_music_add = QPushButton(tab_add_skin, text=skin_dic['music']['button_title'])
button_music_add.setGeometry(
    SKIN_WIDGET_POS_X,
    int(SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff*3.5),
    SKIN_WIDGET_WIDTH,
    BUTTON_SKIN_HEIGHT
    )
button_music_add.setCursor(Qt.CursorShape.PointingHandCursor)
button_music_add.clicked.connect(button_music_update_clicked)
button_music_add.setFont(QFont('Times', 10, 600))


''' BUTTON - ADD ICON '''
def button_icon_update_clicked():
    dialog_icon_add = QFileDialog()
    dialog_icon_add.setWindowTitle("Select a PNG file")
    dialog_icon_add.setNameFilter("PNG files (*.png)")
    dialog_icon_add.exec()
    if dialog_icon_add.exec:
        skin_dic['icon']['path'] = dialog_icon_add.selectedFiles()
        button_icon_add.setText(f"{skin_dic['icon']['button_title']} \u2713")

button_icon_add = QPushButton(tab_add_skin, text=skin_dic['icon']['button_title'])
button_icon_add.setGeometry(
    SKIN_WIDGET_POS_X,
    int(SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff*4.3),
    SKIN_WIDGET_WIDTH,
    BUTTON_SKIN_HEIGHT
    )
button_icon_add.setCursor(Qt.CursorShape.PointingHandCursor)
button_icon_add.clicked.connect(button_icon_update_clicked)
button_icon_add.setFont(QFont('Times', 10, 600))



''' BUTTON - ADD SKIN '''
def add_skin_action():
    all_set = False

    settings_data, skin_selected, selected_skin_folder = load_info()
    
    ''' SKIN NAME '''
    # INPUT --> FOLDER NAME
    if len(input_field_skin_name_add.text().strip().lower()) > 0:
        # TRANSFORM INPUT
        folder_name =''
        for letter in input_field_skin_name_add.text():
            if len(folder_name) < 20:
                if letter.isalpha() or letter.isdecimal():
                    folder_name = f'{folder_name}{letter}'

        # CHECKING IF THE FOLDER NAME ALREADY EXISTS
        for existing_title in settings_data['skins'].keys():
            if existing_title == folder_name:
                folder_name = f'{folder_name}_'

        # CREATING JSON DIC.
        settings_data['skins'][folder_name] = settings_data['skins'][settings_data['skin_selected']]


        all_set = True


    if len(input_field_skin_name_add.text().strip()) == 0:
        MyMessageBoxError(
            'The name field can not be empty!  ',
            WINDOW_CENTER_X,
            WINDOW_CENTER_Y
                )
    

    if all_set:

        if skin_dic['gif']['path'] and skin_dic['music']['path'] and skin_dic['icon']['path']:
            

            os.mkdir(Path(Path().resolve(), 'skins', folder_name))

            shutil.copy(skin_dic['gif']['path'][0], f'skins/{folder_name}/GIF.GIF')
            
            shutil.copy(skin_dic['music']['path'][0], f'skins/{folder_name}/music.mp3')

            shutil.copy(skin_dic['icon']['path'][0], f'skins/{folder_name}/icon.png')
            
            all_set = True
        
        else:
            MyMessageBoxError(
            'All file types need to be added!  ',
            WINDOW_CENTER_X,
            WINDOW_CENTER_Y
                )
            all_set = False
        


    if all_set:
        # CREATING NEW JSON DIC.
        save_settings(settings_data)    

        # ABLE TO REACH THE NEW JSON DIC (WITHOUT AFFECTING THE ORIGINAL ONE)
        settings_data, skin_selected, selected_skin_folder = load_info()
        
        ''' SKIN NAME '''
        settings_data['skins'][folder_name]['title'] = input_field_skin_name_add.text().strip()

        ''' WINDOW TITLE '''
        if len(input_field_window_title_add.text().strip()) > 0:
            settings_data['skins'][folder_name]['window_title'] = input_field_window_title_add.text()[0:108]
        
        if len(input_field_window_title_add.text().strip()) == 0:
            settings_data['skins'][folder_name]['window_title'] = 'It`s Python baby!'
        
        ''' SKIN SELECTED '''
        settings_data['skin_selected'] = folder_name
        
        save_settings(settings_data)

        restart()


button_skin_add = QPushButton(tab_add_skin, text='CREATE SKIN')
button_skin_add.setGeometry(
    SKIN_WIDGET_POS_X,
    int(SKIN_WIDEGT_POS_Y + SKIN_WIDEGT_POS_Y_diff*5.6),
    SKIN_WIDGET_WIDTH,
    BUTTON_SKIN_HEIGHT
    )
button_skin_add.setCursor(Qt.CursorShape.PointingHandCursor)
button_skin_add.clicked.connect(add_skin_action)
button_skin_add.setFont(QFont('Times', 10, 600))



window_main.show()
if cv.music_on: music.player.play()

sys.exit(app.exec())