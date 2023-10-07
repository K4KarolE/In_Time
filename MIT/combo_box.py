
from PyQt6.QtCore import QCoreApplication, QProcess, Qt
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QFont

import sys

from MIT.cons_and_vars import save_settings, load_info, settings_data, skin_selected




class MyComboBox:
    def __init__(self, window_type, combo_pos_x, combo_pos_y):

        skins_dic = settings_data['skins']
        skins_options = []
        for _ in skins_dic:
            skins_options.append(settings_data['skins'][_]['title'])


        def restart():
            QCoreApplication.quit()
            QProcess.startDetached(sys.executable, sys.argv)



        def change_skin():
            settings_data, skin_selected, selected_skin_folder = load_info()
            for selected_title in skins_dic:       
                # SELECTED TITLE(Back to the Future I.) --> FOLDER NAME(back_to_the_future) = skin_selected
                if skins_dic[selected_title]['title'] == self.currentText():
                    settings_data['skin_selected'] = selected_title
                    save_settings(settings_data)
                    restart()


        self = QComboBox(window_type)
        self.addItems(skins_options)
        self.setCurrentText(skins_dic[skin_selected]['title'])
        self.setGeometry(combo_pos_x, combo_pos_y, 160, 20)
        self.currentTextChanged.connect(change_skin)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFont(QFont('Times', 10))