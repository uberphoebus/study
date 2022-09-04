from cgitb import text
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('nado gui')
root.geometry('320x240')

def info():
    msgbox.showinfo('alr', 'comp')
    pass

def warn():
    msgbox.showwarning('wr', 'ajeofjwoiefjiowjfoi')

def error():
    msgbox.showerror('dsfasdf', 'faweiojwoeifjoi')

def okcancel():
    msgbox.askokcancel('awjeof', 'wjofjweoif')

def retcancel():
    msgbox.askretrycancel('awjeof', 'wjofjweoif')

def yesno():
    msgbox.askyesno('afjeio', 'aijeofjwfoe')

def yesnocan():
    response = msgbox.askyesnocancel(title=None, message='jfaosejfoise')
    print(response) # 예 1, 아니오 0, 그 외
    if response == 1:
        print('y')
    elif response == 0:
        print('n')
    else:
        print('can')

Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='wra').pack()
Button(root, command=error, text='err').pack()
Button(root, command=okcancel, text='ok can').pack()
Button(root, command=yesno, text='yesno').pack()
Button(root, command=yesnocan, text='yesnocan').pack()






root.mainloop()