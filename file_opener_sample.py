from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time


"""
Idea : 
	- Have a UI open up
	- Drop the .csv or whatever file into the UI
	- Have check boxes that highlight the series
		- Select x-series or y-series etc. etc.
	- Have a button that says "Plot!"
	- Just opens up an iPython

"""


ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x200')

def open_file():
	file_path = askopenfile(mode='r', filetypes=[('Image Files','*jpeg')])
	if file_path is not None:
		pass

def uploadFiles():
	pb1 = Progressbar(
		ws,
		orient=HORIZONTAL,
		length=300,
		mode='determinate')
	pb1.grid(row=4, columnspan=3, pady=20)
	for i in range(5):
		ws.update_idletasks()
		pb1['value']+=20
		time.sleep(1)
	pb1.destroy()
	Label(ws, text='File Uploaded Successfully!', foreground='green').grid(
		row=4, columnspan=3, pady=10)

adhar = Label(
	ws,
	text='Upload Government id in jpg format')
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(
	ws,
	text = 'Choose File',
	command = open_file)
adharbtn.grid(row=0, column=1)

