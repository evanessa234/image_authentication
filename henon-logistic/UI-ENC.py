from tkinter import *
from tkinter import filedialog
import os
import LogisticEncryption as enc
import ImageTransformation as iT
import Henon_LogisticEncryption as hlE 
from PIL import ImageTk, Image

def choose_File():
    filename = filedialog.askopenfilename()
    entry1.insert(0,str(filename))

def performEntireEncryption():
    filename = entry1.get()
    key = entry2.get()
    resImage1 = hlE.pixelManipulation1(filename)
    resImage2 = hlE.pixelManipulation2(resImage1,key)
    entry3.insert(0, resImage2)

def performLogisticManipulation():
    filename = entry1.get()
    key = entry2.get()
    resImage = enc.LogisticEncryption(filename, key)
    entry4.insert(0,resImage)
    #print(filename)

def performHenonManipulation():
    filename = entry1.get()
    resImage = iT.pixelManipulation(filename)
    entry5.insert(0,resImage)
    #print(filename)


def openFileForHenon_logistic():
    window = Toplevel(root)
    window.title("Henon_Logistic Map")
    window.geometry("700x700")
    path = entry3.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForLogistic():
    window = Toplevel(root)
    window.title("Logistic Map")
    window.geometry("700x700")
    path = entry4.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForHenon():
    window = Toplevel(root)
    window.title("Henon Map")
    window.geometry("700x700")
    path = entry5.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()



#from tkFileDialog import askopenfilename

root =Tk()
Frame1 = Frame(root)
Frame1.pack()

Frame2 = Frame(root)
Frame2.pack(side=TOP)

Frame3 = Frame(root)
Frame3.pack(side=TOP)

Frame4 = Frame(root)
Frame4.pack(side =TOP)

Frame5 = Frame(root)
Frame5.pack(side=TOP)

label_1 = Label(Frame1, text ="Image to be Encrypted : ",width = 125)
entry1 = Entry(Frame1,width =100)
button1 = Button(Frame1, text = "Select Image",command = choose_File)

label_2 = Label(Frame2,text = "Enter key string:")
entry2 = Entry(Frame2,width = 80)


button2 = Button(Frame3, text = "Perform Encryption",command = performEntireEncryption,width=20)
entry3 = Entry(Frame3,width =80)
button3 = Button(Frame3, text="Open Image",command = openFileForHenon_logistic)

button4 = Button(Frame4, text="Generate Logistic Map",command = performLogisticManipulation,width=20)
entry4 = Entry(Frame4,width =80)
button5 = Button(Frame4, text="Open Image",command = openFileForLogistic)

button6 = Button(Frame5, text="Generate Henon Map",command = performHenonManipulation,width=20)
entry5 = Entry(Frame5,width=80)
button7 = Button(Frame5, text="Open Image",command = openFileForHenon)

label_1.pack(side = TOP)
entry1.pack(side = TOP)
button1.pack(side = TOP)

label_2.pack(side = TOP)
entry2.pack(side = TOP)


button2.pack(side = LEFT)
entry3.pack(side=LEFT)
button3.pack(side=LEFT)

button4.pack(side = LEFT)
entry4.pack(side = LEFT)
button5.pack(side = LEFT)

button6.pack(side = LEFT)
entry5.pack(side =LEFT)
button7.pack(side=LEFT)

root.mainloop()