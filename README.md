# InstaPlotter
A quick and dirty GUI to produce plots from data files.

Currently in alpha. 

Run the script from the command line using

```bash
python main_mpl.py

```

or the like and enter the pathname (by text) into the entry field and press **Upload**. Doing so will immediately produce a matplotlib plot based on the data itself.

Note, as the code currently stands, it by default assumes the first column is the x-series and the rest are dependent variables upon the first column, and therefore will be plotted as such. This is meant to only view the code in a visual manner and therefore lacks any details or customizations (as of now).

The future plan is allow for greater control over which data gets shown and if all of the data needs to be shown.

The current GUI backend used is [Tkinter](https://docs.python.org/3/library/tkinter.html) although the next version (currently under development) will use [PyQt5](https://pypi.org/project/PyQt5/) for its cross platform capabilities and better support for drag and drop functionality.

# Dependencies

For this program to work, you will need:
1. Tkinter (which comes pre-installed with a standard python installation)
2. [Pandas](https://pandas.pydata.org/)
3. [Matplotlib](https://matplotlib.org/)

Life can be made easier if you download the latest [Anaconda](https://www.anaconda.com/products/individual) distribution for Python.

==This code is currently under active development.==