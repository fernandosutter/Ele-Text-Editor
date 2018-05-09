from tkinter import *
from tkinter import filedialog

#Fonts############################
def fontHelvetica():
	global text
	text.config(font="Helvetica")

def fontArial():
	global text
	text.config(font="Arial")

def fontTNR():
	global text
	text.config(font=("Times New Roman",))

def fontGothic():
	global text
	text.config(font="Gothic")

def comicsansms():
    global text
    text.config(font="{Comic Sans MS}")

def couriernew():
    global text
    text.config(font="{Courier New}")

def georgia():
    global text
    text.config(font="{Georgia}")

def impact():
    global text
    text.config(font="{Impact}")

def lucidaconsole():
    global text
    text.config(font="{Lucida Console}")

def lucidaunicode():
    global text
    text.config(font="{Lucida Sans Unicode}")

def palatino():
    global text
    text.config(font="{Palatino Linotype}")

def tahoma():
    global text
    text.config(font="{Tahoma}")

def trebuchet():
    global text
    text.config(font="{Trebuchet}")

def verdana():
    global text
    text.config(font="{Verdana}")

def symbol():
    global text
    text.config(font="{Symbol}")

def webdings():
    global text
    text.config(font="{Webdings}")

def wingdings():
    global text
    text.config(font="{Wingdings}")

def mssans():
    global text
    text.config(font="{MS Sans}")

def msserif():
    global text
    text.config(font="{MS Serif}")

#Hotkeys
def newFileHK(self):
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

def saveFileHK(self):
	global filename
	if filename == None:
		saveAs(self)
	else:
		t = text.get(0.0, END)
		f = open(filename, "w")
		f.write(t)
		f.close()

def saveAsHK(self):
	f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title ="UPS", message="Could not save file")

def openFileHK(self):
	f = filedialog.askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

#Loops commands
filename = None

def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

def saveFile():
	global filename
	if filename == None:
		saveAs(self)
	else:
		t = text.get(0.0, END)
		f = open(filename, "w")
		f.write(t)
		f.close()

def saveAs():
	f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title ="UPS", message="Could not save file")

def openFile():
	f = filedialog.askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)
######################################################################

#Main GUI
root = Tk()
root.title("Ele")
root.minsize(width=800, height=500)
root.maxsize(width=800, height=500)

text = Text(root, width=500, height=500)
text.pack()

###############################################################################
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile, accelerator="Ctrl+N")
filemenu.add_command(label="Open", command=openFile, accelerator="Ctrl+O")
filemenu.add_command(label="Save", command=saveFile, accelerator="Ctrl+S")
filemenu.add_command(label="Save as...", command=saveAs, accelerator="Ctrl+A")
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit, accelerator="Ctrl+Q")
menubar.add_cascade(label="File", menu=filemenu)
###############################################################################

#####Hot-Keys#######################
root.bind("<Control-n>", newFileHK)
root.bind("<Control-o>", openFileHK)
root.bind("<Control-s>", saveFileHK)
root.bind("<Control-a>", saveAsHK)
root.bind("<Control-q>", quit)
####################################

###################################################################
formatOptions = Menu(menubar)
formatOptions.add_command(label="Arial", command=fontArial)
formatOptions.add_command(label="Helvetica", command=fontHelvetica)
formatOptions.add_command(label="Times New Roman", command=fontTNR)
formatOptions.add_command(label="Gothic", command=fontGothic)
formatOptions.add_separator()
formatOptions.add_command(label="Georgia", command=georgia)
formatOptions.add_command(label="Trebuchet MS", command=trebuchet)
formatOptions.add_command(label="Verdana", command=verdana)
formatOptions.add_command(label="MS Sans Serif", command=mssans)
formatOptions.add_command(label="Comic Sans MS", command=comicsansms)
formatOptions.add_command(label="Courier New", command=couriernew)
formatOptions.add_command(label="Impact", command=impact)
formatOptions.add_command(label="Lucida Console", command=lucidaconsole)
formatOptions.add_command(label="Lucida Sans Unicode", command=lucidaunicode)
formatOptions.add_command(label="Plalatino Linotype", command=palatino)
formatOptions.add_command(label="Tahoma", command=tahoma)
formatOptions.add_command(label="Symbol", command=symbol)
formatOptions.add_command(label="Webdings", command=webdings)
formatOptions.add_command(label="Wingdings", command=wingdings)
formatOptions.add_command(label="MS Serif", command=msserif)

menubar.add_cascade(label="Font", menu=formatOptions)
###################################################################

root.config(menu=menubar)
root.mainloop()