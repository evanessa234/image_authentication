import tkinter as Tk
from tkinter import *
from tkinter import filedialog
import os
import extract as ex
import Arnold_LogisticEncryption as alE
import Arnold_LogisticDecryption as alD
from PIL import ImageTk, Image
from imageio import imread
import numpy as np
import cv2
import formulas as form

def choose_File_1():
    filename_1 = filedialog.askopenfilename()
    entry1.insert(0,str(filename_1))
    canvas1 = Canvas(root2, width = 120, height = 140)  
    canvas1.pack()  
    #path = entry1.get()
    image = Image.open("dataset/encrypted.png")
    resize_image = image.resize((120, 120))
    img = ImageTk.PhotoImage(resize_image) 
    canvas1.image = img
    canvas1.create_image(0, 20, anchor=NW, image=img) 
    canvas1.create_text(60, 10, text="Extracted Watermark", fill="black", font=('Helvetica 8 bold'))
    canvas1.place(x= 420, y=560)
    

def image_resize(img1,size):
    image = Image.open(img1).resize((size, size), 1)
    image = image.convert('L')
    image.save("dataset//encrypted_img_512.jpg")
    absPath = os.path.abspath("dataset//encrypted_img_512.jpg") 
    image_array = np.array(image.getdata(), dtype=float).reshape((size, size))
    return absPath

def performEntireDecryption():
    filename_1 = entry1.get()
    key = entry2.get()
    file1 = open("myfile.txt","r+") 
    key_valid = file1.readline()
    if key == key_valid:
        resImage1 = alD.inverseArnold(filename_1)
        entry3.insert(0, resImage1)
    else:
        popup = Tk()
        popup.geometry("300x150")
        msg = "    Key is invalid Try again!!"
        title = "Invalid Key"
    #validate_key = StringVar()
        popup.title(title)
        label = Label(popup, text=msg, font = "Poppins,11")
        label.place( x = 20, y = 40)
    
        B1 = Button(
        popup, text="Okay", 
        bg='#424242', 
        fg='White', 
        activebackground = "#5f5f5f", bd = 0,
        highlightthickness = 0,
        relief = "ridge",
        command = popup.destroy)
        B1.config(height= 2, 
                 width=10)
        B1.place(x = 110, y = 80)
        popup.eval('tk::PlaceWindow . center')
        B1['state'] = 'normal' 
        popup.mainloop()
    #resImage2 = alD.pixelManipulation1(resImage1)
    
    
    canvas1 = Canvas(root2, width = 120, height = 140)  
    canvas1.pack()  
    path = entry3.get()
    image = Image.open(path)
    resize_image = image.resize((120, 120))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas1.image = img_resize
    canvas1.create_image(0, 20, anchor=NW, image=img_resize) 
    canvas1.create_text(60, 10, text="Decrypted watermark", fill="black", font=('Helvetica 8 bold'))
    canvas1.place(x= 680, y=560)

    decrypted = entry3.get()
    decrypted_img = cv2.imread(decrypted)
    orig_img = cv2.imread("dataset\\img_wm.png")
    ncc = form.NCIndex(orig_img, decrypted_img)
    entry6.insert(0,ncc)
    ber = form.ber()
    entry7.insert(0,ber)

def choose_File_2():
    filename_2 = filedialog.askopenfilename()
    entry4.insert(0,str(filename_2))
    canvas1 = Canvas(root2, width = 120, height = 140)  
    canvas1.pack()  
    path = entry4.get()
    image = Image.open(path)
    resize_image = image.resize((120, 120))
    img = ImageTk.PhotoImage(resize_image) 
    canvas1.image = img
    canvas1.create_image(0, 20, anchor=NW, image=img) 
    canvas1.create_text(60, 10, text="Watermarked Image", fill="black", font=('Helvetica 8 bold'))
    canvas1.place(x= 320, y=200)


def performWatermarkExtracting():
    filename_2 = entry4.get()
    filename_2 = image_resize(filename_2, 512)
    #cover_image = "images\\eye_512.png"
    #watermark = "images\\hospital_rgb.jpg"
    cover_image = "dataset\\cover_img_512.jpg"
    #cover_image = "new.jpg"
    watermark = "processed_images\\scrambledWatermark.jpg"
    im1 = np.array(Image.open(cover_image))
    im2 = np.array(Image.open(watermark))
    if (len(im1.shape)==2 & len(im2.shape)==2) :
         resImage1, resImage2 = ex.DWT_GRAY_HL_EXTRACT(cover_image, watermark, filename_2)
         entry5.insert(0,resImage1)
         entry8.insert(0,resImage2)
         #entry4.insert(0,resImage2)
    elif (len(im1.shape)==3 & len(im2.shape)==2) :
         resImage1, resImage2 = ex.DWT_GRAY_HL_EXTRACT(cover_image, watermark, filename_2)
         entry5.insert(0,resImage1)
         entry8.insert(0,resImage2)
    elif (len(im1.shape)==3 & len(im2.shape)==3) :
         resImage = ex.DWT_RGB_HL_EXTRACT(cover_image, watermark, filename_2)
         entry5.insert(0,resImage)

    else:
         resImage1, resImage2 = ex.DWT_GRAY_HL_EXTRACT(cover_image, watermark, filename_2)
         entry5.insert(0,resImage1)
         entry8.insert(0,resImage2)
    #entry5.insert(0,resImage)
    #print(filename)

    ex_cover_image = entry8.get()
    cover_img = cv2.imread(ex_cover_image)
    #resiz_image = cover_img.resize((512, 512))
    #image_2 = Image.open(resiz_image)
    orig_img = cv2.imread("dataset\\cover_img_512.jpg")
    psnr = form.psnr(orig_img, cover_img)
    entry9.insert(0,psnr)
    ssim = form.calculate_ssim(orig_img, cover_img)
    entry10.insert(0,ssim)

    canvas1 = Canvas(root2, width = 120, height = 140)  
    canvas1.pack()  
    #path = entry5.get()
    image = Image.open("dataset/encrypted.png")
    resize_image = image.resize((120, 120))
    img = ImageTk.PhotoImage(resize_image) 
    canvas1.image = img
    canvas1.create_image(0, 20, anchor=NW, image=img)
    canvas1.create_text(60, 10, text="Extracted Watermark", fill="black", font=('Helvetica 8 bold'))
    canvas1.place(x= 720, y=200)
    
    canvas2 = Canvas(root2, width = 120, height = 140)  
    canvas2.pack()  
    path = entry8.get()
    image_1 = Image.open(path)
    resized_image = image_1.resize((120, 120))
    img_1 = ImageTk.PhotoImage(resized_image) 
    canvas2.image = img_1
    canvas2.create_image(0, 20, anchor=NW, image=img_1)
    canvas2.create_text(60, 10, text="Extracted Cover image", fill="black", font=('Helvetica 8 bold'))
    canvas2.place(x= 520, y=200)

    
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
    #path = entry5.get()
    img = ImageTk.PhotoImage(Image.open("dataset/encrypted.png"))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForExtracting_coverimage():
    window = Toplevel(root2)
    window.title("Extracted Cover image")
    window.geometry("700x700")
    path = entry4.get()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()



root2 =Tk()
root2.geometry("1240x750")
root2.configure(bg = "#1F3943")
    


canvas = Canvas(
    root2,
    height = 375,
    width = 1240,
    bd = 0,
    highlightthickness = 0,
    bg="#1F3943",
    relief = "ridge")

canvas.place(x = 250, y = 10)

canvas1 = Canvas(
    root2,
    height = 375,
    width = 1240,
    bd = 0,
    highlightthickness = 0,
    bg="#1F3943",
    relief = "ridge")
canvas1.place(x = 250, y = 360)


Frame7 = Frame(canvas)
Frame7.pack(side=TOP)
Frame4 = Frame(canvas, bg= "#617D8B")
Frame4.pack(side =TOP)

Frame5 = Frame(canvas, bg= "#617D8B")
Frame5.pack(side=TOP)

Frame6 = Frame(canvas, bg= "#617D8B")
Frame6.pack(side=TOP)

Frame12 = Frame(canvas)
Frame12.pack(side=TOP)

Frame13 = Frame(canvas)
Frame13.pack(side=TOP)

Frame8 = Frame(canvas1)
Frame8.pack(side=TOP)

Frame1 = Frame(canvas1, bg= "#9ABACA")
Frame1.pack(side=TOP)

Frame2 = Frame(canvas1, bg= "#9ABACA")
Frame2.pack(side=TOP)

Frame3 = Frame(canvas1, bg= "#9ABACA")
Frame3.pack(side=TOP)

Frame11 = Frame(canvas1)
Frame11.pack(side=TOP)

Frame10 = Frame(canvas1)
Frame10.pack(side=TOP)



def key_copy():
    root2.clipboard_clear()
    key = entry2.get()
    root2.clipboard_append(key)
    root2.update()

#label_1 = Label(Frame6, text ="",width = 20)
label_2 = Label(Frame7, text ="Watermark Extraction",width = 20,bg= "#ffffff")
label_7 = Label(Frame4, text ="Choose Watermarked img: ",width = 20,bg= "#617D8B").grid(row=3, column=0,padx=5, pady=5)
entry4 = Entry(Frame4,width =80)
button5 = Button(Frame4, text="Select image",bg="#515151" ,fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_2).grid(row=3, column=2,padx=5, pady=5)


button6 = Button(Frame5, text="Extract Watermark" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performWatermarkExtracting,width=20).grid(row=4, column=0,padx=4, pady=5)
entry5 = Entry(Frame5,width =80)
button7 = Button(Frame5, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForExtracting).grid(row=4, column=2,padx=5, pady=5)

label_11 = Label(Frame6, text ="Extracted Cover image:",width = 20,bg= "#617D8B").grid(row=5, column=0,padx=6, pady=5)
entry8 = Entry(Frame6,width =80)
button8 = Button(Frame6, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForExtracting_coverimage).grid(row=5, column=2,padx=5, pady=5)

label_12 = Label(Frame12, text ="",width = 20)

label_13 = Label(Frame13, text ="PSNR:",width = 10,bg="#515151",fg="#ffffff").grid(row=6, column=0,padx=4, pady=5)
entry9 = Entry(Frame13,width =20)

label_14 = Label(Frame13, text ="SSIM:",width = 10, bg="#515151",fg="#ffffff").grid(row=6, column=3,padx=4, pady=5)
entry10 = Entry(Frame13,width =20)


#label_5 = Label(Frame9, text ="",width = 20)
label_6 = Label(Frame8, text ="Image Decryption",width = 20,bg= "#ffffff")

label_3 = Label(Frame1, text ="Choose encrypted Img : ",width = 20,bg= "#9ABACA").grid(row=0, column=0, padx=5, pady=5)
entry1 = Entry(Frame1,width =80)
button1 = Button(Frame1,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=0, column=2,padx=5, pady=5)

label_4 = Label(Frame2, text = "Enter key:", width = 20,bg= "#9ABACA").grid(row=1, column=0,padx=5, pady=5)
entry2 = Entry(Frame2,width = 80,bd=2)
button2 = Button(Frame2, text="Copy String",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = key_copy).grid(row=1, column=2,padx=6, pady=5)

button3 = Button(Frame3, text="Perform Decrytion" ,fg= "#ffffff", bg ="#353535",activebackground = "#000000",relief = "flat",pady= 5,command = performEntireDecryption,width=20).grid(row=2, column=0,padx=4, pady=5)
entry3 = Entry(Frame3,width =80)
button4 = Button(Frame3, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForHenon_logistic).grid(row=2, column=2,padx=5, pady=5)



label_10 = Label(Frame11, text ="",width = 20)

label_8 = Label(Frame10, text ="NCC:",width = 10,bg="#515151",fg="#ffffff").grid(row=6, column=0,padx=4, pady=5)
entry6 = Entry(Frame10,width =20)

label_9 = Label(Frame10, text ="BER:",width = 10, bg="#515151",fg="#ffffff").grid(row=6, column=3,padx=4, pady=5)
entry7 = Entry(Frame10,width =20)

entry1.grid(row=0, column=1,padx=5, pady=5)
entry2.grid(row=1, column=1,padx=5, pady=5)
entry3.grid(row=2, column=1,padx=5, pady=5)
entry4.grid(row=3, column=1,padx=5, pady=5)
entry5.grid(row=4, column=1,padx=5, pady=5)
entry8.grid(row=5, column=1,padx=5, pady=5)
entry9.grid(row=6, column=1,padx=10, pady=5)
entry10.grid(row=6, column=4,padx=5, pady=5)
entry6.grid(row=6, column=1,padx=10, pady=5)
entry7.grid(row=6, column=4,padx=5, pady=5)

#label_1.pack(side = TOP)
label_2.pack(side = TOP)
label_2.config(font=("Poppins", 14))
#label_5.pack(side = TOP)
label_6.pack(side = TOP)
label_6.config(font=("Poppins", 14))
#label_8.pack(side = TOP)

root2.mainloop()

#from tkFileDialog import askopenfilename
