# tkinter — Python interface to Tcl/Tk
# The tkinter package (“Tk interface”) is the standard Python interface to the 
# Tk GUI toolkit. 
# Tk itself is not part of Python; it is maintained at ActiveState.
# Coupling Widget Variables.
# There are many useful subclasses of Variable already defined: StringVar, IntVar, 
# DoubleVar, and BooleanVar. To read the current value of such a variable, call the
# get() method on it, and to change its value you call the set() method. 
# If you follow this protocol, the widget will always track the value of the variable, 
# with no further intervention on your part. 

class App(Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # here is the application variable

        self.contents = StringVar()

        # set it to some value

        self.contents.set("this is a variable")

        # tell the entry widget to watch this variable

        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return

        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

    def print_contents(self, event):

        print("hi. contents of entry is now ---->",
              self.contents.get())
