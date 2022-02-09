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

def choose_File_2():
    filename_2 = filedialog.askopenfilename()
    entry2.insert(0,str(filename_2))

def image_resize(img1,size):
    image = Image.open(img1).resize((size, size), 1)
    image = image.convert('L')
    image.save("dataset//cover_img_512.jpg")
    absPath = os.path.abspath("dataset//cover_img_512.jpg") 
    image_array = np.array(image.getdata(), dtype=float).reshape((size, size))
    return absPath, image_array

def performWatermarkEmbedding():
    
    filename_1 = entry1.get()
    filename_2 = entry2.get()
    img, im1 = image_resize(filename_1, 512)
    im2 = np.array(Image.open(filename_2))
    if (len(im1.shape)==2 & len(im2.shape)==2) :
         resImage = em.DWT_GRAY_HL_EMBED(img, filename_2)
         entry3.insert(0,resImage)
    elif (len(im1.shape)==2 & len(im2.shape)==3) :
         resImage = em.DWT_GRAY_HL_EMBED(img, filename_2)
         entry3.insert(0,resImage)
    elif (len(im1.shape)==3 & len(im2.shape)==3) :
         resImage = em.DWT_RGB_HL_EMBED(img, filename_2)
         entry3.insert(0,resImage)
    else:
         resImage = em.DWT_GRAY_HL_EMBED(img, filename_2)
         entry3.insert(0,resImage)
    
    #print(filename)

def choose_File_3():
    filename_3 = filedialog.askopenfilename()
    entry4.insert(0,str(filename_3))

def performEntireEncryption():
    filename_3 = entry4.get()
    key = entry5.get()
    resImage1 = hlE.pixelManipulation1(filename_3)
    resImage2 = hlE.pixelManipulation2(resImage1,key)
    entry6.insert(0, resImage2)

#from tkFileDialog import askopenfilename

def openFileForEmbedding():
    window = Toplevel(root1)
    window.title("Watermarked Image")
    window.geometry("700x700")
    path = entry3.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForHenon_logistic():
    window = Toplevel(root1)
    window.title("Henon_Logistic Map (Encryption)")
    window.geometry("700x700")
    path = entry6.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()





root1 =Tk()

Frame7 = Frame(root1)
Frame7.pack(side=TOP)

Frame1 = Frame(root1, bg= "#A0A9CB")
Frame1.pack(side=TOP)

Frame2 = Frame(root1, bg= "#A0A9CB")
Frame2.pack(side=TOP)

Frame3 = Frame(root1, bg= "#A0A9CB")
Frame3.pack(side=TOP)

Frame8 = Frame(root1)
Frame8.pack(side=TOP)

Frame4 = Frame(root1, bg= "#A1AFDF")
Frame4.pack(side =TOP)

Frame5 = Frame(root1, bg= "#A1AFDF")
Frame5.pack(side=TOP)

Frame6 = Frame(root1, bg= "#A1AFDF")
Frame6.pack(side=TOP)

Frame9 = Frame(root1)
Frame9.pack(side=TOP)

def key_copy():
    root1.clipboard_clear()
    key = entry5.get()
    root1.clipboard_append(key)
    root1.update()

label_9 = Label(Frame7, text ="",width = 20)
label_5 = Label(Frame7, text ="Watermark Embedding",width = 20,bg= "#ffffff")


label_1 = Label(Frame1, text ="Choose Cover Img : ",width = 20,bg= "#A0A9CB").grid(row=0, column=0, padx=5, pady=5)
entry1 = Entry(Frame1,width =80)
button1 = Button(Frame1,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=0, column=2,padx=5, pady=5)

label_2 = Label(Frame2, text ="Choose Watermark : ",width = 20,bg= "#A0A9CB").grid(row=1, column=0, padx=5, pady=5)
entry2 = Entry(Frame2,width =80)
button2 = Button(Frame2,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_2).grid(row=1, column=2,padx=5,pady=5)

button3 = Button(Frame3, text="Embed Watermark" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performWatermarkEmbedding,width=20).grid(row=2, column=0,padx=4, pady=5)
entry3 = Entry(Frame3,width =80)
button4 = Button(Frame3, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=2, column=2,padx=5, pady=5)

label_8 = Label(Frame8, text ="",width = 20)
label_6 = Label(Frame8, text ="Image Encryption",width = 20,bg= "#ffffff")

label_3 = Label(Frame4, text ="Choose Watermarked img: ",width = 20,bg= "#A1AFDF").grid(row=3, column=0,padx=5, pady=5)
entry4 = Entry(Frame4,width =80)
button5 = Button(Frame4, text="Select image",bg="#515151" ,fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_3).grid(row=3, column=2,padx=5, pady=5)

label_4 = Label(Frame5, text = "Enter key string: ", width = 20,bg= "#A1AFDF").grid(row=4, column=0,padx=5, pady=5)
entry5 = Entry(Frame5,width = 80,bd=2)
button6 = Button(Frame5, text="Copy String",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = key_copy).grid(row=4, column=2,padx=6, pady=5)


button7 = Button(Frame6, text="Perform Encrytion" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performEntireEncryption,width=20).grid(row=5, column=0,padx=4, pady=5)
entry6 = Entry(Frame6,width =80)
button7 = Button(Frame6, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForHenon_logistic).grid(row=5, column=2,padx=5, pady=5)

label_7 = Label(Frame9, text ="",width = 20)

entry1.grid(row=0, column=1,padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry3.grid(row=2, column=1,padx=5, pady=5)
entry4.grid(row=3, column=1,padx=5, pady=5)
entry5.grid(row=4, column=1,padx=5, pady=5)
entry6.grid(row=5, column=1,padx=5, pady=5)


label_9.pack(side = TOP)
label_5.pack(side = TOP)
label_5.config(font=("Poppins", 14))
label_8.pack(side = TOP)
label_6.pack(side = TOP)
label_6.config(font=("Poppins", 14))
label_7.pack(side = TOP)

root1.mainloop()
