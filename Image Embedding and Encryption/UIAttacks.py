from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
from imageio import imread
import numpy as np
import cv2
import math
from skimage.util import random_noise

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
        cv2.imwrite("./processed_images/attacked_salt&pepper.jpg", img)
        return img

def gaussian_noise():
    img = entry1.get()
    img = cv2.imread(img)
    img = img.copy()
    im_arr = np.asarray(img)
    # can parametrize: clip, mean, var
    noise_img = random_noise(im_arr, mode='gaussian')
    noise_img = (255 * noise_img).astype(np.uint8)
    cv2.imwrite("./processed_images/attacked_gaussiannoise.jpg", noise_img)
    return noise_img

def rotate180():
        img = entry1.get()
        img = cv2.imread(img)
        img = img.copy()
        angle = 180
        scale = 1.0
        w = img.shape[1]
        h = img.shape[0]
        rangle = np.deg2rad(angle)  # angle in radians
        nw = (abs(np.sin(rangle) * h) + abs(np.cos(rangle) * w)) * scale
        nh = (abs(np.cos(rangle) * h) + abs(np.sin(rangle) * w)) * scale
        rot_mat = cv2.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, scale)
        rot_move = np.dot(rot_mat, np.array(
            [(nw - w) * 0.5, (nh - h) * 0.5, 0]))
        rot_mat[0, 2] += rot_move[0]
        rot_mat[1, 2] += rot_move[1]
        rotated_img = cv2.warpAffine(img, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4)
        cv2.imwrite("./processed_images/attacked_roatation180.jpg", rotated_img)
        return rotated_img

def rotate90():
        img = entry1.get()
        img = cv2.imread(img)
        img = img.copy()
        angle = 90
        scale = 1.0
        w = img.shape[1]
        h = img.shape[0]
        rangle = np.deg2rad(angle)  # angle in radians
        nw = (abs(np.sin(rangle) * h) + abs(np.cos(rangle) * w)) * scale
        nh = (abs(np.cos(rangle) * h) + abs(np.sin(rangle) * w)) * scale
        rot_mat = cv2.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, scale)
        rot_move = np.dot(rot_mat, np.array(
            [(nw - w) * 0.5, (nh - h) * 0.5, 0]))
        rot_mat[0, 2] += rot_move[0]
        rot_mat[1, 2] += rot_move[1]
        rotated_img = cv2.warpAffine(img, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4)
        cv2.imwrite("./processed_images/attacked_roatation90.jpg", rotated_img)
        return rotated_img

def cropimg():
        img = entry1.get()
        img = cv2.imread(img)
        rows,cols, _ = img.shape
        crop_img = img[256:512, 30:512]
        cv2.imwrite("./processed_images/attacked_cropping.jpg", crop_img)
        return crop_img


#from tkFileDialog import askopenfilename

def openFileForSaltandPepperNoise():
    window = Toplevel(root1)
    window.title("Salt and Pepper noise")
    window.geometry("700x700")
    path = "./processed_images/attacked.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForRotate180():
    window = Toplevel(root1)
    window.title("Rotation 180°")
    window.geometry("700x700")
    path = "./processed_images/attacked_roatation180.jpg"    
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

def openFileForRotate90():
    window = Toplevel(root1)
    window.title("Rotation 90°")
    window.geometry("700x700")
    path = "./processed_images/attacked_roatation90.jpg"    
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

def openFileForResizing():
    window = Toplevel(root1)
    window.title("Resized image")
    window.geometry("700x700")
    path = "./processed_images/attacked_resizing.jpg"    
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


button2 = Button(Frame2,text="Gaussian Noise",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = gaussian_noise, width=20).grid(row=1, column=0, columnspan= 1, padx=5,pady=5)
button3 = Button(Frame2, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForGaussianNoise).grid(row=1, column=1, padx=5, pady=5)

button4 = Button(Frame2,text="Salt&Pepper Noise",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = saltnoise, width=20).grid(row=1, column=4, columnspan= 1, padx=5,pady=5)
button5 = Button(Frame2, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForSaltandPepperNoise).grid(row=1, column=5,padx=5, pady=5)

button6 = Button(Frame3,text="Rotate 90°",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = rotate90, width=20).grid(row=2, column=0,columnspan= 1 , ipadx= 2, padx=5,pady=5)
button7 = Button(Frame3, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForRotate90).grid(row=2, column=1,padx=5, pady=5)

button8 = Button(Frame3,text="Rotate 180°",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = rotate180, width=20).grid(row=2, column=3,columnspan= 1, padx=5,pady=5)
button9 = Button(Frame3, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForRotate180).grid(row=2, column=5,padx=5, pady=5)

button10 = Button(Frame4,text="Cropping",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = cropimg, width=20).grid(row=3, column=0, columnspan= 1, padx=5,pady=5)
button11 = Button(Frame4, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForCropped).grid(row=3, column=1, padx=5, pady=5)

button12 = Button(Frame4,text="Compression",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = choose_File_1, width=20).grid(row=3, column=3, columnspan= 1, padx=5,pady=5)
button13 = Button(Frame4, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForCompression).grid(row=3, column=5,padx=5, pady=5)

button14 = Button(Frame5,text="Resizing",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = choose_File_1, width=20).grid(row=4, column=0, columnspan= 1, padx=5,pady=5)
button15 = Button(Frame5, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForResizing).grid(row=4, column=1,padx=5, pady=5)

button16 = Button(Frame5,text="Scaling",bg="#ffffff",fg="#000000",activebackground = "#000000",relief = "flat",command = choose_File_1, width=20).grid(row=4, column=3, columnspan= 1, padx=5,pady=5)
button17 = Button(Frame5, text="Open Image",bg="#515151",fg="#ffffff",activebackground = "#000000",relief = "flat",command = openFileForScaling).grid(row=4, column=5,padx=5, pady=5)



entry1.grid(row=0, column=1,padx=5, pady=5)


label_9.pack(side = TOP)
label_5.pack(side = TOP)
label_5.config(font=("Poppins", 14))


root1.mainloop()
