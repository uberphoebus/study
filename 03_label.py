from tkinter import *

root = Tk()
root.title('nado gui')
root.geometry('640x480')

# 레이블 : 글자만 보여주는 것
label1 = Label(root, text='안녕하세요')
label1.pack()

# 이미지
photo = PhotoImage(file='./check.png')
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text='또 만나요')
    
    global photo2 # 함수 내 변화를 유지하기 위해서는 전역변수로
    photo2 = PhotoImage(file='./check2.png')
    label2.config(image=photo2)

btn = Button(root, text='클릭',command=change)
btn.pack()

root.mainloop()