import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')
        self.resize(300, 200)

        button = QPushButton(self, text='Sample button')
        button.setGeometry(10,10, 150, 100)
        button.clicked.connect(self.button_clicked)


    def button_clicked(self):
        
        def user_accepted():
            print('\nYeah, go for it!\n')


        saving_mbox = QMessageBox()
        saving_mbox.setWindowTitle('Confirmation')
        saving_mbox.setWindowIcon(QIcon(f'skins/_images/window_settings.ico'))
        saving_mbox.setIcon(QMessageBox.Icon.Question)
        saving_mbox.setText('Saving changes?')
        saving_mbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        saving_mbox.accepted.connect(user_accepted)
        saving_mbox.exec()

    
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()