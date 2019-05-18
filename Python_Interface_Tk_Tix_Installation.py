# tkinter — Python interface to Tcl/Tk
# The tkinter package (“Tk interface”) is the standard Python interface to the 
# Tk GUI toolkit. 
# Tk itself is not part of Python; it is maintained at ActiveState.
# To use tkinter.tix, you must have the Tix widgets installed, usually alongside your 
# installation of the Tk widgets. 
# To test your installation, try the following:
 
from tkinter import tix

root = tix.Tk()
root.tk.eval('package require Tix')

 