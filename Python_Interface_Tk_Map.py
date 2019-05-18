# tkinter — Python interface to Tcl/Tk
# The tkinter package (“Tk interface”) is the standard Python interface to the 
# Tk GUI toolkit. 
# Tk itself is not part of Python; it is maintained at ActiveState.
# map(style, query_opt=None, **kw). 
# Query or sets dynamic values of the specified option(s) in style.
# Each key in kw is an option and each value should be a list or a tuple (usually) containing 
# statespecs grouped in tuples, lists, or some other preference. 
# A statespec is a compound of one or more states and then a value.
# An example may make it more understandable:
 
import tkinter
from tkinter import ttk

root = tkinter.Tk()

style = ttk.Style()

style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

colored_btn = ttk.Button(text="Test", style="C.TButton").pack()

root.mainloop()
 