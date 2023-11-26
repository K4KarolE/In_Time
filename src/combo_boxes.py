
from PyQt6.QtCore import QCoreApplication, QProcess, Qt
from PyQt6.QtWidgets import QComboBox, QFontComboBox
from PyQt6.QtGui import QFont

import sys

from .cons_and_vars import save_settings, load_info, settings_data, selected_skin_folder




class MyComboBoxSkins(QComboBox):
    def __init__(self, window_type, width, is_skin_switch_advanced, pos_x, pos_y):
        super().__init__()
        
        def change_skin():
            settings_data, skin_selected, selected_skin_folder = load_info()
            for selected_title in skins_dic:       
                # SELECTED TITLE(Back to the Future I.) --> FOLDER NAME(back_to_the_future) = skin_selected
                if skins_dic[selected_title]['title'] == self.currentText():
                    settings_data['skin_selected'] = selected_title
                    if is_skin_switch_advanced:
                        settings_data['is_skin_switch_advanced'] = True
                    save_settings(settings_data)
                    restart()     

        skins_dic = settings_data['skins']
        skins_options = []
        for _ in skins_dic:
            skins_options.append(settings_data['skins'][_]['title'])
        skins_options.sort()

        self.setParent(window_type)
        self.addItems(skins_options)
        self.setCurrentText(selected_skin_folder['title'])
        self.setGeometry(pos_x, pos_y, width, 20)
        self.currentTextChanged.connect(change_skin)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFont(QFont('Times', 10))



class MyComboBoxWidgetUpdate(QComboBox):
    def __init__(self, window_type, widgets_list, selected_widget_action, width, pos_x, pos_y):
        super().__init__()

        self.setParent(window_type)
        self.addItems(widgets_list)
        self.setGeometry(pos_x, pos_y, width, 20)
        self.currentTextChanged.connect(selected_widget_action)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFont(QFont('Times', 10))



class MyComboBoxFont(QFontComboBox):
    def __init__(self, window_type, selected_widget_action, width, pos_x, pos_y):
        super().__init__()

        self.setParent(window_type)
        self.setCurrentText(selected_skin_folder['json_widg_params']['hours_and_mins']['style'])
        self.setGeometry(pos_x, pos_y, width, 20)
        self.currentTextChanged.connect(selected_widget_action)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFont(QFont('Times', 10))



def restart():
    QCoreApplication.quit()
    QProcess.startDetached(sys.executable, sys.argv)