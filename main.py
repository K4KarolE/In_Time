
from tkinter import *
from time import strftime

import json
from pathlib import Path

import platform
import os

import pygame       # for playing music
pygame.init()



def open_settings():
    f = open(path_json)
    settings_data = json.load(f)
    return settings_data

def save_settings(settings_data):
    with open(path_json, 'w') as f:
        json.dump(settings_data, f, indent=2)
    return

def time_display():
    # HOURES:MINUTES
    hours_and_mins = strftime('%H:%M')
    hours_and_mins_label.config(text=hours_and_mins)
    # :SECONDS
    seconds = strftime(':%S')
    seconds_label.config(text=seconds)
    seconds_label.after(1000, time_display)

def play_music():
    pygame.mixer.music.load(Path(working_directory, 'skins', skin_selected, 'music.mp3'))
    pygame.mixer.music.play(loops=0)



working_directory = os.path.dirname(__file__)
path_json = Path(working_directory, "settings_db.json")
settings_data = open_settings()


# COLORS - FONT STYLE
# original tkinter grey: #F0F0F0 - FYI
skin_selected = settings_data['skin_selected']                                  
selected_skin_folder = settings_data['skins'][skin_selected]

background_color = selected_skin_folder['background_color']    
field_background_color = selected_skin_folder['field_background_color'] 
font_style = selected_skin_folder['font_style']
font_color = selected_skin_folder['font_color']
window_background_color = selected_skin_folder['window_background_color']

# play_music()

# WINDOW
window = Tk()
window.configure(background=window_background_color) # FYI - not necessery / not working if the image background color is set
window.title(selected_skin_folder['window_title'])
window_width = 600
window_length = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width*0.2, screen_height*0.67))
window.resizable(0,0)   # locks the main window

# IMAGES
path_image = Path(working_directory, "skins", skin_selected, "BG.PNG")      # Path functions makes the path OS independent
backgound_image = PhotoImage(file = path_image)
backgound_image_label = Label(window, image = backgound_image)
backgound_image_label.place(x = -2, y = 0)

if platform.system() == 'Windows':      # will not be visible on Linux, macOS
    path_icon = Path(working_directory, "skins", skin_selected, "icon.ico")
    window.iconbitmap(path_icon)        # window icon - left, top corner

# TIME
hours_and_mins_label = Label(window, font=('calibri', 100, 'bold'),
            background=None,
            foreground='purple')

seconds_label = Label(window, font=('calibri', 70, 'bold'),
            background=None,
            foreground='purple')

hours_and_mins_label.place(x=50, y=50)
seconds_label.place(x=360, y=85)


time_display()

window.mainloop()