# tkinter � Python interface to Tcl/Tk
# The tkinter package (�Tk interface�) is the standard Python interface to the 
# Tk GUI toolkit. 
# Tk itself is not part of Python; it is maintained at ActiveState.
# theme_settings(themename, settings). 
# Temporarily sets the current theme to themename, apply specified settings and then 
# restore the previous theme.
# Each key in settings is a style and each value may contain the keys �configure�, �map�, 
# �layout� and �element create� and they are expected to have the same format as specified 
# by the methods Style.configure(), Style.map(), Style.layout() and Style.element_create() 
# respectively.
# As an example, let�s change the Combobox for the default theme a bit:
 
from tkinter import ttk
import tkinter

root = tkinter.Tk()

style = ttk.Style()

style.theme_settings("default", {
   "TCombobox": {
       "configure": {"padding": 5},
       "map": {
           "background": [("active", "green2"),
                          ("!disabled", "green4")],
           "fieldbackground": [("!disabled", "green3")],
           "foreground": [("focus", "OliveDrab1"),
                          ("!disabled", "OliveDrab2")]
       }
   }
})

combo = ttk.Combobox().pack()

root.mainloop()
