from tkinter import *

root = Tk()
root.title('nado gui')
root.geometry('320x240')

listbox = Listbox(root, selectmode='extended', height=0)
# single 단일 / extended 여러 개
# height 보여줄 개수
listbox.insert(0, 'apple')
listbox.insert(1, 'straw')
listbox.insert(2, 'ban')
listbox.insert(END, 'mel')
listbox.insert(END, 'gra')
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0) # 맨 뒤, 앞 항목 삭제
    
    # 갯수 확인
    # print('list count', listbox.size())
    
    # 항목 확인
    # print('get', listbox.get(0, 2))
    
    # 선택된 항목 확인 : 위치로 반환
    print('select', listbox.curselection())
    
    pass

btn = Button(root, text='click', command=btncmd)
btn.pack()

root.mainloop()