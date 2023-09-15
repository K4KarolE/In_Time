# Thank you "CodeLoop - By Ritik" for the GIF - Tkinter code:
# https://youtu.be/ZX-5XQ1Q8Zg?si=juxoU-Z9WFK-St6J

# What did we learn?
# The tkinter label generation sequence -> what will be on the top
# Not the ..label1.place(x,y), ..label2.place(x,y) sequence


from tkinter import *
from time import strftime

import json
from pathlib import Path

from PIL import Image

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


def load_music():
    pygame.mixer.music.load(Path(working_directory, 'skins', skin_selected, 'music.mp3'))

def play_music():
    pygame.mixer.music.play(loops=0)

def stop_music():
    pygame.mixer.music.fadeout(1500)



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

# MUSIC
music_on = settings_data['music_on']
# if  music_on:
    # load_music()
    # play_music()

# WINDOW
window = Tk()
window.configure(background=window_background_color) # FYI - not necessery / not working if the image background color is set
window.title(selected_skin_folder['window_title'])
window_width = 800
window_length = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_length}+%d+%d' % (screen_width*0.2, screen_height*0.6))
window.resizable(0,0)   # locks the main window

# BG GIF
path_gif = Path(working_directory, "skins", skin_selected, "GIF.GIF")
get_frames_count_all = Image.open(path_gif)
frames_count_all = get_frames_count_all.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
images_list = [PhotoImage(file=path_gif, format=f"gif -index {i}") for i in range(frames_count_all)]

count = 0
anim = None
animation_speed = 50       # 1000 = 1 sec
def animation(count):
    image_next = images_list[count]
    gif_label.configure(image=image_next)
    count += 1
    if count == frames_count_all-1:     # -1: the last frame/image is not usable, too noise
        count = 0
    window.after(animation_speed, lambda :animation(count))



# BG IMAGE
path_image = Path(working_directory, "skins", skin_selected, "BG.PNG")      # Path functions makes the path OS independent
backgound_image = PhotoImage(file = path_image)



if platform.system() == 'Windows':      # will not be visible on Linux, macOS
    path_icon = Path(working_directory, "skins", skin_selected, "icon.ico")
    window.iconbitmap(path_icon)        # window icon - left, top corner

# LABELS
# IMAAGES
backgound_image_label = Label(window, image = backgound_image, borderwidth=0)
# GIF
gif_label = Label(window, borderwidth=0)
# TIME
hours_and_mins_label = Label(window, font=('calibri', 100, 'bold'),
            background='red',
            foreground='black')

seconds_label = Label(window, font=('calibri', 70, 'bold'),
            background='#420000',
            foreground='black')


## WIDGET PLACEMENT
# IMAGE
backgound_image_label.place(x = -2, y = 0)
# GIF
gif_label.place(x=0, y=0)
# TIME
hours_and_mins_label.place(x=50, y=50)
seconds_label.place(x=360, y=85)
# BUTTONS


animation(count)
time_display()

window.mainloop()