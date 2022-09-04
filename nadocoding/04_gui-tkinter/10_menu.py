from tkinter import *

root = Tk()
root.title('nado gui')
root.geometry('320x240')

def create_new_file():
    print('new')

# file menu
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='new', command=create_new_file)
menu_file.add_command(label='wind')
menu_file.add_separator()
menu_file.add_command(label='open')
menu_file.add_separator()
menu_file.add_command(label='save all', state='disable') # 비활성화
menu_file.add_separator()
menu_file.add_command(label='exit', command=root.quit)
menu.add_cascade(label='file', menu=menu_file)

# edit menu
menu.add_cascade(label='edit')

# radio
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='py')
menu_lang.add_radiobutton(label='java')
menu_lang.add_radiobutton(label='c++')
menu.add_cascade(label='lang', menu=menu_lang)

# view
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='mini')
menu.add_cascade(label='view', menu=menu_view)


root.config(menu=menu)
root.mainloop()