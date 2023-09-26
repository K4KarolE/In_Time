'''
Motion in Time - PyQt6 version
'''

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QMovie, QIcon, QPixmap
from PyQt6.QtCore import QSize


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.resize(720, 486)
    window.setWindowTitle("Animation")


    label_animation = QLabel(window)
    
   
    
    # BUTTON - SETTINGS
    icon_settings = QIcon('skins/_icons/icon_settings.png')
    button_settings = QPushButton(window, text=None, icon=icon_settings)
    button_settings.setIconSize(QSize(20,20))       # icon sizing
    button_settings.setGeometry(20, 30, 30, 30)     # pos, pos, size, size


    # BUTTON - SETTINGS
    icon_settings = QIcon('skins/_icons/icon_start.png')
    button_music = QPushButton(window, text=None, icon=icon_settings)
    button_music.setIconSize(QSize(20,20))
    button_music.setGeometry(20, 62, 29, 29)     # pos, pos, size, size
  
    skin_selected = 'terminator'

    
    # SKINS
    if skin_selected == 'terminator':

        app.setStyleSheet("QPushButton"
                            # DEFAULT
                            "{"
                            "background-color : #AF0000;"
                            "border-radius: 5px;"          # corner roundness
                            "border: 2px solid black;"
                            "}"
                            # CLICKED
                            "QPushButton::pressed"
                            "{"
                            "background-color : #400000;"
                            "}"
                            )



    
    skin_selected = 'terminator'
    movie = QMovie(f'skins/{skin_selected}/GIF.GIF')
    label_animation.setMovie(movie)
    label_animation.resize(720,486)
    movie.start()
    movie.setSpeed(100)
    
    window.show()


    # ANIMATION SWITCH
    # print('\n')
    # input(' Press enter to change the animation ')
    # skin_selected = 'idiocracy'
    # movie = QMovie(f'skins/{skin_selected}/GIF.GIF')
    # label_animation.setMovie(movie)
    # movie.start()
    # movie.setSpeed(100)

    # # ANIMATION SPEED CHANGE
    # print('\n')
    # user_input = int(input('Add new animation speed: '))
    # print('\n')
    # if user_input: movie.setSpeed(user_input)


    # app.exec()

    sys.exit(app.exec())