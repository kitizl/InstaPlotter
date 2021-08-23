#!python3

"""
	Following this : https://www.youtube.com/watch?v=YXPyB4XeYLA
"""

from tkinter import * # this is horrible

# in tkinter, everything is a widget

# first step, we need to create a window

root = Tk() # this is the root widget
"""

Using PACK

myLabel = Label(root, text="Hello World")

# creating a label
# Label (the widget within which it needs to go, attributes of this object)

# ways to putting the object in the widget

# Way 1) Pack

myLabel.pack() # just shove it in there into root

# now we need to create an event loop

root.mainloop() # this is how you start a loop
"""

"""
# pressing 'X' is basically ending the loop

# Way 2) Grid System

myLabel1 = Label(root, text="Hellow World!")
myLabel2 = Label(root, text="My name is Nithesh")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# this is however, not "responsive"
"""

"""
	Creating a button


# this is just how you call Widgets in general.

# setting the state attribute to DISABLED greys out the button
# 	myButton = Button(root, text="Click me!", state=DISABLED)


# padx pady to change the size of the button
# 	myButton = Button(root, text="Click me!", padx=50, pady=50)

# introduce functionality

def myClick():
	myLabel = Label(root, text="Clicked!")
	myLabel.pack()

myButton = Button(root, text="Click me!", command=myClick)
myButton.pack()

# use fg and bg attrs to change the colour, you can use hex
"""

"""
	Creating input fields


# now you use an "entry widget"



entryWidget = Entry(root)
# we can change colour, width, etc.
entryWidget.insert(0, "Hello")
# default text within form (pre-filled)

myButton = Button(root, text="Submit")

entryWidget.pack()
myButton.pack()

## entryWidget.get() # retrieves the data from the field

"""

"""
	Calculator!
"""



root.mainloop()

