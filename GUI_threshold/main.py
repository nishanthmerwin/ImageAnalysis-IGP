

from Tkinter import *
from tkFileDialog import askopenfilename

import PIL

from PIL import Image
from PIL import ImageTk

import os




app = Tk()

app.title("Threshold")

filename = askopenfilename()

print filename[-4:]

if(filename[-4:] != ".csv"):
	exit()


f = open(filename,"r")
picPaths = []
#Get all of the paths
for line in f:
	path = line.split(",")[5].rstrip()
	picPaths.append(path)

length = len(picPaths)


def displayimg(lineNumber):	
	img1 = Image.open(picPaths[lineNumber])
	img1 = img1.resize((250, 250), Image.ANTIALIAS)
	img1 = ImageTk.PhotoImage(img1)
	panel = Label(app,image=img)
	panel.pack(side="bottom",fill="both",expand="yes")


def on_closing():
	exit()

app.protocol("WM_DELETE_WINDOW", on_closing)



app.mainloop()

