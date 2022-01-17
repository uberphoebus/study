from tkinter import *

root = Tk()
root.title('nado gui')
root.geometry('320x240')

chkvar = IntVar() # 정수형으로 값을 저장
chkbox = Checkbutton(root, text='not today', variable=chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text='not week', variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0일 때는 체크 해제, 1일 때 체크
    print(chkvar2.get())
    pass

btn = Button(root, text='click', command=btncmd)
btn.pack()

root.mainloop()