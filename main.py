''' 
What did we learn?
- The labels placement - the last one will be on the top
- Need CANVAS to be able to display text with clear transparent background
- Canvas.create_text() parameters` style
- Be able to save/hold a sequence of tkinter widgets we need class instance sequence (/docs/tkinter_fonts.py)
- How to loop a function (time display, volume and animation speed)
 - Cancel callbacks - destroying window with recursive functions like above (/docs/cancel_callbacks.py)
- default_button = Button(window, ..).place(x,y) --> NO default_button.configure option
    + widget creation and placement need to be seperate: 
    + default_button = Button(window, ..), default_button.place(x,y) --> default_button.configure
'''


from tkinter import Tk, PhotoImage, Canvas, Button, Scale, Label, OptionMenu, StringVar

from time import strftime
from json import load, dump
from pathlib import Path
import platform

from PIL import Image
from PIL import ImageTk

from pygame import mixer


class Music:
    def __init__(self, on, volume):
        self.on = on
        self.volume = volume

class Animation:
    def __init__(self, speed):
        self.speed = speed
    
class Params:
    def __init__(self, value):
        self.value = value


def open_settings():
    f = open(path_json)
    settings_data = load(f)
    return settings_data

def save_settings(settings_data):
    with open(path_json, 'w') as f:
        dump(settings_data, f, indent=2)
    return


# DIRECTORY AND JSON PATH
working_directory = Path(__file__).parent
path_json = Path(working_directory, 'settings_db.json')

# MIXER
mixer.init()



# MAIN
def main():

    def load_info():
        settings_data = open_settings()
        skin_selected = settings_data['skin_selected']                                  
        selected_skin_folder = settings_data['skins'][skin_selected]
        return settings_data, skin_selected, selected_skin_folder


    def time_display():
        # TIME
        hours_and_mins = strftime('%H:%M')
        seconds = strftime(':%S')
        # TOP
        canvas.itemconfig(hours_and_mins_display, text=hours_and_mins)
        canvas.itemconfig(seconds_display, text=seconds)
        # BACK - "SHADOW"
        canvas.itemconfig(hours_and_mins_display_2nd, text=hours_and_mins)
        canvas.itemconfig(seconds_display_2nd, text=seconds)
        # CALLBACK
        canvas.after(1000, lambda:time_display())


    # MUSIC
    def music_stop():
        mixer.music.fadeout(0)


    def music_load_play():
        mixer.music.load(Path(working_directory, 'skins', skin_selected, 'music.mp3'))
        mixer.music.set_volume(music.volume)
        mixer.music.play(loops=-1)


    def music_switch_on_off():
        
        settings_data, skin_selected, selected_skin_folder = load_info()
        
        # MUSIC ON --> OFF
        if settings_data['music_on']:
            music_stop()
            settings_data['music_on'] = False
            sound_button.configure(image=button_image_start)

        # MUSIC OFF --> ON
        else:
            music_load_play()
            settings_data['music_on'] = True
            sound_button.configure(image=button_image_stop)

        selected_skin_folder['music_volume'] = music.volume
        save_settings(settings_data)


    # IMAGE CREATION - resizable
    def image_generate(image_size, picture_name):   # (24, 'icon_close.png')
        my_img_path = Path(working_directory, 'skins', '_icons', picture_name)
        my_img = Image.open(my_img_path)
        width = int(image_size)
        height = int(image_size)
        resized_image = my_img.resize((width, height))
        photo = ImageTk.PhotoImage(resized_image)
        return photo

    
    # JSON / SETTINGS / SKIN - LOAD INFO
    settings_data, skin_selected, selected_skin_folder = load_info()

    # MUSIC
    music = Music(settings_data['music_on'], selected_skin_folder['music_volume'])

    # ANIMATION
    count = 0
    animation = Animation(selected_skin_folder['animation_speed'])  # 1000 = 1 sec

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
    canvas = Canvas(
        window,
        width=window_width,
        height=window_high)
    canvas.place(x=0,y=0)
    # BASE IMAGE FOR ANIMATION
    image_display = canvas.create_image((0,0))


    # ANIMATION
    def img_seq_creation():
        path_gif = Path(working_directory, 'skins', skin_selected, 'GIF.GIF')
        get_frames_count_all = Image.open(path_gif)
        frames_count_all = get_frames_count_all.n_frames
        # images_list = [PhotoImage(file=path_gif, format=f"gif -index {i}") for i in range(frames_count_all)]
        # # prev.line = original code snippet - creating list of PhotoImage objects for each frames

        images_list = []
        [images_list.append(t) for t in range(frames_count_all*2)]
        for i in range(frames_count_all):
            images_list[i] = PhotoImage(file=path_gif, format=f'gif -index {i}')
            images_list[(frames_count_all*2-1)-i] = PhotoImage(file=path_gif, format=f'gif -index {i}')
        return images_list, frames_count_all
        # the returning part of the animation coming from:
        # allocating the same image object for 2 mirrored position in the list
        # -> half size GIF enough, faster load time
    
    images_list, frames_count_all = img_seq_creation()


    def animation_func(animation_param, count):
        image_next = images_list[count]
        canvas.itemconfig(image_display, image=image_next, anchor='nw')
        count += 1
        if count == frames_count_all*2:
            count = 0
        # CALLBACK
        canvas.after(animation.speed, lambda:animation_func(animation_param, count))



    # WINDOW ICON - left, top corner - better window load time when this is after animation section
    if platform.system() == 'Windows':      # will not be visible on Linux, macOS
        path_icon = Path(working_directory, 'skins', skin_selected, 'icon.ico')
        window.iconbitmap(path_icon)


    ## TIME
    re_pos = 4  # for the "shadows"
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


    ## BUTTONS - ON THE MAIN WINDOW
    pos_y_diff = 33

    # SETTINGS BUTTON
    button_image_settings = image_generate(21, 'icon_settings.png')
    Button(
        canvas,
        command=lambda:[canvas_launcher()], 
        image = button_image_settings,
        background=button_bg_color,
        activebackground=button_bg_color_clicked
        ).place(x=button_pos_x, y=button_pos_y)


    # MUSIC BUTTON
    button_image_start = image_generate(20, 'icon_start.png')
    button_image_stop = image_generate(20, 'icon_stop.png')
    if music.on:
        music_start_stop_img = button_image_stop
    else:
        music_start_stop_img = button_image_start
    sound_button = Button(canvas,
                text='sound',
                command=lambda:[music_switch_on_off()], 
                image = music_start_stop_img,
                background=button_bg_color,
                activebackground=button_bg_color_clicked)
    sound_button.place(x=button_pos_x, y=button_pos_y + pos_y_diff)



    '''
    CANVAS - FOR THE SETTINGS WINDOW, TRIGGERED BY THE SETTINGS BUTTON
    '''
    # CANVAS COUNTER, LAUNCHER
    canvas_launched = Params(False)
    def canvas_launcher():      # command of the SETTINGS button
        if canvas_launched.value:
            pass
        else:
            display_canvas_settings()
            canvas_launched.value = True


    # DISPLAY CANVAS
    def display_canvas_settings():
        # CANVAS
        canvas_settings_width = 300
        canvas_settings_height = 185
        canvas_settings = Canvas(
            window,
            background=button_bg_color,
            highlightthickness=3,
            highlightbackground='black',
            width=canvas_settings_width,
            height=canvas_settings_height)
        canvas_settings.place(
            x=button_pos_x+canvas_settings_pos_x_diff,
            y=button_pos_y-3,
            anchor=canvas_settings_orentation)
        

        # CLOSE BUTTON
        Button(
            canvas_settings,
            image=button_image_close,
            command=lambda:[close_canvas_settings()],
            background=button_bg_color,
            activebackground=button_bg_color_clicked
            ).place(x=canvas_settings_width-30, y=15)



        ## SLIDERS
        slider_width = 13
        # VOLUME SLIDER
        volume_slider = Scale(
            canvas_settings,
            from_=0,
            to=10,
            length=190,
            width=slider_width,
            background=button_bg_color,
            activebackground=button_bg_color,
            troughcolor=button_bg_color_clicked,
            highlightthickness=0,
            orient='horizontal',
            showvalue=False
            )
        volume_slider.set(music.volume*10)
        volume_slider.place(x=60, y=40)


        def volume_slider_update(music_volume_param):       
            # GET LATEST VALUE
            volume_slider_value = volume_slider.get()/10
            
            # UPDATE VOLUME, WHEN THERE IS A CHANGE IN SLIDER POSITION/VALUE
            if volume_slider_value != music_volume_param:     
                mixer.music.set_volume(volume_slider_value)
                music_volume_param = volume_slider_value
                music.volume = volume_slider_value
            
            # CALLBACK
            canvas_settings.after(50, lambda: volume_slider_update(music_volume_param))    # 1000 = 1 sec
        
        volume_slider_update(music.volume)

        
        # ANIMATION SPEED SLIDER
        animation_slider = Scale(
            canvas_settings,
            from_=200,
            to=10,
            length=190,
            width=slider_width,
            background=button_bg_color,
            activebackground=button_bg_color,
            troughcolor=button_bg_color_clicked,
            highlightthickness=0,
            orient='horizontal',
            showvalue=False)
        animation_slider.set(animation.speed)
        animation_slider.place(x=60, y=90)

        def animation_speed_update():
            animation.speed=animation_slider.get()
            # CALLBACK
            canvas_settings.after(50, lambda:animation_speed_update())
        
        animation_speed_update()


        # CHANGE SKIN, TRIGGERED BY THE SKIN OPTIONMENU SELECTION
        def change_skin(__):
            for selected_title in skins_dic:
                
                # SELECTED TITLE(Back to the Future I.) --> FOLDER NAME(back_to_the_future) = skin_selected
                if skins_dic[selected_title] == skins_roll_down_clicked.get():
                    
                    # LOAD INFO
                    settings_data, skin_selected, selected_skin_folder = load_info()
                    
                    # SAVING CURRENT SETTINGS AND THE NEWLY SELECTED SKIN
                    selected_skin_folder['music_volume'] = music.volume
                    selected_skin_folder['animation_speed'] = animation.speed
                    settings_data['skin_selected'] = music.on
                    settings_data['skin_selected'] = selected_title
                    save_settings(settings_data)
                    
                    # CANCEL MUSIC, WINDOW
                    music_stop()
                    window.destroy()
                    
                    # CANCEL CALLBACKS - time, volume, animation
                    for after_id in window.eval('after info').split():
                        window.after_cancel(after_id)
                    
                    # RELAUNCH MAIN
                    main()


        ## SKINS - OPTION MENU - ROLL DOWN MENU
        # SKINS DIC.
        skins_dic = {'back_to_the_future': 'Back to the Future I.',
                    'donnie_darko': 'Donnie Darko',
                    'idiocracy': 'Idiocracy',
                    'terminator': 'Terminator I.'}
        
        # LIST OF MOVIE TITLES
        skins_options = [i for i in skins_dic.values()]
        
        # OPTION MENU
        skins_roll_down_clicked = StringVar()
        skins_roll_down_clicked.set(skins_dic[skin_selected])
        skins_roll_down = OptionMenu(
            canvas_settings,
            skins_roll_down_clicked,
            *skins_options,
            command=change_skin)
        
        # ROLL DOWN - BUTTON
        skins_roll_down.configure(
            font=(None, 10, 'bold'),
            foreground=button_bg_color_clicked,
            activeforeground = button_bg_color,
            background=button_bg_color,
            activebackground=button_bg_color_clicked,
            highlightbackground=button_bg_color)
        
        # ROLL DOWN - MENU
        skins_roll_down['menu'].configure(
            font=(None, 10, 'bold'),
            activeborderwidth=9,
            foreground=button_bg_color_clicked,
            activeforeground=button_bg_color,
            background=button_bg_color,
            activebackground=button_bg_color_clicked)
        skins_roll_down.place(x=60, y=130)


        # CLOSE CANVAS
        def close_canvas_settings():
            settings_data, skin_selected, selected_skin_folder = load_info()
            selected_skin_folder['music_volume'] = music.volume
            selected_skin_folder['animation_speed'] = animation.speed
            save_settings(settings_data)
            canvas_launched.value = False
            canvas_settings.destroy()
        

        ## DISPLAY IMAGES
        # VOLUME IMAGE
        Label(canvas_settings,image=image_volume, background=button_bg_color).place(x=15, y=30)
        
        # ANIMATION SPEED IMAGE
        Label(canvas_settings,image=image_animation_speed, background=button_bg_color).place(x=15, y=80)

        # SKIN SWITCH IMAGE
        Label(canvas_settings,image=image_skin_switch, background=button_bg_color).place(x=13, y=125)


    # IMAGE GENERATION FOR SETTINGS WINDOW(CANVAS)
    image_volume = image_generate(30, 'icon_volume.png')
    image_animation_speed = image_generate(30, 'icon_animation_speed.png')
    image_skin_switch = image_generate(37, 'icon_skin_switch.png')
    button_image_close = image_generate(15, 'icon_close.png')


    # FUNCTIONS
    time_display()
    animation_func(animation.speed, count)
    if music.on: music_load_play()
    

    window.mainloop()


if __name__ == "__main__":
    main()