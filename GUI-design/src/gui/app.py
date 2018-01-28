from Tkinter import *


def resize(ev=None):
    label.config(font='Helvetica -%d bold' % \
                 scale.get())


top = Tk()
top.geometry('550x350')

label = Label(top, text='hello', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=0, to=100, orient=HORIZONTAL, command=resize)
scale.set(30)
scale.pack(fill=X, expand=1)

quit = Button(top, text='Quit', command=top.quit, activeforeground='white',
              activebackground='red')
quit.pack()

mainloop()
