import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('nado gui')
root.geometry('320x240')


frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')
listbox = Listbox(
    frame, selectmode='extended', height=10,
    yscrollcommand=scrollbar.set # set이 없으면 안됨
)
for i in range(1, 32):
    listbox.insert(END, str(i) + 'day')

listbox.pack(side='left')

scrollbar.config(command=listbox.yview) # 매핑



root.mainloop()