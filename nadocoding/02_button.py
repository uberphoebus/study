from tkinter import *

root = Tk()
root.title('nado gui')

btn1 = Button(root, text='버튼1')
btn1.pack() # 창에 표시

btn2 = Button(root, padx=5, pady=10, text='버튼2222222')
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text='버튼3')
btn3.pack()

btn4 = Button(root, width=10, height=3, text='버튼4')
btn4.pack()

# pad는 텍스트의 내용에 더한 여백의 크기
# width, height는 절대 크기

btn5 = Button(root, fg='red', bg='yellow', text='버튼5')
btn5.pack()

# 버튼에 이미지 넣기
photo = PhotoImage(file='./check.png')
btn6 = Button(root, image=photo)
btn6.pack()

# 버튼 동작
def btncmd():
    print('버튼이 클릭되었어요')

btn7 = Button(root, text='동작하는 버튼', command=btncmd)
btn7.pack()

root.mainloop() # 창이 닫히지 않는 루프