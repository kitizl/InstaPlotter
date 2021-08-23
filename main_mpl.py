#!python3

# we're going to do a quick and easy plotter thing

from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
# initializing the window

window = Tk()

# one pane system

# enter file (drag and drop)

# follow this : https://pythonguides.com/upload-a-file-in-python-tkinter/


def upload():
	pathname = pathWid.get()
	dataFrame = pd.read_csv(pathname)
	print("Data imported")
	print(dataFrame.head())

	headers = dataFrame.keys()
	# cleaning up data
	for k in headers:
		dataFrame[k] = pd.to_numeric(dataFrame[k], errors='coerce')
		# converts all data to float or int, and converts non-nums to NaNs
	dataFrame = dataFrame.dropna() # removing all NaN data
	print("Data cleaned")
	xSeries = dataFrame[headers[0]]
	print("Check")
	for i,head in enumerate(headers[1:]):
		plt.plot(xSeries, dataFrame[head])
	plt.show()

label1 = Label(window, text="Write path below").pack()
pathWid = Entry(window)
pathWid.pack()

 # takes in the file
uploadButton = Button(window, text="Upload", command=upload).pack()

# figure out what the data series are




# if it's just two columns, then let col1 :: x and col2 :: y and plot

# if there are multiple series, then generate two colums with all of the feature names
# with check boxes next to them

# load up the data and plot using ipython

window.mainloop() # to make sure everything works out swell

