# tkinter — Python interface to Tcl/Tk
# The tkinter package (“Tk interface”) is the standard Python interface to the 
# Tk GUI toolkit. 
# Tk itself is not part of Python; it is maintained at ActiveState.
# class tkinter.tix.tixCommand. 
# The tix commands provide access to miscellaneous elements of Tix’s internal state and the Tix
# application context. Most of the information manipulated by these methods pertains to the application 
# as a whole, or to a screen or display, rather than to a particular window.
# To view the current settings, the common usage is:
 
from tkinter import tix

root = tix.Tk()

print(root.tix_configure())

 