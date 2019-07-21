from tkinter import *

root = Tk()
# Menu line creation
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)
help_menu = Menu(menu)
menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About')

# Tags
v = IntVar()
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)

# Input
T = Text(root, height=2, width=30)
T.pack()

mainloop()
