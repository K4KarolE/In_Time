# Thank you "CodeLoop - By Ritik" for the GIF - Tkinter code:
# https://youtu.be/ZX-5XQ1Q8Zg?si=juxoU-Z9WFK-St6J

# What did we learn?
# The tkinter label generation sequence -> what will be on the top
# Not the ..label1.place(x,y), ..label2.place(x,y) sequence
# Need CANVAS to be able to display text with clear transparent background


from tkinter import Tk, PhotoImage, Canvas
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
    hours_and_mins = strftime('%H:%M')
    seconds = strftime(':%S')
    # TOP
    canvas.itemconfig(hours_and_mins_display, text=hours_and_mins)
    canvas.itemconfig(seconds_display, text=seconds)
    # BACK
    canvas.itemconfig(hours_and_mins_display_2nd, text=hours_and_mins)
    canvas.itemconfig(seconds_display_2nd, text=seconds)
    canvas.after(1000, time_display)


def load_music():
    pygame.mixer.music.load(Path(working_directory, 'skins', skin_selected, 'music.mp3'))

def play_music():
    pygame.mixer.music.play(loops=-1)       # -1: repeat

def stop_music():
    pygame.mixer.music.fadeout(1500)

def volume_music(value):
    pygame.mixer.music.set_volume(value)         # 0.0-1.0

def load_and_play():
    if  music_on:
        load_music()
        volume_music(0.2)
        play_music()


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
# TIME
time_font_color = selected_skin_folder['time_font_color']
time_hm_font = selected_skin_folder['time_hm_font']
time_sec_font = selected_skin_folder['time_sec_font']
# HOURS & MINUTES
time_hm_pos_x = selected_skin_folder['time_hm_pos_x']
time_hm_pos_y = selected_skin_folder['time_hm_pos_y']
# SECONDS
time_sec_pos_x = selected_skin_folder['time_sec_pos_x']
time_sec_pos_y = selected_skin_folder['time_sec_pos_y']

# MUSIC
music_on = settings_data['music_on']


# WINDOW
window = Tk()
# window.configure(background=window_background_color) # FYI - not necessery / not working if the image background color is set
window.title(selected_skin_folder['window_title'])
window_width = 720 + 2
window_high = 486 + 2
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_high}+%d+%d' % (screen_width*0.2, screen_height*0.6))
window.resizable(0,0)   # locks the main window

## BG GIF
path_gif = Path(working_directory, "skins", skin_selected, "GIF.GIF")
get_frames_count_all = Image.open(path_gif)
frames_count_all = get_frames_count_all.n_frames  # gives total number of frames that gif contains


images_list = [PhotoImage(file=path_gif, format=f"gif -index {i}") for i in range(frames_count_all)]  # creating list of PhotoImage objects for each frames

count = 0
anim = None
animation_speed = 80      # 1000 = 1 sec
def animation(count):
    image_next = images_list[count]
    canvas.itemconfig(image_display, image=image_next, anchor='nw')

    count += 1
    if count == frames_count_all-1:     # -1: the last frame/image is not usable, too noisy
        count = 0
    canvas.after(animation_speed, lambda :animation(count))


# BG IMAGE
# path_image = Path(working_directory, "skins", skin_selected, "BG.PNG")      # Path functions makes the path OS independent
# backgound_image = PhotoImage(file = path_image)


if platform.system() == 'Windows':      # will not be visible on Linux, macOS
    path_icon = Path(working_directory, "skins", skin_selected, "icon.ico")
    window.iconbitmap(path_icon)        # window icon - left, top corner

canvas = Canvas(window, width=window_width, height=window_high)
canvas.place(x=0,y=0)

image_display = canvas.create_image((0,0))
# BACK
re_pos = 4
hours_and_mins_display_2nd = canvas.create_text((time_hm_pos_x + re_pos, time_hm_pos_y + re_pos), text=strftime('%H:%M'), font=time_hm_font, fill='black', anchor='sw')
seconds_display_2nd = canvas.create_text((time_sec_pos_x + re_pos, time_sec_pos_y + re_pos), text=strftime(':%S'), font=time_sec_font, fill="black", anchor='sw')
# TOP
hours_and_mins_display = canvas.create_text((time_hm_pos_x, time_hm_pos_y), text=strftime('%H:%M'), font=time_hm_font, fill=time_font_color, anchor='sw')
seconds_display = canvas.create_text((time_sec_pos_x, time_sec_pos_y), text=strftime(':%S'), font=time_sec_font, fill=time_font_color, anchor='sw')

time_display()
animation(count)
load_and_play()

window.mainloop()