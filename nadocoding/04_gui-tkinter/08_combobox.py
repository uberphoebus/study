from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('nado gui')
root.geometry('320x240')

values = [str(i) + '일' for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('card') # 최초목록 제목 설정

values = [str(i) + '일' for i in range(1, 32)]
readonly_combobox = ttk.Combobox(root, height=5, values=values, state='readonly')
readonly_combobox.current(0) # 0 인덱스 선택
readonly_combobox.pack()




def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())
    pass

btn = Button(root, text='order', command=btncmd)
btn.pack()

root.mainloop()