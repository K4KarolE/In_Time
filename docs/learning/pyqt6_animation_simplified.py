import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QMovie


if __name__ == "__main__":
    
    app = QApplication([])

    window = QMainWindow()
    window.resize(720, 486)
    window.setWindowTitle("Animation")

    label = QLabel(window)

    skin_selected = 'terminator'
    movie = QMovie(f'skins/{skin_selected}/GIF.GIF')
    
    label.setMovie(movie)
    label.resize(720,486)
    movie.start()
    movie.setSpeed(100)
    
    window.show()


    # ANIMATION SWITCH
    print('\n')
    input(' Press enter to change the animation ')
    skin_selected = 'idiocracy'
    movie = QMovie(f'skins/{skin_selected}/GIF.GIF')
    label.setMovie(movie)
    movie.start()
    movie.setSpeed(100)

    # ANIMATION SPEED CHANGE
    print('\n')
    user_input = int(input('Add new animation speed: '))
    print('\n')
    movie.setSpeed(user_input)


    app.exec()

    # sys.exit(app.exec()) - unnecessary?