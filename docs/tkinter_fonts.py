'''
Tkinter fonts
Original from jimmiesrustled - Thank you mate!
https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter

Just made it clickable
'''

from tkinter import Tk, font, Canvas, Frame, Scrollbar, Button
import pyperclip


class Buttons():
    def __init__(self, text):
        self.text = text
    
    def create(self):
        return Button(frame,
                     text = self.text,
                     font = (self.text, 20),
                     command=lambda:[pyperclip.copy(self.text)]
                     )

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))


root = Tk()
root.title('Font Families')
fonts=list(font.families())
fonts.sort()

canvas = Canvas(root, borderwidth=0, background="#ffffff", width=400, height=800)
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")
frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

counter = 0
buttons_list = []
for item in fonts:
    buttons_list.append(Buttons(item).create())
    buttons_list[counter].pack()
    counter += 1

root.mainloop()