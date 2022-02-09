from tkinter import *
from tkinter import filedialog
import os
import extract as ex
import Henon_LogisticDecryption as hlD 
from PIL import ImageTk, Image
from imageio import imread
import numpy as np

def choose_File_1():
    filename_1 = filedialog.askopenfilename()
    entry1.insert(0,str(filename_1))

def performEntireDecryption():
    filename_1 = entry1.get()
    key = entry2.get()
    resImage1 = hlD.pixelManipulation2(filename_1, key)
    resImage2 = hlD.pixelManipulation1(resImage1)
    entry3.insert(0, resImage2)

def choose_File_2():
    filename_2 = filedialog.askopenfilename()
    entry4.insert(0,str(filename_2))

def performWatermarkExtracting():
    filename_2 = entry4.get()
    #cover_image = "images\\eye_512.png"
    #watermark = "images\\hospital1.jpg"
    cover_image = "images\\x-ray_512.jpg"
    watermark = "images\\lena_gray_512.jpg"
    im1 = np.array(Image.open(cover_image))
    im2 = np.array(Image.open(watermark))
    if (len(im1.shape)==2 & len(im2.shape)==2) :
         resImage = ex.DWT_GRAY_HL_EXTRACT(cover_image, watermark, filename_2)
         #entry3.insert(0,resImage)
    elif (len(im1.shape)==2 & len(im2.shape)==3) :
         resImage = ex.DWT_GRAY_HL_EXTRACT(cover_image, watermark, filename_2)
         #entry3.insert(0,resImage)
    elif (len(im1.shape)==3 & len(im2.shape)==3) :
         resImage = ex.DWT_RGB_HL_EXTRACT(cover_image, watermark, filename_2)
         #entry3.insert(0,resImage)
    entry5.insert(0,resImage)
    #print(filename)


def openFileForHenon_logistic():
    window = Toplevel(root2)
    window.title("Henon_Logistic Map (Decryption)")
    window.geometry("700x700")
    path = entry3.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForExtracting():
    window = Toplevel(root2)
    window.title("Extracted Watermark")
    window.geometry("700x700")
    path = entry5.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()




root2 =Tk()

Frame7 = Frame(root2)
Frame7.pack(side=TOP)

Frame1 = Frame(root2, bg= "#A0A9CB")
Frame1.pack(side=TOP)

Frame2 = Frame(root2, bg= "#A0A9CB")
Frame2.pack(side=TOP)

Frame3 = Frame(root2, bg= "#A0A9CB")
Frame3.pack(side=TOP)

Frame8 = Frame(root2)
Frame8.pack(side=TOP)

Frame4 = Frame(root2, bg= "#A1AFDF")
Frame4.pack(side =TOP)

Frame5 = Frame(root2, bg= "#A1AFDF")
Frame5.pack(side=TOP)

Frame6 = Frame(root2)
Frame6.pack(side=TOP)

def key_copy():
    root2.clipboard_clear()
    key = entry2.get()
    root2.clipboard_append(key)
    root2.update()

label_1 = Label(Frame7, text ="",width = 20)
label_2 = Label(Frame7, text ="Image Decryption",width = 20,bg= "#ffffff")


label_3 = Label(Frame1, text ="Choose encrypted Img : ",width = 20,bg= "#A0A9CB").grid(row=0, column=0, padx=5, pady=5)
entry1 = Entry(Frame1,width =80)
button1 = Button(Frame1,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=0, column=2,padx=5, pady=5)

label_4 = Label(Frame2, text = "Enter key string: ", width = 20,bg= "#A0A9CB").grid(row=1, column=0,padx=5, pady=5)
entry2 = Entry(Frame2,width = 80,bd=2)
button2 = Button(Frame2, text="Copy String",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = key_copy).grid(row=1, column=2,padx=6, pady=5)

button3 = Button(Frame3, text="Perform Decrytion" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performEntireDecryption,width=20).grid(row=2, column=0,padx=4, pady=5)
entry3 = Entry(Frame3,width =80)
button4 = Button(Frame3, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForHenon_logistic).grid(row=2, column=2,padx=5, pady=5)

label_5 = Label(Frame8, text ="",width = 20)
label_6 = Label(Frame8, text ="Watermark Extraction",width = 20,bg= "#ffffff")

label_7 = Label(Frame4, text ="Choose Watermarked img: ",width = 20,bg= "#A1AFDF").grid(row=3, column=0,padx=5, pady=5)
entry4 = Entry(Frame4,width =80)
button5 = Button(Frame4, text="Select image",bg="#515151" ,fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_2).grid(row=3, column=2,padx=5, pady=5)


button6 = Button(Frame5, text="Extract Watermark" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performWatermarkExtracting,width=20).grid(row=4, column=0,padx=4, pady=5)
entry5 = Entry(Frame5,width =80)
button7 = Button(Frame5, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForExtracting).grid(row=4, column=2,padx=5, pady=5)

label_8 = Label(Frame6, text ="",width = 20)

entry1.grid(row=0, column=1,padx=5, pady=5)
entry2.grid(row=1, column=1,padx=5, pady=5)
entry3.grid(row=2, column=1,padx=5, pady=5)
entry4.grid(row=3, column=1,padx=5, pady=5)
entry5.grid(row=4, column=1,padx=5, pady=5)


label_1.pack(side = TOP)
label_2.pack(side = TOP)
label_2.config(font=("Poppins", 14))
label_5.pack(side = TOP)
label_6.pack(side = TOP)
label_6.config(font=("Poppins", 14))
label_8.pack(side = TOP)

root2.mainloop()

#from tkFileDialog import askopenfilename
