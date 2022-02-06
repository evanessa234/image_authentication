from tkinter import *
from tkinter import filedialog
import os
import embed as em
import extract as ex
import Henon_LogisticDecryption as hlD 
import Henon_LogisticEncryption as hlE 
from PIL import ImageTk, Image

def choose_File_1():
    filename_1 = filedialog.askopenfilename()
    entry1.insert(0,str(filename_1))

def choose_File_2():
    filename_2 = filedialog.askopenfilename()
    entry2.insert(0,str(filename_2))


def performWatermarkEmbedding():
    filename_1 = entry1.get()
    filename_2 = entry2.get()
    resImage = em.DWT_RGB_HL_EMBED(filename_1, filename_2)
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

def openFileForHenon_logistic_Encryption():
    window = Toplevel(root1)
    window.title("Henon_Logistic Map (Encryption)")
    window.geometry("700x700")
    path = entry6.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

#hjkjhvc
def choose_File_4():
    filename_4 = filedialog.askopenfilename()
    entry7.insert(0,str(filename_4))

def performEntireDecryption():
    filename_4 = entry7.get()
    key = entry8.get()
    resImage1 = hlD.pixelManipulation2(filename_4, key)
    resImage2 = hlD.pixelManipulation1(resImage1)
    entry9.insert(0, resImage2)

def choose_File_5():
    filename_5 = filedialog.askopenfilename()
    entry10.insert(0,str(filename_5))

def choose_File_6():
    filename_6 = filedialog.askopenfilename()
    entry11.insert(0,str(filename_6))

def choose_File_7():
    filename_7 = filedialog.askopenfilename()
    entry12.insert(0,str(filename_7))

def performWatermarkExtracting():
    filename_5 = entry10.get()
    filename_6 = entry11.get()
    filename_7 = entry12.get()
    resImage = ex.DWT_RGB_HL_EXTRACT(filename_5, filename_6, filename_7)
    entry13.insert(0,resImage)
    #print(filename)


def openFileForHenon_logistic_Decryption():
    window = Toplevel(root2)
    window.title("Henon_Logistic Map (Decryption)")
    window.geometry("700x700")
    path = entry9.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForExtracting():
    window = Toplevel(root2)
    window.title("Extracted Watermark")
    window.geometry("700x700")
    path = entry11.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()



root1 =Tk()

Frame1 = Frame(root1)
Frame1.pack(side=TOP)

Frame2 = Frame(root1, bg= "#8B96BD")
Frame2.pack(side=TOP)

Frame3 = Frame(root1, bg= "#8B96BD")
Frame3.pack(side=TOP)

Frame4 = Frame(root1, bg= "#8B96BD")
Frame4.pack(side=TOP)

Frame5 = Frame(root1)
Frame5.pack(side=TOP)

Frame6 = Frame(root1, bg= "#A1AFDF")
Frame6.pack(side =TOP)

Frame7 = Frame(root1, bg= "#A1AFDF")
Frame7.pack(side=TOP)

Frame8 = Frame(root1, bg= "#A1AFDF")
Frame8.pack(side=TOP)

Frame9 = Frame(root1)
Frame9.pack(side=TOP)

Frame10 = Frame(root1)
Frame10.pack(side=TOP)

Frame11 = Frame(root1, bg= "#A1AFDF")
Frame11.pack(side =TOP)

Frame12 = Frame(root1, bg= "#A1AFDF")
Frame12.pack(side=TOP)

Frame13 = Frame(root1, bg= "#A1AFDF")
Frame13.pack(side=TOP)

Frame14 = Frame(root1)
Frame14.pack(side=TOP)

Frame15 = Frame(root1, bg= "#8B96BD")
Frame15.pack(side=TOP)

Frame16 = Frame(root1, bg= "#8B96BD")
Frame16.pack(side=TOP)

Frame17 = Frame(root1, bg= "#8B96BD")
Frame17.pack(side=TOP)

Frame18 = Frame(root1, bg= "#8B96BD")
Frame18.pack(side=TOP)

Frame19 = Frame(root1)
Frame19.pack(side=TOP)

label_1 = Label(Frame1, text ="",width = 20)
label_2 = Label(Frame1, text ="Watermark Embedding",width = 20,bg= "#ffffff")


label_3 = Label(Frame2, text ="Choose Cover Img : ",width = 20,bg= "#8B96BD").grid(row=0, column=0, padx=5, pady=5)
entry1 = Entry(Frame2,width =80)
button1 = Button(Frame2,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=0, column=2,padx=5, pady=5)

label_4 = Label(Frame3, text ="Choose Watermark : ",width = 20,bg= "#8B96BD").grid(row=1, column=0, padx=5, pady=5)
entry2 = Entry(Frame3,width =80)
button2 = Button(Frame3,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_2).grid(row=1, column=2,padx=5,pady=5)

button3 = Button(Frame4, text="Embed Watermark" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performWatermarkEmbedding,width=20).grid(row=2, column=0,padx=4, pady=5)
entry3 = Entry(Frame4,width =80)
button4 = Button(Frame4, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=2, column=2,padx=5, pady=5)

label_5 = Label(Frame5, text ="",width = 20)
label_6 = Label(Frame5, text ="Image Encryption",width = 20,bg= "#ffffff")

label_7 = Label(Frame6, text ="Choose Watermarked img: ",width = 20,bg= "#A1AFDF").grid(row=3, column=0,padx=5, pady=5)
entry4 = Entry(Frame6,width =80)
button5 = Button(Frame6, text="Select image",bg="#515151" ,fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_3).grid(row=3, column=2,padx=5, pady=5)

label_8 = Label(Frame7, text = "Enter key string: ", width = 20,bg= "#A1AFDF").grid(row=4, column=0,padx=5, pady=5)
entry5 = Entry(Frame7,width = 80,bd=2)
button6 = Button(Frame7, text="Copy String",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForHenon_logistic_Encryption).grid(row=4, column=2,padx=6, pady=5)


button7 = Button(Frame8, text="Perform Encrytion" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performEntireEncryption,width=20).grid(row=5, column=0,padx=4, pady=5)
entry6 = Entry(Frame8,width =80)
button7 = Button(Frame8, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForHenon_logistic_Encryption).grid(row=5, column=2,padx=5, pady=5)

label_9 = Label(Frame9, text ="",width = 20)

entry1.grid(row=0, column=1,padx=5, pady=5)
entry2.grid(row=1, column=1,padx=5, pady=5)
entry3.grid(row=2, column=1,padx=5, pady=5)
entry4.grid(row=3, column=1,padx=5, pady=5)
entry5.grid(row=4, column=1,padx=5, pady=5)
entry6.grid(row=5, column=1,padx=5, pady=5)



label_1.pack(side = TOP)
label_2.pack(side = TOP)
label_2.config(font=("Poppins", 14))
label_5.pack(side = TOP)
label_6.pack(side = TOP)
label_6.config(font=("Poppins", 14))
label_9.pack(side = TOP)



label_10 = Label(Frame10, text ="",width = 20)
label_11 = Label(Frame10, text ="Image Decryption",width = 20,bg= "#ffffff")


label_12 = Label(Frame11, text ="Choose encrypted Img : ",width = 20,bg= "#8B96BD").grid(row=6, column=0, padx=5, pady=5)
entry7 = Entry(Frame11,width =80)
button8 = Button(Frame11,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_4).grid(row=6, column=2,padx=5, pady=5)

label_13 = Label(Frame12, text = "Enter key string: ", width = 20,bg= "#8B96BD").grid(row=7, column=0,padx=5, pady=5)
entry8 = Entry(Frame12,width = 80,bd=2)
button9 = Button(Frame12, text="Copy String",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForHenon_logistic_Decryption).grid(row=7, column=2,padx=6, pady=5)

button3 = Button(Frame13, text="Perform Decrytion" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performEntireDecryption,width=20).grid(row=8, column=0,padx=4, pady=5)
entry9 = Entry(Frame13,width =80)
button10 = Button(Frame13, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForHenon_logistic_Decryption).grid(row=8, column=2,padx=5, pady=5)

label_14 = Label(Frame14, text ="",width = 20)
label_15 = Label(Frame14, text ="Watermark Extraction",width = 20,bg= "#ffffff")

label_16 = Label(Frame15, text ="Choose cover img: ",width = 20,bg= "#A1AFDF").grid(row=9, column=0,padx=5, pady=5)
entry10 = Entry(Frame15,width =80)
button11 = Button(Frame15, text="Select image",bg="#515151" ,fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_5).grid(row=9, column=2,padx=5, pady=5)

label_17 = Label(Frame16, text ="Choose Watermark: ",width = 20,bg= "#A1AFDF").grid(row=10, column=0,padx=5, pady=5)
entry11 = Entry(Frame16,width =80)
button12 = Button(Frame16, text="Select image",bg="#515151" ,fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_6).grid(row=10, column=2,padx=5, pady=5)

label_18 = Label(Frame17, text ="Choose Watermarked img: ",width = 20,bg= "#A1AFDF").grid(row=11, column=0,padx=5, pady=5)
entry12 = Entry(Frame17,width =80)
button13 = Button(Frame17, text="Select image",bg="#515151" ,fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_7).grid(row=11, column=2,padx=5, pady=5)


button14 = Button(Frame18, text="Extract Watermark" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performWatermarkExtracting,width=20).grid(row=12, column=0,padx=4, pady=5)
entry13 = Entry(Frame18,width =80)
button15 = Button(Frame18, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForExtracting).grid(row=12, column=2,padx=5, pady=5)

label_19 = Label(Frame19, text ="",width = 20)

entry7.grid(row=6, column=1,padx=5, pady=5)
entry8.grid(row=7, column=1,padx=5, pady=5)
entry9.grid(row=8, column=1,padx=5, pady=5)
entry10.grid(row=9, column=1,padx=5, pady=5)
entry11.grid(row=10, column=1,padx=5, pady=5)
entry12.grid(row=11, column=1,padx=5, pady=5)
entry13.grid(row=12, column=1,padx=5, pady=5)



label_10.pack(side = TOP)
label_11.pack(side = TOP)
label_11.config(font=("Poppins", 14))
label_14.pack(side = TOP)
label_15.pack(side = TOP)
label_15.config(font=("Poppins", 14))
label_19.pack(side = TOP)

root1.mainloop()