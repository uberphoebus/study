from tkinter import *

root = Tk()
root.title('nado gui')
root.geometry('640x480')

# 텍스트
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, 'input') # 기본값 제공

# entry : 엔터입력 불가. 한줄로 입력 받음.
e = Entry(root, width=30)
e.pack()
e.insert(0, 'oneline')

# 가져오기
def btncmd():
    # 내용 출력
    print(txt.get('1.0', END)) # 모든 텍스트 가져옴
    print(e.get())
    
    # 기입 내용 삭제
    txt.delete('1.0', END)
    e.delete(0, END)

btn = Button(root, text='click', command=btncmd)
btn.pack()

root.mainloop()