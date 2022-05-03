import tkinter as Tk
from tkinter import *
import os
import sys
import tkinter.font as font


from PIL import Image,ImageTk

def open_send_info():
    os.system('python UIENC.py')
    

def open_receive_info():
    os.system('python UIDEC.py')

def open_generate_key():
    os.system('python UIAttacks.py')


dashboard = Tk()

dashboard.geometry("1240x750")
dashboard.configure(bg = "#ffffff")
canvas = Canvas(
    dashboard,
    bg = "#1F3943",
    height = 750,
    width = 1240,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

label_1 = Label(dashboard, text ="Medical Image Authentication Using Watermarking",bg= "#1F3943",wraplength=600, justify="left", fg='#ffffff',font=('Helvetica', 30, 'bold'))
label_1.place(x = 160, y = 200)
photo = PhotoImage(file="images/bg.png")
label_2 = Label(dashboard, image = photo)
label_2.place(x = 750, y = 220)
#img0 = PhotoImage(file = f"images/Send_info.png")
buttonFont = font.Font(family='Helvetica', size=16, weight='bold')

b2 = Button(
    dashboard,
    text = "Send information" ,
    borderwidth = 0,
    font=buttonFont,
    highlightthickness = 0,
    bg= "#ffffff",
    fg='#515151',
    command = open_send_info,
    relief = "flat")

b2.place(
    x = 170, y = 350,
    width = 380,
    height = 70)



#img1 = PhotoImage(file = f"images/Receive_info.png")

b3 = Button(
    dashboard,
    font=buttonFont,
    fg='#515151',
    text = "Receive information",
    borderwidth = 0,
    highlightthickness = 0,
    bg= "#ffffff",
    command = open_receive_info,
    relief = "flat")
b3.place(
    x = 170, y = 450,
    width = 380,
    height = 70)


#img2 = PhotoImage(file = f"images/Generate_key.png")
b4 = Button(
    dashboard,
    text = "Perform Attacks" ,
    font=buttonFont,
    fg='#515151',
    borderwidth = 0,
    bg= "#ffffff",
    highlightthickness = 0,
    command = open_generate_key,
    relief = "flat")

b4.place(
    x = 170, y = 550,
    width = 380,
    height = 70)

dashboard.resizable(False, False)
dashboard.mainloop()
