from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('nado gui')
root.geometry('320x240')

# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate')
# indeterminate 결정되지 않음
progressbar = ttk.Progressbar(root, maximum=100, mode='determinate')
progressbar.start(10) # 10ms 마다 움직임
progressbar.pack()





def btncmd():
    pass

btn = Button(root, text='order', command=btncmd)
btn.pack()

root.mainloop()