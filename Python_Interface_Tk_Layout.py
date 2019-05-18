# tkinter � Python interface to Tcl/Tk
# The tkinter package (�Tk interface�) is the standard Python interface to the 
# Tk GUI toolkit. 
# Tk itself is not part of Python; it is maintained at ActiveState.
# layout(style, layoutspec=None) 
# Define the widget layout for given style. If layoutspec is omitted, return the layout 
# specification for given style.
# layoutspec, if specified, is expected to be a list or some other sequence type (excluding strings), 
# where each item should be a tuple and the first item is the layout name and the second item 
# should have the format described in Layouts.
# To understand the format, see the following example (it is not intended to do anything useful):
 
from tkinter import ttk
import tkinter

root = tkinter.Tk()

style = ttk.Style()

style.layout("TMenubutton", [
   ("Menubutton.background", None),
   ("Menubutton.button", {"children":
       [("Menubutton.focus", {"children":
           [("Menubutton.padding", {"children":
               [("Menubutton.label", {"side": "left", "expand": 1})]
           })]
       })]
   }),
])

mbtn = ttk.Menubutton(text='Text')
mbtn.pack()

root.mainloop()

 