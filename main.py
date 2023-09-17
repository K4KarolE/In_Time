# Thank you "CodeLoop - By Ritik" for the original GIF display - Tkinter code:
# https://youtu.be/ZX-5XQ1Q8Zg?si=juxoU-Z9WFK-St6J

# What did we learn?
# - The labels placement - the last one will be on the top
# - Need CANVAS to be able to display text with clear transparent background
# - Be able to save/hold a sequence of tkinter widgets we need class instance sequence (/docs/tkinter_fonts.py)


from tkinter import Tk, PhotoImage, Canvas, Button
from time import strftime

from json import load, dump
from pathlib import Path

from PIL import Image
from PIL import ImageTk

import platform
import os

from pygame import mixer
mixer.init()



def open_settings():
    f = open(path_json)
    settings_data = load(f)
    return settings_data

def save_settings(settings_data):
    with open(path_json, 'w') as f:
        dump(settings_data, f, indent=2)
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

def music_load():
    mixer.music.load(Path(working_directory, 'skins', skin_selected, 'music.mp3'))

def music_play():
    music_load()
    mixer.music.set_volume(music_volume)
    mixer.music.play(loops=-1)              # -1: repeat

def music_stop():
    mixer.music.fadeout(500)
    
def music_volume_set(value):
    mixer.music.set_volume(value)         # 0.0-1.0

def load_play_music():
    if  music_on:
        music_load()
        mixer.music.set_volume(music_volume)
        mixer.music.play(loops=-1)

def music_switch():
    settings_data = open_settings()
    if settings_data['music_on']:
        music_stop()
        settings_data['music_on'] = False
        save_settings(settings_data)
        sound_button.configure(image=button_image_start)
    else:
        music_play()
        settings_data['music_on'] = True
        save_settings(settings_data)
        sound_button.configure(image=button_image_stop)

def button_image(image_size, picture_name):       # (24, 'icon_close.png')
    my_img_path = Path(working_directory, 'skins', '_icons', picture_name)
    my_img = Image.open(my_img_path)
    width = int(image_size)
    height = int(image_size)
    resized_image = my_img.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo


# JSON / SETTINGS
working_directory = os.path.dirname(__file__)
path_json = Path(working_directory, 'settings_db.json')
settings_data = open_settings()
skin_selected = settings_data['skin_selected']                                  
selected_skin_folder = settings_data['skins'][skin_selected]

# COLORS - FONT STYLE
# original tkinter grey: #F0F0F0 - FYI
background_color = selected_skin_folder['background_color']    
field_background_color = selected_skin_folder['field_background_color'] 
font_style = selected_skin_folder['font_style']
font_color = selected_skin_folder['font_color']
window_background_color = selected_skin_folder['window_background_color']
icon_bg_color = selected_skin_folder['icon_bg_color']
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
music_volume = settings_data['music_volume']
# ANIMATION
animation_speed = selected_skin_folder['animation_speed']  # 1000 = 1 sec

# WINDOW
window = Tk()
window.title(selected_skin_folder['window_title'])
window_width = 720 + 2
window_high = 486 + 2
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_high}+%d+%d' % (screen_width*0.2, screen_height*0.6))
window.resizable(0,0)   # locks the main window
# CANVAS
canvas = Canvas(window, width=window_width, height=window_high)
canvas.place(x=0,y=0)
image_display = canvas.create_image((0,0))

## ANIMATION
path_gif = Path(working_directory, 'skins', skin_selected, 'GIF.GIF')
get_frames_count_all = Image.open(path_gif)
frames_count_all = get_frames_count_all.n_frames  # gives total number of frames that gif contains
# images_list = [PhotoImage(file=path_gif, format=f"gif -index {i}") for i in range(frames_count_all)]
# # original code snippet - creating list of PhotoImage objects for each frames

# the returning part of the animation coming from:
# allocating the same image object for 2 mirrored position in the list
# -> smaller GIF, faster load time
images_list = []
[images_list.append(t) for t in range(frames_count_all*2)]
for i in range(frames_count_all):
    images_list[i] = PhotoImage(file=path_gif, format=f'gif -index {i}')
    images_list[(frames_count_all*2-1)-i] = PhotoImage(file=path_gif, format=f'gif -index {i}')

count = 0
anim = None
def animation(count):
    image_next = images_list[count]
    canvas.itemconfig(image_display, image=image_next, anchor='nw')

    count += 1
    if count == frames_count_all*2:
        count = 0
    canvas.after(animation_speed, lambda :animation(count))

# WINDOW ICON - left, top corner - window loading better when this is after animation section
if platform.system() == 'Windows':      # will not be visible on Linux, macOS
    path_icon = Path(working_directory, 'skins', skin_selected, 'icon.ico')
    window.iconbitmap(path_icon)

## TIME
re_pos = 4  # for the "shadow"
# BACK
# anchor = se/sw -> changing time size(11<55): will no overlapping or too far from eachother
hours_and_mins_display_2nd = canvas.create_text((time_hm_pos_x + re_pos, time_hm_pos_y + re_pos), text=strftime('%H:%M'), font=time_hm_font, fill='black', anchor='se')
seconds_display_2nd = canvas.create_text((time_sec_pos_x + re_pos, time_sec_pos_y + re_pos), text=strftime(':%S'), font=time_sec_font, fill='black', anchor='sw')
# TOP
hours_and_mins_display = canvas.create_text((time_hm_pos_x, time_hm_pos_y), text=strftime('%H:%M'), font=time_hm_font, fill=time_font_color, anchor='se')
seconds_display = canvas.create_text((time_sec_pos_x, time_sec_pos_y), text=strftime(':%S'), font=time_sec_font, fill=time_font_color, anchor='sw')

# SOUND BUTTON
button_image_start = button_image(20, 'start.png')
button_image_stop = button_image(20, 'stop.png')
if music_on:
    music_start_stop_img = button_image_stop
else:
    music_start_stop_img = button_image_start
sound_button = Button(canvas, text = 'test',
            command=lambda:[music_switch()], 
            image = music_start_stop_img,
            background=icon_bg_color)
sound_button.place(x=window_width-50, y=50)

# FUNCTIONS
time_display()
animation(count)
load_play_music()

window.mainloop()