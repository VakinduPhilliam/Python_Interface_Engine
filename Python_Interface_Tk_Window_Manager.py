# tkinter — Python interface to Tcl/Tk
# The tkinter package (“Tk interface”) is the standard Python interface to the 
# Tk GUI toolkit. 
# Tk itself is not part of Python; it is maintained at ActiveState.
# The Window Manager.
# To get at the toplevel window that contains an arbitrary widget, you can call 
# the _root() method. This method begins with an underscore to denote the fact 
# that this function is part of the implementation, and not an interface to Tk 
# functionality.

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application

myapp = App()

#
# here are method calls to the window manager class
#

myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# start the program

myapp.mainloop()
