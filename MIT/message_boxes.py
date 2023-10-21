from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon

class MyMessageBoxConfReq(QMessageBox):
    def __init__(self, question, function, pos_x, pos_y):
        super().__init__()

        self.setWindowTitle('Confirmation needed')
        self.setWindowIcon(QIcon(f'skins/_images/settings.png'))
        self.setIcon(QMessageBox.Icon.Question)
        self.setText(question)
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        self.accepted.connect(function)
        self.move(pos_x, pos_y)
        self.exec()



class MyMessageBoxConfirmation(QMessageBox):
    def __init__(self, message, pos_x, pos_y):
        super().__init__()

        self.setWindowTitle('All set')
        self.setWindowIcon(QIcon(f'skins/_images/settings.png'))
        # self.setIcon(QMessageBox.Icon.Information) # information icon is broken
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.move(pos_x, pos_y)
        self.exec()




class MyMessageBoxError(QMessageBox):
    def __init__(self, message, pos_x, pos_y):
        super().__init__()

        self.setWindowTitle('ERROR')
        self.setWindowIcon(QIcon(f'skins/_images/settings.png'))
        self.setIcon(QMessageBox.Icon.Warning)
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Close)
        self.move(pos_x, pos_y)
        self.exec()
