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
tab_control.add(tab1, text='VERIZON')
tab_control.add(tab2, text='EPAM')
# Spacing
lbl1 = Label(tab1, text='label1', padx=5, pady=5)
lbl1.grid(column=3, row=0)
# RadioButtons
# v = IntVar()
# Radiobutton(tab1, text='GfG', variable=v, value=1).pack(anchor=W)
# Radiobutton(tab1, text='MIT', variable=v, value=1).pack(anchor=W)
var1 = IntVar()
Checkbutton(tab1, text='TestAutomate', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(tab1, text='Email', variable=var2).grid(row=1, sticky=W)

# lbl2 = Label(tab2, text='label2')
# lbl2.grid(column=0, row=0)
var1 = IntVar()
Checkbutton(tab2, text='ToDo', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(tab2, text='NeedToCheck', variable=var2).grid(row=1, sticky=W)
tab_control.pack(expand=1, fill='both')



# Input
T = Text(window, height=2, width=30)
T.pack()



window.mainloop()
