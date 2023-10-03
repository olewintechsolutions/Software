from tkinter import *
from tkinter.ttk import *
import os
import ctypes
import pathlib
from tkinter import Tk, Button, filedialog


import tkinter as tk

ctypes.windll.shcore.SetProcessDpiAwareness(True)

main_window = Tk()
main_window.title('Electro-Magnetic Forward Modelling')
main_window.geometry("1000x800")
#win_image = PhotoImage(file="logo.png")
#main_window.iconphoto(False,win_image)

main_window.grid_columnconfigure(1, weight=1)
main_window.grid_rowconfigure(1, weight=1)


menubar = Menu(main_window)
main_window.config(menu=menubar)























def open_file():
   print("Opening file...")

def save_file():
   print("Saving file...")

def cut_text():
   print("Cutting text...")

def copy_text():
   print("Copying text...")

def paste_text():
   print("Pasting text...")



def my_child():
    mini_window = Tk()
    mini_window.title("About EM Tool")
    mini_window.geometry("900x600")
    text = Message(mini_window,text = "Welcome to Em Tool")
    text.pack()
    mini_window.mainloop()
def change_theme():
   current_bg = main_window.cget("bg")
   new_bg = "white" \
       if current_bg == "black" \
       else "black"
   main_window.configure(bg=new_bg)


def pathChange(*event):
    # Get all Files and Folders from the given Directory
    directory = os.listdir(currentPath.get())
    # Clearing the list
    list.delete(0, END)
    # Inserting the files and directories into the list
    for file in directory:
        list.insert(0, file)

def changePathByClick(event=None):
    # Get clicked item.
    picked = list.get(list.curselection()[0])
    # get the complete path by joining the current path with the picked item
    path = os.path.join(currentPath.get(), picked)
    # Check if item is file, then open it
    if os.path.isfile(path):
        print('Opening: '+path)
        os.startfile(path)
    # Set new path, will trigger pathChange function.
    else:
        currentPath.set(path)

def goBack(event=None):
    # get the new path
    newPath = pathlib.Path(currentPath.get()).parent
    # set it to currentPath
    currentPath.set(newPath)
    # simple message
    print('Going Back')


def open_popup():
    global top
    top = Toplevel(main_window)
    top.geometry("250x150")
    top.resizable(False, False)
    top.title("Child Window")
    top.columnconfigure(0, weight=1)
    Label(top, text='Enter File or Folder name').grid()
    Entry(top, textvariable=newFileName).grid(column=0, pady=50, sticky='NSEW')
    Button(top, text="Create", command=newFileOrFolder).grid(pady=50, sticky='NSEW')

def newFileOrFolder():
    # check if it is a file name or a folder
    if len(newFileName.get().split('.')) != 1:
        open(os.path.join(currentPath.get(), newFileName.get()), 'w').close()
    else:
        os.mkdir(os.path.join(currentPath.get(), newFileName.get()))
    # destroy the top
    top.destroy()
    pathChange()

top = ''
# String variables
newFileName = StringVar(main_window, "File.dot", 'new_name')
currentPath = StringVar(
    main_window,
    name='currentPath',
    value=pathlib.Path.cwd()
)
currentPath.trace('w', pathChange)


Button(main_window, text='Folder Up', command=goBack).grid(
    sticky='NSEW', column=0, row=0
)

# Keyboard shortcut for going up
main_window.bind("<Alt-Up>", goBack)
Entry(main_window, textvariable=currentPath).grid(
    sticky='NSEW', column=1, row=0, ipady=10, ipadx=10
)


# List of files and folder
list = Listbox(main_window)
list.grid(sticky='NSEW', column=1, row=1, ipady=10, ipadx=10)
list.bind('<Double-1>', changePathByClick)
list.bind('<Return>', changePathByClick)



fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)


fileMenu.add_command(label="File", command=pathChange)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Open Folder")
fileMenu.add_command(label="Import file" , command=open_popup)
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As")
fileMenu.add_command(label="Print ")
fileMenu.add_command(label="Copy file")
fileMenu.add_separator()
fileMenu.add_command(label="Exit EM Tool", command=main_window.quit, accelerator="Ctrl+Q")



editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)

viewMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label ="View", menu = viewMenu)
viewMenu.add_command(label='Topology')
viewMenu.add_command(label='Recent files')


sub_menu = Menu(viewMenu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts', command=change_theme)
sub_menu.add_command(label='Color Themes', command=change_theme)

# add the File menu to the menubar
viewMenu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

aboutMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='About', menu = aboutMenu)
aboutMenu.add_command(label='What is Modelling')
aboutMenu.add_command(label='Electro-Magnetic Method')
aboutMenu.add_separator()
aboutMenu.add_command(label='About us ', command=lambda:my_child())


main_window.config(menu=menubar)


pathChange('')
main_window.mainloop()
