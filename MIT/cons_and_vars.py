
from dataclasses import dataclass
from pathlib import Path
from json import load, dump

def open_settings():
    f = open(path_json)
    settings_data = load(f)
    return settings_data

def save_settings(settings_data):
    with open(path_json, 'w') as f:
        dump(settings_data, f, indent=2)
    return

def load_info():
    settings_data = open_settings()
    skin_selected = settings_data['skin_selected']                                  
    selected_skin_folder = settings_data['skins'][skin_selected]
    return settings_data, skin_selected, selected_skin_folder


working_directory = Path().resolve()
path_json = Path(working_directory, 'settings_db_pyqt.json')
settings_data, skin_selected, selected_skin_folder = load_info()



@dataclass
class Data:
    # MUSIC
    music_on = settings_data['music_on']
    music_volume = selected_skin_folder['music_volume']

    # ANIMATION
    animation_speed = selected_skin_folder['animation_speed']  # 100% = original

    # BUTTONS
    button_bg_color = selected_skin_folder['button_bg_color']
    button_bg_color_clicked = selected_skin_folder['button_bg_color_clicked']
    button_pos_x = selected_skin_folder['button_pos_x']
    button_pos_y = selected_skin_folder['button_pos_y']

    # TIME
    time_font_color = selected_skin_folder['time_font_color']
    time_font_style = selected_skin_folder['time_font_style']
    time_hm_font_size = selected_skin_folder['time_hm_font_size']
    time_sec_font_size = selected_skin_folder['time_sec_font_size']

    # HOURS & MINUTES
    time_hm_pos_x = selected_skin_folder['time_hm_pos_x']
    time_hm_pos_y = selected_skin_folder['time_hm_pos_y']

    # SECONDS
    time_sec_pos_x = selected_skin_folder['time_sec_pos_x']
    time_sec_pos_y = selected_skin_folder['time_sec_pos_y']

    # WINDOW SETTINGS - POSITIONING
    window_settings_pos_x_diff = selected_skin_folder['window_settings_pos_x_diff']
    window_settings_pos_y_diff = selected_skin_folder['window_settings_pos_y_diff']
