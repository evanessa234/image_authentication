import tkinter as Tk
from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
from imageio import imread
import numpy as np
import cv2
import math
from skimage.util import random_noise
import formulas as form

def choose_File_1():
    filename_1 = filedialog.askopenfilename()
    entry1.insert(0,str(filename_1))
    #canvas1 = Canvas(root1, width = 120, height = 140)  
    #canvas1.pack()  
    path = entry1.get()
    image = Image.open(path)
    resize_image = image.resize((120, 120))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas1.image = img_resize
    canvas1.create_image(0, 20, anchor=NW, image=img_resize) 
    

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
    cv2.imwrite("./processed_images/attacked_salt&pepper.jpg", img)
    #canvas1 = Canvas(root1, width = 120, height = 140)  
    #canvas1.pack()  
    image = Image.open("processed_images/attacked_salt&pepper.jpg")
    resize_image = image.resize((120, 120))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas3.image = img_resize
    canvas3.create_image(0, 20, anchor=NW, image=img_resize) 
    

    attacked = cv2.imread("processed_images/attacked_salt&pepper.jpg")
    #resize_image = cv2..resize(attacked,(512,512))
    orig_img = cv2.imread("dataset/cover_img_512.jpg")
    psnr = form.psnr(orig_img, attacked)
    entry4.insert(0,psnr)
    ssim = form.calculate_ssim(orig_img, attacked)
    entry11.insert(0,ssim)
    return img

def gaussian_noise():
    img = entry1.get()
    img = cv2.imread(img)
    img = img.copy()
    im_arr = np.asarray(img)
    # can parametrize: clip, mean, var
    noise_img = random_noise(im_arr, mode='gaussian')
    noise_img = (120 * noise_img).astype(np.uint8)
    cv2.imwrite("./processed_images/attacked_gaussiannoise.jpg", noise_img)

    #canvas1 = Canvas(root1, width = 120, height = 140)  
    #canvas1.pack()  
    image = Image.open("processed_images/attacked_gaussiannoise.jpg")
    resize_image = image.resize((120, 120))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas2.image = img_resize
    canvas2.create_image(0, 20, anchor=NW, image=img_resize) 
    #canvas1.create_text(60, 10, text="Gaussian noise", fill="black", font=('Helvetica 8 bold'))
    #canvas1.place(x= 140, y=430)

    attacked = cv2.imread("processed_images/attacked_gaussiannoise.jpg")
    #resize_image = cv2..resize(attacked,(512,512))
    orig_img = cv2.imread("dataset/cover_img_512.jpg")
    psnr = form.psnr(orig_img, attacked)
    entry2.insert(0,psnr)
    ssim = form.calculate_ssim(orig_img, attacked)
    entry3.insert(0,ssim)

    return noise_img

def rotate180():
    img = entry1.get()
    Original_Image = Image.open(img)
    rotated_image = Original_Image.rotate(180)
    rotated_img = rotated_image.save("./processed_images/attacked_roatation180.jpg")
    return rotated_img

def rotate10():
    img = entry1.get()
    Original_Image = Image.open(img)
    rotated_image = Original_Image.rotate(10)
    rotated_img = rotated_image.save("./processed_images/attacked_roatation10.jpg")
    #canvas1 = Canvas(root1, width = 120, height = 140)  
    #canvas1.pack()  
    image = Image.open("processed_images/attacked_roatation10.jpg")
    resize_image = image.resize((120, 120))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas6.image = img_resize
    canvas6.create_image(0, 20, anchor=NW, image=img_resize) 
    
    attacked = cv2.imread("processed_images/attacked_roatation10.jpg")
    #resize_image = cv2..resize(attacked,(512,512))
    orig_img = cv2.imread("dataset/cover_img_512.jpg")
    psnr = form.psnr(orig_img, attacked)
    entry7.insert(0,psnr)
    ssim = form.calculate_ssim(orig_img, attacked)
    entry14.insert(0,ssim)

    return rotated_img


def cropimg():
    img = entry1.get()
    img = cv2.imread(img)
    rows,cols, _ = img.shape
    crop_img = img[256:rows, 30:cols]
    cv2.imwrite("./processed_images/attacked_cropping.jpg", crop_img)
    #canvas1 = Canvas(root1, width = 120, height = 140)  
    #canvas1.pack()  
    image = Image.open("processed_images/attacked_cropping.jpg")
    resize_image = image.resize((120, 50))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas4.image = img_resize
    canvas4.create_image(0, 20, anchor=NW, image=img_resize) 

    attacked = cv2.imread("processed_images/attacked_cropping.jpg")
    resize_image = cv2.resize(attacked,(512,512))
    orig_img = cv2.imread("dataset/cover_img_512.jpg")
    psnr = form.psnr(orig_img, resize_image)
    entry5.insert(0,psnr)
    ssim = form.calculate_ssim(orig_img, resize_image)
    entry12.insert(0,ssim)
    return crop_img

def scaling():
    img = entry1.get()
    im = cv2.imread(img)
    width = int(im.shape[1] * 200 / 100)
    height = int(im.shape[0] * 200 / 100)
    dim = (width, height)
    img = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite("./processed_images/attacked_scaling.jpg", img)
    #canvas1 = Canvas(root1, width = 120, height = 140)  
    #anvas1.pack()  
    image = Image.open("processed_images/attacked_scaling.jpg")
    resize_image = image.resize((120, 120))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas9.image = img_resize
    canvas9.create_image(0, 20, anchor=NW, image=img_resize) 

    attacked = cv2.imread("processed_images/attacked_scaling.jpg")
    resize_image = cv2.resize(attacked,(512,512))
    orig_img = cv2.imread("dataset/cover_img_512.jpg")
    psnr = form.psnr(orig_img, resize_image)
    entry10.insert(0,psnr)
    ssim = form.calculate_ssim(orig_img, resize_image)
    entry17.insert(0,ssim)

    return img

def sharpening():
    img = entry1.get()
    im = cv2.imread(img)
    kernel = np.array([[-1,0,-1], 
                       [-1, 9,-1],
                       [-1,-1,-1]])
    sharpened = cv2.filter2D(im, -1, kernel)
    cv2.imwrite("./processed_images/attacked_sharpened.jpg", sharpened)
    #canvas1 = Canvas(root1, width = 120, height = 140)  
    #canvas1.pack()  
    image = Image.open("processed_images/attacked_sharpened.jpg")
    resize_image = image.resize((120, 120))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas7.image = img_resize
    canvas7.create_image(0, 20, anchor=NW, image=img_resize) 
    
    attacked = cv2.imread("processed_images/attacked_sharpened.jpg")
    #resize_image = cv2..resize(attacked,(512,512))
    orig_img = cv2.imread("dataset/cover_img_512.jpg")
    psnr = form.psnr(orig_img, attacked)
    entry8.insert(0,psnr)
    ssim = form.calculate_ssim(orig_img, attacked)
    entry15.insert(0,ssim)
    return img

def darker10():
    img = entry1.get()
    img = cv2.imread(img)
    img = img.copy()
    w, h = img.shape[:2]
    for xi in range(0, w):
        for xj in range(0, h):
            img[xi, xj, 0] = int(img[xi, xj, 0] * 0.9)
            img[xi, xj, 1] = int(img[xi, xj, 1] * 0.9)
            img[xi, xj, 2] = int(img[xi, xj, 2] * 0.9)
    cv2.imwrite("./processed_images/attacked_darkened.jpg", img)
    #canvas1 = Canvas(root1, width = 120, height = 140)  
    #canvas1.pack()  
    image = Image.open("processed_images/attacked_darkened.jpg")
    resize_image = image.resize((120, 120))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas8.image = img_resize
    canvas8.create_image(0, 20, anchor=NW, image=img_resize) 

    attacked = cv2.imread("processed_images/attacked_darkened.jpg")
    #resize_image = cv2..resize(attacked,(512,512))
    orig_img = cv2.imread("dataset/cover_img_512.jpg")
    psnr = form.psnr(orig_img, attacked)
    entry9.insert(0,psnr)
    ssim = form.calculate_ssim(orig_img, attacked)
    entry16.insert(0,ssim)

    return img

def compression():
    img = entry1.get()
    img = Image.open(img)
    path = "processed_images/attacked_compression.jpg"
    img.save(path, optimize=True, quality=10)
    #canvas1 = Canvas(root1, width = 120, height = 140)  
    #canvas1.pack()  
    image = Image.open("processed_images/attacked_compression.jpg")
    resize_image = image.resize((120, 120))
    img_resize = ImageTk.PhotoImage(resize_image) 
    canvas5.image = img_resize
    canvas5.create_image(0, 20, anchor=NW, image=img_resize) 
    
    attacked = cv2.imread("processed_images/attacked_compression.jpg")
    #resize_image = cv2..resize(attacked,(512,512))
    orig_img = cv2.imread("dataset/cover_img_512.jpg")
    psnr = form.psnr(orig_img, attacked)
    entry6.insert(0,psnr)
    ssim = form.calculate_ssim(orig_img, attacked)
    entry13.insert(0,ssim)

    return cv2.imread(path)
#from tkFileDialog import askopenfilename

def openFileForSaltandPepperNoise():
    window = Toplevel(root1)
    window.title("Salt and Pepper noise")
    window.geometry("700x700")
    path = "./processed_images/attacked_salt&pepper.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForSharpen():
    window = Toplevel(root1)
    window.title("Sharpened image")
    window.geometry("700x700")
    path = "./processed_images/attacked_sharpened.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForRotate10():
    window = Toplevel(root1)
    window.title("Rotation 10°")
    window.geometry("700x700")
    path = "./processed_images/attacked_roatation10.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForCropped():
    window = Toplevel(root1)
    window.title("Cropped image")
    window.geometry("700x700")
    path = "./processed_images/attacked_cropping.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForScaling():
    window = Toplevel(root1)
    window.title("Scaled image")
    window.geometry("700x700")
    path = "./processed_images/attacked_scaling.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForDarkening():
    window = Toplevel(root1)
    window.title("Darkened image")
    window.geometry("700x700")
    path = "./processed_images/attacked_darkened.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForCompression():
    window = Toplevel(root1)
    window.title("Compressed image")
    window.geometry("700x700")
    path = "./processed_images/attacked_compression.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForGaussianNoise():
    window = Toplevel(root1)
    window.title("Gaussian Noise")
    window.geometry("700x700")
    path = "./processed_images/attacked_gaussiannoise.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

root1 = Tk()
root1.geometry("1500x750")
#root1.configure(bg = "#ffffff")
    
canvas = Canvas(
    root1,
    height = 750,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    bg="#1F3943",
    relief = "ridge")
canvas.place(x = 0, y = 0)

Frame11 = Frame(root1)
Frame11.pack(side=TOP)

Frame10 = Frame(root1)
Frame10.pack(side=TOP)

Frame1 = Frame(root1, bg= "#9ABACA")
Frame1.pack(side=TOP)

Frame2 = Frame(root1)
Frame2.pack(side=TOP)

Frame4 = Frame(root1)
Frame4.pack(side =TOP) 

Frame3 = Frame(root1)
Frame3.pack(side=TOP)





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

label_9 = Label(Frame11, text ="",width = 20)
label_5 = Label(Frame10, text ="Perform Attacks",width = 20,bg= "#ffffff")


label_1 = Label(Frame1, text ="Choose Image : ",width = 18,bg= "#9ABACA").grid(row=0, column=0, ipadx= 1, padx=5, pady=5)
entry1 = Entry(Frame1,width =80)
button1 = Button(Frame1,text="Select image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = choose_File_1).grid(row=0, column=2,padx=5, pady=5)


button2 = Button(Frame2,text="Gaussian Noise",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = gaussian_noise, width=38).grid(row=1, column=0, columnspan= 1, padx=5,pady=5)
button3 = Button(Frame2, text="Open",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForGaussianNoise, width=8).grid(row=1, column=1, padx=5, pady=5)

button4 = Button(Frame2,text="Salt&Pepper Noise",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = saltnoise, width=38).grid(row=1, column=3, columnspan= 1, padx=5,pady=5)
button5 = Button(Frame2, text="Open",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForSaltandPepperNoise, width=8).grid(row=1, column=5,padx=5, pady=5)

button6 = Button(Frame3,text="Rotate 10°",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = rotate10, width=38).grid(row=2, column=0,columnspan= 1 ,padx=5,pady=5)
button7 = Button(Frame3, text="Open",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForRotate10, width=8).grid(row=2, column=1,padx=5, pady=5)

button8 = Button(Frame3,text="Sharpening",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = sharpening, width=38).grid(row=2, column=3,columnspan= 1, padx=5,pady=5)
button9 = Button(Frame3, text="Open",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForSharpen, width=8).grid(row=2, column=5,padx=5, pady=5)

button10 = Button(Frame4,text="Cropping",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = cropimg, width=38).grid(row=3, column=0, columnspan= 1, padx=5,pady=5)
button11 = Button(Frame4, text="Open",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForCropped, width=8).grid(row=3, column=1, padx=5, pady=5)

button12 = Button(Frame4,text="Compression",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = compression, width=38).grid(row=3, column=3, columnspan= 1, padx=5,pady=5)
button13 = Button(Frame4, text="Open",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForCompression, width=8).grid(row=3, column=5,padx=5, pady=5)

button14 = Button(Frame5,text="Darkening",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = darker10, width=38).grid(row=4, column=0, columnspan= 1, padx=5,pady=5)
button15 = Button(Frame5, text="Open",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForDarkening, width=8).grid(row=4, column=1,padx=5, pady=5)

button16 = Button(Frame5,text="Scaling",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = scaling, width=38).grid(row=4, column=3, columnspan= 1, padx=5,pady=5)
button17 = Button(Frame5, text="Open",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForScaling, width=8).grid(row=4, column=5,padx=5, pady=5)

label_2 = Label(Frame6, text ="",width = 20)

canvas1 = Canvas(root1, width = 120, height = 140)  
canvas1.pack() 
canvas1.create_text(60, 10, text="Watermarked image", fill="black", font=('Helvetica 8 bold'))
canvas1.place(x= 680, y=240)

canvas2 = Canvas(root1, width = 120, height = 140)  
canvas2.pack() 
canvas2.create_text(60, 10, text="Gaussian noise", fill="black", font=('Helvetica 8 bold'))
canvas2.place(x= 170, y=430)

canvas3 = Canvas(root1, width = 120, height = 140)  
canvas3.pack() 
canvas3.create_text(60, 10, text="Salt&Pepper noise", fill="black", font=('Helvetica 8 bold'))
canvas3.place(x= 320, y=430)

canvas4 = Canvas(root1, width = 120, height = 140)  
canvas4.pack() 
canvas4.create_text(60, 10, text="Cropping", fill="black", font=('Helvetica 8 bold'))
canvas4.place(x= 470, y=430)

canvas5 = Canvas(root1, width = 120, height = 140)  
canvas5.pack() 
canvas5.create_text(60, 10, text="Compression", fill="black", font=('Helvetica 8 bold'))
canvas5.place(x= 620, y=430)

canvas6 = Canvas(root1, width = 120, height = 140)  
canvas6.pack() 
canvas6.create_text(60, 10, text="Rotation 10°", fill="black", font=('Helvetica 8 bold'))
canvas6.place(x= 770, y=430)

canvas7 = Canvas(root1, width = 120, height = 140)  
canvas7.pack() 
canvas7.create_text(60, 10, text="Sharpening", fill="black", font=('Helvetica 8 bold'))
canvas7.place(x= 920, y=430)

canvas8 = Canvas(root1, width = 120, height = 140)  
canvas8.pack() 
canvas8.create_text(60, 10, text="Darkening°", fill="black", font=('Helvetica 8 bold'))
canvas8.place(x= 1070, y=430)

canvas9 = Canvas(root1, width = 120, height = 140)  
canvas9.pack()
canvas9.create_text(60, 10, text="Scaling", fill="black", font=('Helvetica 8 bold'))
canvas9.place(x= 1220, y=430) 

label_3 = Label(canvas, text ="PSNR:",width = 14,bg="#515151",fg="#ffffff")
label_3.place(x= 30, y=590)
entry2 = Entry(canvas,width =20)
entry2.place(x= 170, y=590)

entry4 = Entry(canvas,width =20)
entry4.place(x= 320, y=590)

entry5 = Entry(canvas,width =20)
entry5.place(x= 470, y=590)

entry6 = Entry(canvas,width =20)
entry6.place(x= 620, y=590)

entry7 = Entry(canvas,width =20)
entry7.place(x= 770, y=590)

entry8 = Entry(canvas,width =20)
entry8.place(x= 920, y=590)

entry9 = Entry(canvas,width =20)
entry9.place(x= 1070, y=590)

entry10 = Entry(canvas,width =20)
entry10.place(x= 1220, y=590)


label_4 = Label(canvas, text ="SSIM:",width = 14, bg="#515151",fg="#ffffff")
label_4.place(x= 30, y=630)
entry3 = Entry(canvas,width =20)
entry3.place(x= 170, y=630)
#entry4 = Entry(Frame7,width =38)
entry11 = Entry(canvas,width =20)
entry11.place(x= 320, y=630)

entry12 = Entry(canvas,width =20)
entry12.place(x= 470, y=630)

entry13 = Entry(canvas,width =20)
entry13.place(x= 620, y=630)

entry14 = Entry(canvas,width =20)
entry14.place(x= 770, y=630)

entry15= Entry(canvas,width =20)
entry15.place(x= 920, y=630)

entry16 = Entry(canvas,width =20)
entry16.place(x= 1070, y=630)

entry17 = Entry(canvas,width =20)
entry17.place(x= 1220, y=630)



entry1.grid(row=0, column=1,padx=5, pady=5)
#entry2.grid(row=5, column=1,padx=10, pady=5)
#entry3.grid(row=5, column=4,padx=5, pady=5)
#entry4.grid(row=5, column=7,padx=5, pady=5)



#label_9.pack(side = TOP)
label_5.pack(side = TOP)
label_5.config(font=("Poppins", 14))


root1.mainloop()