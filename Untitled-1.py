from pygame import *
from tkinter import *
root = Tk()
q = 1000 # curently balance
q1 = 1000-500

def btn_click1():
    b1.Label.destroy()

l  = Label(root,text='Shop',font='Courier 30')
l1 = Button(root,text='pistol',font='Courier 20',command='btn_click1')
b1 = Label(root,text=q,font='courier 20')
b2 = Label(root,text='500',font='courier 30')
b2.place(x=0,y=160)
b1.place(x=1300)
l1.place(x=0,y=100)
l.pack()
root.mainloop()