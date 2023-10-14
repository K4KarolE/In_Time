
from dataclasses import dataclass
from pathlib import Path
from json import load, dump

def open_settings():
    with open(PATH_JSON) as f:
        settings_data = load(f)
    return settings_data

def save_settings(settings_data):
    with open(PATH_JSON, 'w') as f:
        dump(settings_data, f, indent=2)
    return

def load_info():
    settings_data = open_settings()
    skin_selected = settings_data['skin_selected']                                  
    selected_skin_folder = settings_data['skins'][skin_selected]
    return settings_data, skin_selected, selected_skin_folder


WORKING_DIRECTORY = Path().resolve()
PATH_JSON = Path(WORKING_DIRECTORY, 'settings_db_pyqt.json')
settings_data, skin_selected, selected_skin_folder = load_info()


## DELETE SKIN
if settings_data['delete_skin']['enabled']:

    del settings_data['skins'][settings_data['delete_skin']['target_skin']]
    settings_data['delete_skin']['enabled'] = False
    settings_data['delete_skin']['target_skin'] = 'None'

    save_settings(settings_data)
    settings_data, skin_selected, selected_skin_folder = load_info()


@dataclass
class Data:

    # MUSIC
    music_on = settings_data['music_on']
    music_volume = selected_skin_folder['music_volume']

    # ANIMATION
    animation_speed = selected_skin_folder['animation_speed']  # 100% = original

    # BUTTONS COLOR
    button_bg_color = selected_skin_folder['button_bg_color']
    button_bg_color_clicked = selected_skin_folder['button_bg_color_clicked']

    ## TIME
    time_font_color = selected_skin_folder['json_widg_params']['hours_and_mins']['color']
    time_font_style = selected_skin_folder['json_widg_params']['hours_and_mins']['style']

    time_hm_font_size = selected_skin_folder['json_widg_params']['hours_and_mins']['size']
    time_hm_shad_font_size = selected_skin_folder['json_widg_params']['hours_and_mins_shadow']['size']

    time_sec_font_size = selected_skin_folder['json_widg_params']['seconds']['size']
    time_sec_shad_font_size = selected_skin_folder['json_widg_params']['seconds_shadow']['size']

   
    # WIDGET SELECTING COMBOBOX
    selected_widg_changed = False


    ## POSITIONS
    # HOURS & MINUTES
    time_hm_pos_x = selected_skin_folder['json_widg_params']['hours_and_mins']['x']
    time_hm_pos_y = selected_skin_folder['json_widg_params']['hours_and_mins']['y']
    # HOURS & MINUTES - SHADOW
    time_hm_shadow_pos_x = selected_skin_folder['json_widg_params']['hours_and_mins_shadow']['x']
    time_hm_shadow_pos_y = selected_skin_folder['json_widg_params']['hours_and_mins_shadow']['y']

    # SECONDS
    time_sec_pos_x = selected_skin_folder['json_widg_params']['seconds']['x']
    time_sec_pos_y = selected_skin_folder['json_widg_params']['seconds']['y']
    # SECONDS - SHADOW
    time_sec_shadow_pos_x = selected_skin_folder['json_widg_params']['seconds_shadow']['x']
    time_sec_shadow_pos_y = selected_skin_folder['json_widg_params']['seconds_shadow']['y']


    # BUTTON MUSIC
    button_music_pos_x = selected_skin_folder['json_widg_params']['button_music']['x']
    button_music_pos_y = selected_skin_folder['json_widg_params']['button_music']['y']

    # BUTTON SETTINGS
    button_settings_pos_x = selected_skin_folder['json_widg_params']['button_settings']['x']
    button_settings_pos_y = selected_skin_folder['json_widg_params']['button_settings']['y']

    # WINDOW SETTINGS
    window_settings_pos_x = settings_data['window_settings']['x']
    window_settings_pos_y = settings_data['window_settings']['y']

    # WINDOW MAIN
    window_main_pos_x = settings_data['window_main']['x']
    window_main_pos_y = settings_data['window_main']['y']



