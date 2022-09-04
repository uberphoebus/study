from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title('nado gui')
root.geometry('320x240')

# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate')
# indeterminate 결정되지 않음
# progressbar = ttk.Progressbar(root, maximum=100, mode='determinate')
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=10, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 11):
        time.sleep(1)
        p_var2.set(i) # 프로그레스 바의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text='start', command=btncmd2)
btn.pack()

root.mainloop()