# tkinter — Python interface to Tcl/Tk
# The tkinter package (“Tk interface”) is the standard Python interface to the 
# Tk GUI toolkit. 
# Tk itself is not part of Python; it is maintained at ActiveState.
# class tkinter.tix.Tk(screenName=None, baseName=None, className='Tix') 
# Toplevel widget of Tix which represents mostly the main window of an application. 
# It has an associated Tcl interpreter.
# Classes in the tkinter.tix module subclasses the classes in the tkinter. 
# The former imports the latter, so to use tkinter.tix with Tkinter, all you need to 
# do is to import one module.
# In general, you can just import tkinter.tix, and replace the toplevel call to 
# tkinter.Tk with tix.Tk:
 
from tkinter import tix
from tkinter.constants import *

root = tix.Tk()
 