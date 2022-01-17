from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('nado gui')
root.geometry('320x240')

# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate')
# indeterminate 결정되지 않음
# progressbar = ttk.Progressbar(root, maximum=100, mode='determinate')
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd():
    progressbar2.stop() # 작동 중지
    pass

btn = Button(root, text='start', command=btncmd)
btn.pack()

root.mainloop()