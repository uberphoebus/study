import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('nado gui')
root.geometry('320x240')

Label(root, text='menu select').pack(side='top')

Button(root, text='order').pack(side='bottom')

frame_burger = Frame(root, relief='solid', bd=1)
# relief 테두리 모양, bd 외곽선
frame_burger.pack(side='left', fill='both', expand=True)

Button(frame_burger, text='hamburger').pack()
Button(frame_burger, text='ch hamburger').pack()
Button(frame_burger, text='chick hamburger').pack()

frame_drink = LabelFrame(root, text='drink')
frame_drink.pack(side='right', fill='both', expand=True)
Button(frame_drink, text='cid').pack()
Button(frame_drink, text='col').pack()


root.mainloop()