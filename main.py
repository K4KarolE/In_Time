
from tkinter import *
from time import strftime

import json
from pathlib import Path



def open_settings():
    f = open(path_json)
    settings_data = json.load(f)
    return settings_data

def save_settings(settings_data):
    with open(path_json, 'w') as f:
        json.dump(settings_data, f, indent=2)
    return

def time_display():
    hours_and_mins = strftime('%H:%M')
    hours_and_mins_label.config(text=hours_and_mins)
    hours_and_mins_label.after(1000, time_display)

    seconds = strftime(':%S')
    seconds_label.config(text=seconds)
    seconds_label.after(1000, time_display)

path_json = Path("settings_db.json")
settings_data = open_settings()
skin_selected = settings_data['skin_selected']
 
 
window = Tk()
# window.configure(background=window_background_color) FYI - not necessery / not working if the image background color is set
window.title(settings_data['skins'][skin_selected]['window_title'])
window_width = 600
window_length = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width*0.2, screen_height*0.67))
window.resizable(0,0)   # locks the main window

hours_and_mins_label = Label(window, font=('calibri', 100, 'bold'),
            background=None,
            foreground='purple')

seconds_label = Label(window, font=('calibri', 80, 'bold'),
            background=None,
            foreground='purple')

hours_and_mins_label.place(x=50, y=50)
seconds_label.place(x=360, y=75)
time_display()

window.mainloop()