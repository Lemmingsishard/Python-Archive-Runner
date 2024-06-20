import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os 
import zipfile

#initializations
surface = tkinter.Tk()
surface.geometry("400x240")
surface.title("Python_Archive_Runner")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#probably archaic and useless variables
bob = 0
title = ttk.Label(master = surface, text = "Python Archive Runner | v0.5", font = "24")
title.pack()
switch = str(os.listdir())

#archaic and useless functions and code blocks
dirlist = []
for i in os.listdir():
    dirlist.append(i)
    dirlist.append("\n")


def showdir():
    global dirlist
    dirlist = []
    for i in os.listdir():
        dirlist.append(i)
        dirlist.append("\n")
    global stringvar
    #stringvar.set(str(os.listdir()[0:3]) + "\n" + str(os.listdir()[3:6]) + "\n" + str(os.listdir()[6:9]) + "\n" + str(os.listdir()[9:]))
    stringvar.set(dirlist)

#something useful finally
def showabout():
    messagebox.showinfo("About", "Python_Archive_Runner version 0.5 made for windows\nmade by wizard studios Copyleft MMXXIV - MMXXV (remind me to update)")

list = []

#the lifeblood of this project
def waffen():
    global list
    flabbysteve = filedialog.askopenfilename(filetypes = [("Python Archive Files", "*.par")])
    with zipfile.ZipFile(flabbysteve, "r") as read:
        read.extractall()

        for i in read.namelist():
            list.append(i)
        read.close()

    with zipfile.ZipFile(flabbysteve, "w") as read:
        if os.path.isfile("main.py"):
            os.system("python main.py")
        elif os.path.isfile("main.pyw"):
            os.system("python main.pyw")
        elif os.path.isfile("main.pyc"):
            os.system("python main.pyc")
        else:
            print("Error 404")
            os.system("pause")
            exit()
        for i in list:
            read.write(i)
            os.remove(i)
        read.close()

#Zip to Par converter
def stormtrooper():
    sfile = cpen.get()
    ofile = cut.get()
    os.rename(sfile, ofile + ".par")

#menubar
menubar = tkinter.Menu(surface)
#file
file = tkinter.Menu(menubar, tearoff = 0) 
file.add_command(label = "Quit", command = exit)
menubar.add_cascade(label = "File", menu = file)
#help
helpmuh = tkinter.Menu(menubar, tearoff=0)
helpmuh.add_command(label="About", command=showabout)
menubar.add_cascade(label="Help", menu=helpmuh)
surface.configure(menu = menubar)

#Par Opener
oframe = ttk.Frame(master = surface)
obutton = ttk.Button(master = oframe, text = "open .par file", command = waffen)
obutton.pack()
obutton.pack()
oframe.pack(pady = 10)

#converter
cframe = ttk.Frame(master = surface)
ctitle = ttk.Label(master = cframe, text = "type the name of the file you want to convert to .par (extension required)")
ctitle.pack()
cpen = ttk.Entry(master = cframe)
cpen.pack()
cdostitle = ttk.Label(master = cframe, text = "type what you want the name of the new .par file to be (no extension)")
cdostitle.pack()
cut = ttk.Entry(master = cframe)
cut.pack()
cbutton = ttk.Button(master = cframe, text = "convert", command = stormtrooper)
cbutton.pack()
cframe.pack()

surface.mainloop()