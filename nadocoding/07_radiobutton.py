from tkinter import *

root = Tk()
root.title('nado gui')
root.geometry('320x240')

# 여러 개 중에 택 1
label1 = Label(root, text='select').pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text='burger', value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text='c burger', value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text='cc burger', value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text='drink').pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text='col', value='col', variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text='si', value='si', variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()



def btncmd():
    print(burger_var.get()) # value를 반환
    print(drink_var.get()) # value를 반환
    pass

btn = Button(root, text='order', command=btncmd)
btn.pack()

root.mainloop()