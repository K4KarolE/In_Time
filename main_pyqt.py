'''
Motion in Time - PyQt6 version
'''

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QMovie, QIcon, QPixmap
from PyQt6.QtCore import QSize


if __name__ == "__main__":
    
    app = QApplication([])

    window = QMainWindow()
    window.resize(720, 486)
    window.setWindowTitle("Animation")


    label_animation = QLabel(window)
    
    icon_size = QSize(25,25)
    icon = QIcon('skins/_icons/icon_settings.png')
 
    button_settings = QPushButton(window, text=None, icon=icon)
    button_settings.setIconSize(icon_size)
    button_settings.setFlat(False)
    button_settings.setStyleSheet("background-color: #AF0000")
    button_settings.setGeometry(100, 100, 35, 35)
   

    
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


    app.exec()

    # sys.exit(app.exec()) - unnecessary?