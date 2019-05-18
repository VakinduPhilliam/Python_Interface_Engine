# tkinter — Python interface to Tcl/Tk
# The tkinter package (“Tk interface”) is the standard Python interface to the 
# Tk GUI toolkit. 
# Tk itself is not part of Python; it is maintained at ActiveState.
# configure(style, query_opt=None, **kw) 
# Query or set the default value of the specified option(s) in style.
# Each key in kw is an option and each value is a string identifying the value 
# for that option.
# For example, to change every default button to be a flat button with some padding 
# and a different background color:
 
from tkinter import ttk
import tkinter

root = tkinter.Tk()

ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")

btn = ttk.Button(text="Sample")
btn.pack()

root.mainloop()

 