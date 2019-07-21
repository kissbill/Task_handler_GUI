from idlelib import window
from tkinter import *
from tkinter import ttk

window = Tk()
# Menu line creation
menu = Menu(window)
window.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=window.quit)
help_menu = Menu(menu)
menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About')

# Tab control
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
lbl1 = Label(tab1, text='label1')
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='label2')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')

# Tags
v = IntVar()
Radiobutton(window, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(window, text='MIT', variable=v, value=1).pack(anchor=W)

# Input
T = Text(window, height=2, width=30)
T.pack()

# var1 = IntVar()
# Checkbutton(window, text='male', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(window, text='female', variable=var2).grid(row=1, sticky=W)

window.mainloop()
