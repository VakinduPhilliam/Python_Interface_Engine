# tkinter — Python interface to Tcl/Tk
# The tkinter package (“Tk interface”) is the standard Python interface to the 
# Tk GUI toolkit. 
# Tk itself is not part of Python; it is maintained at ActiveState.
# lookup(style, option, state=None, default=None). 
# Returns the value specified for option in style.
# If state is specified, it is expected to be a sequence of one or more states. 
# If the default argument is set, it is used as a fallback value in case no specification 
# for option is found.
# To check what font a Button uses by default:
 
from tkinter import ttk

print(ttk.Style().lookup("TButton", "font"))
