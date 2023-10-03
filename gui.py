# Software application development using python language 15-April-2020 \\

# my first programming application for forward modelling in EM Method
# Prof Sudha Agrahari  dept. of Geology & Exploration Geophysics IIT Kharagpur \\
# this application will plot the field raw data
# By using the Python libraries and modules




from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd, ttk
from tkinter.messagebox import showinfo
import pandas as pd
import numpy
import tree

from panels import frame

mahe = tk.Tk()

mahe.title('Electro-Magnetic Forward Modelling')

mahe.geometry('1200x800')

menubar = Menu(mahe)
mahe.config(menu=menubar)

def change_theme():
   current_bg = mahe.cget("bg")
   new_bg = "white" \
       if current_bg == "black" \
       else "black"
   mahe.configure(bg=new_bg)

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes,
    )

    showinfo(
        title='Selected File',
        message=filename
    )

def open_file():
   filename = fd.askopenfilename(title="Open a File", filetype=(("xlxs files", ".*xlsx"),
("All Files", "*.")))

   if filename:
      try:
         filename = r"{}".format(filename)
         df = pd.read_excel(filename)
      except ValueError:
         Label.config(text="File could not be opened")
      except FileNotFoundError:
         Label.config(text="File Not Found")

   # Clear all the previous data in tree
   clear_treeview()

   # Add new data in Treeview widget
   tree["column"] = list(df.columns)
   tree["show"] = "headings"

   # For Headings iterate over the columns
   for col in tree["column"]:
      tree.heading(col, text=col)

   # Put Data in Rows
   df_rows = df.to_numpy().tolist()
      for row in df_rows:
         tree.insert("", "end", values=row)

   tree.pack()

# Clear the Treeview Widget
def clear_treeview():
   tree.delete(*tree.get_children())

# Create a Treeview widget
tree = ttk.Treeview(frame)

# Add a Menu
m = Menu(mahe)
mahe.config(menu=m)
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)


fileMenu.add_command(label="File", command=select_file)
fileMenu.add_command(label="Open" , command=open_file)
fileMenu.add_command(label="Open Folder", command=open_file)
fileMenu.add_command(label="Import file", command=open_file)
fileMenu.add_command(label="Save", command=open_file)
fileMenu.add_command(label="Save As", command=open_file)
fileMenu.add_command(label="Print ", command=open_file)
fileMenu.add_command(label="Copy file", command=open_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit EM Tool", command=mahe.quit)



editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)

viewMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label ="View", menu = viewMenu)
viewMenu.add_command(label='Topology')
viewMenu.add_command(label='Recent files')
menu_sub=tk.Menu(viewMenu,tearoff=0,bg='white')
viewMenu.add_cascade(label='Appearance',menu=menu_sub )
menu_sub.add_command(label='Light Mode', command = change_theme)
menu_sub.add_command(label='Dark Mode', command = change_theme)


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

def my_child():
    mini_window=tk.Tk()
    mini_window.title("About EM Tool")
    mini_window.geometry("900x600")
    text = Message(mini_window,text = "Welcome to Em Tool\n ")
    text.pack()
    mini_window.mainloop()

mahe.mainloop()
