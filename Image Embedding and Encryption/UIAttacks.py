from tkinter import *
from tkinter import filedialog
import os
import embed as em
import Henon_LogisticEncryption as hlE 
from PIL import ImageTk, Image
from imageio import imread
import numpy as np
import cv2
from time import sleep


def choose_File_1():
    filename_1 = filedialog.askopenfilename()
    entry1.insert(0,str(filename_1))


def saltnoise():
        img = entry1.get()
        img = cv2.imread(img)
        img = img.copy()
        for k in range(1000):
            i = int(np.random.random() * img.shape[1])
            j = int(np.random.random() * img.shape[0])
            if img.ndim == 2:
                img[j, i] = 255
            elif img.ndim == 3:
                img[j, i, 0] = 255
                img[j, i, 1] = 255
                img[j, i, 2] = 255
        cv2.imwrite("./processed_images/attacked.jpg", img)
        return img

#from tkFileDialog import askopenfilename

def openFileForEmbedding():
    window = Toplevel(root1)
    window.title("Salt and Pepper noise")
    window.geometry("700x700")
    path = "./processed_images/attacked.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()


root1 =Tk()

Frame10 = Frame(root1)
Frame10.pack(side=TOP)

Frame1 = Frame(root1, bg= "#A0A9CB")
Frame1.pack(side=TOP)

Frame2 = Frame(root1)
Frame2.pack(side=TOP)

Frame4 = Frame(root1)
Frame4.pack(side =TOP) 

Frame3 = Frame(root1)
Frame3.pack(side=TOP)

Frame8 = Frame(root1)
Frame8.pack(side=TOP)



Frame5 = Frame(root1)
Frame5.pack(side=TOP)

Frame6 = Frame(root1)
Frame6.pack(side=TOP)

Frame7 = Frame(root1)
Frame7.pack(side=TOP)

Frame8 = Frame(root1)
Frame8.pack(side=TOP)

Frame9 = Frame(root1)
Frame9.pack(side=TOP)



def key_copy():
    root1.clipboard_clear()
    key = entry5.get()
    root1.clipboard_append(key)
    root1.update()

label_9 = Label(Frame10, text ="",width = 20)
label_5 = Label(Frame10, text ="Perform Attacks",width = 20,bg= "#ffffff")


label_1 = Label(Frame1, text ="Choose Image : ",width = 20,bg= "#A0A9CB").grid(row=0, column=0, padx=5, pady=5)
entry1 = Entry(Frame1,width =80)
button1 = Button(Frame1,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=0, column=2,padx=5, pady=5)


button2 = Button(Frame2,text="Gaussian Noise",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=1, column=0, columnspan= 1, padx=5,pady=5)
button3 = Button(Frame2, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=1, column=1, padx=5, pady=5)

button4 = Button(Frame2,text="Salt&Pepper Noise",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = saltnoise).grid(row=1, column=4, columnspan= 1, padx=5,pady=5)
button5 = Button(Frame2, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=1, column=5,padx=5, pady=5)

button6 = Button(Frame3,text="Rotate 90°",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=2, column=0,columnspan= 1 , ipadx= 2, padx=5,pady=5)
button7 = Button(Frame3, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=2, column=1,padx=5, pady=5)

button8 = Button(Frame3,text="Rotate 180°",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=2, column=3,columnspan= 1, padx=5,pady=5)
button9 = Button(Frame3, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=2, column=5,padx=5, pady=5)

button10 = Button(Frame4,text="Cropping",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=3, column=0, columnspan= 1, padx=5,pady=5)
button11 = Button(Frame4, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=3, column=1, padx=5, pady=5)

button12 = Button(Frame4,text="Compression",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=3, column=3, columnspan= 1, padx=5,pady=5)
button13 = Button(Frame4, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=3, column=5,padx=5, pady=5)

button14 = Button(Frame5,text="Resizing",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=4, column=0, columnspan= 1, padx=5,pady=5)
button15 = Button(Frame5, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=4, column=1,padx=5, pady=5)

button16 = Button(Frame5,text="Scaling",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=4, column=3, columnspan= 1, padx=5,pady=5)
button17 = Button(Frame5, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=4, column=5,padx=5, pady=5)



entry1.grid(row=0, column=1,padx=5, pady=5)


label_9.pack(side = TOP)
label_5.pack(side = TOP)
label_5.config(font=("Poppins", 14))


root1.mainloop()