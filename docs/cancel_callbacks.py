# Thank you j_4321 for your answer / original script
# https://stackoverflow.com/questions/63628566/how-to-handle-invalid-command-name-error-while-executing-after-script-in-tk


from tkinter import Tk, IntVar, Label, Button

# CALLBACK FUNCTIONS
def callback_1():     
    var.set(var.get() + 1)
    root.after(1000, callback_1)
                    
n = 0
def callback_2(n):
    print('Random text', n)
    n += 1
    root.after(1000, lambda: callback_2(n))


# This is what you need - above and below can be ignored
# Cancel all scheduled callbacks and quit
def quit():
    for after_id in root.eval('after info').split():
        root.after_cancel(after_id)
    root.destroy()

# WINDOW - LOOP
root = Tk()
root.pack_propagate(False)

## LOOPS
# PRINT IN WINDOW
var = IntVar()   # tkinter class instance -> global
Label(root, textvariable=var).pack()


# PRINT IN CONSOLE
dipp = Button(root, text='Q', command=lambda:quit()).pack()

# FUNCTIONS
callback_1()
callback_2(n)
# root.protocol('WM_DELETE_WINDOW', quit) looks unnecessary - from the original post
root.mainloop()
