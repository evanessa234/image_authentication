from tkinter import *
from tkinter import filedialog
import os
import embed as em
import Arnold_LogisticEncryption as alE 
from PIL import ImageTk, Image
from imageio import imread
import numpy as np
import cv2
import formulas as form


def choose_File_1():
    filename_1 = filedialog.askopenfilename()
    entry1.insert(0,str(filename_1))
    canvas1 = Canvas(root1, width = 120, height = 140)  
    canvas1.pack()  
    path = entry1.get()
    image = Image.open(path)
    resize_image = image.resize((120, 120))
    img = ImageTk.PhotoImage(resize_image) 
    canvas1.image = img
    canvas1.create_image(0, 20, anchor=NW, image=img) 
    canvas1.create_text(60, 10, text="Cover image", fill="black", font=('Helvetica 8 bold'))
    canvas1.place(x= 350, y=560)
    

def choose_File_2():
    filename_2 = filedialog.askopenfilename()
    entry2.insert(0,str(filename_2))
    canvas1 = Canvas(root1, width = 120, height = 140)  
    canvas1.pack()  
    #path = entry2.get()
    image = Image.open("dataset/encrypted.png")
    resize_image = image.resize((120, 120))
    img = ImageTk.PhotoImage(resize_image) 
    canvas1.image = img
    canvas1.create_image(0, 20, anchor=NW, image=img) 
    canvas1.create_text(60, 10, text="Encrypted Watermark", fill="black", font=('Helvetica 8 bold'))
    canvas1.place(x= 550, y=560)
    

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
    elif (len(im1.shape)==3 & len(im2.shape)==2) :
         resImage = em.DWT_GRAY_HL_EMBED(img, filename_2)
         entry3.insert(0,resImage)
    elif (len(im1.shape)==3 & len(im2.shape)==3) :
         resImage = em.DWT_RGB_HL_EMBED(img, filename_2)
         entry3.insert(0,resImage)
    else:
         resImage = em.DWT_GRAY_HL_EMBED(img, filename_2)
         entry3.insert(0,resImage)

    canvas1 = Canvas(root1, width = 120, height = 140)  
    canvas1.pack()  
    path = entry1.get()
    image = Image.open(path)
    resize_image = image.resize((120, 120))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas1.image = img_resize
    canvas1.create_image(0, 20, anchor=NW, image=img_resize) 
    canvas1.create_text(60, 10, text="Watermarked image", fill="black", font=('Helvetica 8 bold'))
    canvas1.place(x= 750, y=560)
    watermarked = entry3.get()
    watermarked_img = cv2.imread(watermarked)
    orig_img = cv2.imread(img)
    psnr = form.psnr(orig_img, watermarked_img)
    entry7.insert(0,psnr)
    ssim = form.calculate_ssim(orig_img, watermarked_img)
    entry8.insert(0,ssim)
    #print(filename)

def choose_File_3():
    filename_3 = filedialog.askopenfilename()
    entry4.insert(0,str(filename_3))
    canvas1 = Canvas(root1, width = 120, height = 140)  
    canvas1.pack()  
    path = entry4.get()
    image = Image.open(path)
    resize_image = image.resize((120, 120))
    img = ImageTk.PhotoImage(resize_image) 
    canvas1.image = img
    canvas1.create_image(0, 20, anchor=NW, image=img) 
    canvas1.create_text(60, 10, text="Watermark", fill="black", font=('Helvetica 8 bold'))
    canvas1.place(x= 420, y=180)
    
    


def performEntireEncryption():
    filename_3 = entry4.get()
    #key = int(entry5.get())
    #resImage1 = alE.pixelManipulation1(filename_3)
    resImage2 = alE.arnold(filename_3)
    entry6.insert(0, resImage2)
    canvas1 = Canvas(root1, width = 120, height = 140)  
    canvas1.pack()  
    #path = entry6.get()
    image = Image.open("dataset/encrypted.png")
    resize_image = image.resize((120, 120))
    img = ImageTk.PhotoImage(resize_image) 
    canvas1.image = img
    canvas1.create_image(0, 20, anchor=NW, image=img)
    canvas1.create_text(60, 10, text="Encrypted Watermark", fill="black", font=('Helvetica 8 bold'))
    canvas1.place(x= 680, y=180)
    key = alE.random_key()
    file1 = open("myfile.txt","w")
    file1.write(key)
    file1.close()
    entry5.insert(0,key)
    
    


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
    #path = entry6.get()
    img = ImageTk.PhotoImage(Image.open("dataset/encrypted.png"))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()



root1 =Tk()
root1.geometry("1240x750")
root1.configure(bg = "#1F3943")
    
canvas = Canvas(
    root1,
    height = 375,
    width = 1240,
    bd = 0,
    highlightthickness = 0,
    bg="#1F3943",
    relief = "ridge")

canvas.place(x = 250, y = 10)

canvas1 = Canvas(
    root1,
    height = 375,
    width = 1240,
    bd = 0,
    highlightthickness = 0,
    bg="#1F3943",
    relief = "ridge")
canvas1.place(x = 250, y = 360)


Frame11 = Frame(canvas)
Frame11.pack(side=TOP)

Frame7 = Frame(canvas)
Frame7.pack(side=TOP)

Frame4 = Frame(canvas, bg= "#9ABACA")
Frame4.pack(side =TOP)


Frame6 = Frame(canvas, bg= "#9ABACA")
Frame6.pack(side=TOP)
Frame5 = Frame(canvas, bg= "#9ABACA")
Frame5.pack(side=TOP)





Frame12 = Frame(canvas)
Frame12.pack(side=TOP)

Frame13 = Frame(canvas)
Frame13.pack(side=TOP)

Frame8 = Frame(canvas1)
Frame8.pack(side=TOP)


Frame1 = Frame(canvas1, bg= "#617D8B")
Frame1.pack(side=TOP)

Frame2 = Frame(canvas1, bg= "#617D8B")
Frame2.pack(side=TOP)

Frame3 = Frame(canvas1, bg= "#617D8B")
Frame3.pack(side=TOP)


Frame10 = Frame(canvas)
Frame10.pack(side=TOP)

Frame9 = Frame(canvas1)
Frame9.pack(side=TOP)

def key_copy():
    root1.clipboard_clear()
    key = entry5.get()
    root1.clipboard_append(key)
    root1.update()

label_12 = Label(Frame11, text ="",width = 20)

label_5 = Label(Frame7, text ="Image Encryption",width = 20,bg= "#ffffff")

label_3 = Label(Frame4, text ="Choose Watermark: ",width = 20,bg= "#9ABACA").grid(row=3, column=0,padx=5, pady=5)
entry4 = Entry(Frame4,width =80)
button5 = Button(Frame4, text="Select image",bg="#515151" ,fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_3).grid(row=3, column=2,padx=5, pady=5)

label_4 = Label(Frame5, text = "Generated key: ", width = 20,bg= "#9ABACA").grid(row=4, column=0,padx=5, pady=5)
entry5 = Entry(Frame5,width = 80,bd=2)
button6 = Button(Frame5, text="Copy String",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = key_copy).grid(row=4, column=2,padx=6, pady=5)


button7 = Button(Frame6, text="Perform Encrytion" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performEntireEncryption,width=20).grid(row=5, column=0,padx=4, pady=5)
entry6 = Entry(Frame6,width =80)
button8 = Button(Frame6, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForHenon_logistic).grid(row=5, column=2,padx=5, pady=5)

#button9 = Button(Frame10, text="Watermark" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = openFileForHenon_logistic,width=15).grid(row=6, column=0,padx=4, pady=5)

#display_img = entry4.get()
#display_img = cv2.imread(display_img)
#resized_display_image = display_img.resize((330,65), Image.ANTIALIAS)
#new_display_image= ImageTk.PhotoImage(Image.open(entry4.get()))
#label_10 = Label(Frame10, image = new_display_image).pack(side=LEFT)

label_8 = Label(Frame8, text ="",width = 20)
label_6 = Label(Frame8, text ="Watermark Embedding",width = 20,bg= "#ffffff")

label_1 = Label(Frame1, text ="Choose Cover Img : ",width = 20,bg= "#617D8B").grid(row=0, column=0, padx=5, pady=5)
entry1 = Entry(Frame1,width =80)
button1 = Button(Frame1,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=0, column=2,padx=5, pady=5)

label_2 = Label(Frame2, text ="Choose Watermark : ",width = 20,bg= "#617D8B").grid(row=1, column=0, padx=5, pady=5)
entry2 = Entry(Frame2,width =80)
button2 = Button(Frame2,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_2).grid(row=1, column=2,padx=5,pady=5)

button3 = Button(Frame3, text="Embed Watermark" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performWatermarkEmbedding,width=20).grid(row=2, column=0,padx=4, pady=5)
entry3 = Entry(Frame3,width =80)
button4 = Button(Frame3, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForEmbedding).grid(row=2, column=2,padx=5, pady=5)

label_9 = Label(Frame10, text ="",width = 20)

label_10 = Label(Frame9, text ="PSNR:",width = 10,bg="#515151",fg="#ffffff").grid(row=6, column=0,padx=4, pady=5)
entry7 = Entry(Frame9,width =20)

label_11 = Label(Frame9, text ="SSIM:",width = 10, bg="#515151",fg="#ffffff").grid(row=6, column=3,padx=4, pady=5)
entry8 = Entry(Frame9,width =20)

entry1.grid(row=0, column=1,padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry3.grid(row=2, column=1,padx=5, pady=5)
entry4.grid(row=3, column=1,padx=5, pady=5)
entry5.grid(row=4, column=1,padx=5, pady=5)
entry6.grid(row=5, column=1,padx=5, pady=5)
entry7.grid(row=6, column=1,padx=10, pady=5)
entry8.grid(row=6, column=4,padx=5, pady=5)


#label_9.pack(side = TOP)
label_5.pack(side = TOP)
label_5.config(font=("Poppins", 14))
#label_8.pack(side = TOP)
label_6.pack(side = TOP)
label_6.config(font=("Poppins", 14))


root1.mainloop()