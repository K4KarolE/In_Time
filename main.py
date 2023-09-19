# Thank you "CodeLoop - By Ritik" for the original GIF display - Tkinter code:
# https://youtu.be/ZX-5XQ1Q8Zg?si=juxoU-Z9WFK-St6J

# What did we learn?
# - The labels placement - the last one will be on the top
# - Need CANVAS to be able to display text with clear transparent background
# - canvas.create_text() parameters` style
# - Be able to save/hold a sequence of tkinter widgets we need class instance sequence (/docs/tkinter_fonts.py)
# - how to loop a function (animation, volume slider)


from tkinter import Tk, PhotoImage, Canvas, Button, Scale, Label
from time import strftime

from json import load, dump
from pathlib import Path

from PIL import Image
from PIL import ImageTk

import platform
import os

from pygame import mixer
mixer.init()

class Music:
    def __init__(self, on, volume):
        self.on = on
        self.volume = volume

count = 0
class Animation:
    def __init__(self, speed):
        self.speed = speed
    
    def animation_func(animation_param, count):
        image_next = images_list[count]
        canvas.itemconfig(image_display, image=image_next, anchor='nw')

        count += 1
        if count == frames_count_all*2:
            count = 0
        canvas.after(animation.speed, lambda :Animation.animation_func(animation_param, count))

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

# MUSIC
# saving the music`s ON/OFF and VOLUME parameters to DB when:
# 1.start playing 2.stop playing 3.closing the settings window
def music_load():
    mixer.music.load(Path(working_directory, 'skins', skin_selected, 'music.mp3'))

def music_play():
    music_load()
    mixer.music.set_volume(music.volume)
    mixer.music.play(loops=-1)              # -1: repeat

def music_stop():
    mixer.music.fadeout(500)
    
def music_volume_set(value):
    mixer.music.set_volume(value)         # 0.0-1.0

def load_play_music():
    if  music.on:
        music_load()
        mixer.music.set_volume(music.volume)
        mixer.music.play(loops=-1)

def music_switch_on_off():
    settings_data = open_settings()
    skin_selected = settings_data['skin_selected']                                  
    selected_skin_folder = settings_data['skins'][skin_selected]
    if settings_data['music_on']:
        music_stop()
        settings_data['music_on'] = False
        sound_button.configure(image=button_image_start)
    else:
        music_play()
        settings_data['music_on'] = True
        sound_button.configure(image=button_image_stop)
    selected_skin_folder['music_volume'] = music.volume
    save_settings(settings_data)

# IMAGE CREATION - resizable
def image_generate(image_size, picture_name):       # (24, 'icon_close.png')
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


# FONT
font_style = selected_skin_folder['font_style']
font_color = selected_skin_folder['font_color']
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

# MUSIC
music = Music(settings_data['music_on'], selected_skin_folder['music_volume'])

# ANIMATION
animation = Animation(selected_skin_folder['animation_speed'])  # 1000 = 1 sec

# CANVAS 2nd - SETTINGS
canvas_settings_orentation = selected_skin_folder['canvas_settings_orentation']
canvas_settings_pos_x_diff = selected_skin_folder['canvas_settings_pos_x_diff']

# WINDOW
window = Tk()
window.title(selected_skin_folder['window_title'])
window_width = 720 + 2
window_high = 486 + 2
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{window_width}x{window_high}+%d+%d' % (screen_width/2, screen_height-window_high-80))
window.resizable(0,0)   # locks the main window
# CANVAS
canvas = Canvas(window, width=window_width, height=window_high)
canvas.place(x=0,y=0)
image_display = canvas.create_image((0,0))

## ANIMATION
def img_seq_creation():
    path_gif = Path(working_directory, 'skins', skin_selected, 'GIF.GIF')
    get_frames_count_all = Image.open(path_gif)
    frames_count_all = get_frames_count_all.n_frames
    # images_list = [PhotoImage(file=path_gif, format=f"gif -index {i}") for i in range(frames_count_all)]
    # # original code snippet - creating list of PhotoImage objects for each frames

    images_list = []
    [images_list.append(t) for t in range(frames_count_all*2)]
    for i in range(frames_count_all):
        images_list[i] = PhotoImage(file=path_gif, format=f'gif -index {i}')
        images_list[(frames_count_all*2-1)-i] = PhotoImage(file=path_gif, format=f'gif -index {i}')
    return images_list, frames_count_all
    # the returning part of the animation coming from:
    # allocating the same image object for 2 mirrored position in the list
    # -> half size GIF, faster load time

images_list, frames_count_all = img_seq_creation()


# WINDOW ICON - left, top corner - window loading better when this is after animation section
if platform.system() == 'Windows':      # will not be visible on Linux, macOS
    path_icon = Path(working_directory, 'skins', skin_selected, 'icon.ico')
    window.iconbitmap(path_icon)

## TIME
re_pos = 4  # for the "shadow"
# BACK
# anchor = se/sw -> changing time size(11<55): will no overlapping or too far from eachother
hours_and_mins_display_2nd = canvas.create_text(
    (time_hm_pos_x + re_pos, time_hm_pos_y + re_pos),
    text=strftime('%H:%M'),
    font=(time_font_style, time_hm_font_size, 'bold'),
    fill='black',
    anchor='se')
seconds_display_2nd = canvas.create_text(
    (time_sec_pos_x + re_pos, time_sec_pos_y + re_pos),
    text=strftime(':%S'),
    font=(time_font_style, time_sec_font_size, 'bold'),
    fill='black',
    anchor='sw')
# TOP
hours_and_mins_display = canvas.create_text(
    (time_hm_pos_x, time_hm_pos_y),
    text=strftime('%H:%M'),
    font=(time_font_style, time_hm_font_size, 'bold'),
    fill=time_font_color,
    anchor='se')
seconds_display = canvas.create_text(
    (time_sec_pos_x, time_sec_pos_y),
    text=strftime(':%S'),
    font=(time_font_style, time_sec_font_size, 'bold'),
    fill=time_font_color,
    anchor='sw')

## BUTTONS
pos_y_diff = 33

# SETTINGS BUTTON
button_image_settings = image_generate(21, 'icon_settings.png')
settings_button = Button(canvas, text = 'test',
            command=lambda:[display_canvas_settings()], 
            image = button_image_settings,
            background=button_bg_color,
            activebackground=button_bg_color_clicked)
settings_button.place(x=button_pos_x, y=button_pos_y)

# SOUND BUTTON
button_image_start = image_generate(20, 'icon_start.png')
button_image_stop = image_generate(20, 'icon_stop.png')
if music.on:
    music_start_stop_img = button_image_stop
else:
    music_start_stop_img = button_image_start
sound_button = Button(canvas, text = 'test',
            command=lambda:[music_switch_on_off()], 
            image = music_start_stop_img,
            background=button_bg_color,
            activebackground=button_bg_color_clicked)
sound_button.place(x=button_pos_x, y=button_pos_y + pos_y_diff)


## CANVAS 2nd - SETTINGS
def display_canvas_settings():
    # CANVAS
    canvas_settings_width = 300
    canvas_settings_height = 250
    canvas_settings = Canvas(
        window,
        background=button_bg_color,
        highlightthickness=2,
        highlightbackground=button_bg_color_clicked,
        width=canvas_settings_width,
        height=canvas_settings_height)
    
    canvas_settings.place(
        x=button_pos_x+canvas_settings_pos_x_diff,
        y=button_pos_y,
        anchor=canvas_settings_orentation)
    
    # CLOSE BUTTON
    close_button = Button(canvas_settings,
        text='X',
        image=button_image_close,
        command=lambda:[close_canvas_settings()],
        background=button_bg_color,
        activebackground=button_bg_color_clicked)
    close_button.place(x=canvas_settings_width-30, y=15)

    # VOLUME IMAGE
    image_volume_label = Label(canvas_settings,image=image_volume, background=button_bg_color)
    image_volume_label.place(x=15, y=30)

    # VOLUME SLIDER
    volume_slider = Scale(
        canvas_settings,
        from_=0,
        to=10,
        length=190,
        width=10,
        background=button_bg_color,
        activebackground=button_bg_color,
        troughcolor=button_bg_color_clicked,
        highlightthickness=0,
        orient='horizontal',
        showvalue=False
        )
    volume_slider.set(music.volume*10)
    volume_slider.place(x=60, y=40)
    def volume_slider_update(music_volume_param):       # update volume, when there is a change in slider position/value
        volume_slider_value = volume_slider.get()/10
        if volume_slider_value != music_volume_param:   # checking any change in volume      
            music_volume_set(volume_slider_value)
            music_volume_param = volume_slider_value
            music.volume = volume_slider_value
        canvas_settings.after(50, lambda:volume_slider_update(music_volume_param))    # 1000 = 1 sec
    
    volume_slider_update(music.volume)

    # ANIMATION SPEED SLIDER
    animation_slider = Scale(
        canvas_settings,
        from_=10,
        to=200,
        length=190,
        width=10,
        background=button_bg_color,
        activebackground=button_bg_color,
        troughcolor=button_bg_color_clicked,
        highlightthickness=0,
        orient='horizontal',
        showvalue=False
        )
    animation_slider.set(animation.speed)
    animation_slider.place(x=60, y=90)

    def animation_speed_update():
        animation.speed=animation_slider.get()
        canvas_settings.after(50, lambda:animation_speed_update())
    
    animation_speed_update()

    # CLOSE CANVAS
    def close_canvas_settings():
        # SAVE VOLUME, ANIMATION SPEED
        settings_data = open_settings()
        skin_selected = settings_data['skin_selected']
        selected_skin_folder = settings_data['skins'][skin_selected]
        selected_skin_folder['music_volume'] = music.volume
        selected_skin_folder['animation_speed'] = animation.speed
        save_settings(settings_data)
        # CLOSE CANVAS
        canvas_settings.destroy()

# IMAGE GENERATION
image_volume = image_generate(30, 'icon_volume.png')
button_image_close = image_generate(15, 'icon_close.png')

## FUNCTIONS
time_display()
Animation.animation_func(animation.speed, count)
load_play_music()

window.mainloop()