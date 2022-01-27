import ImageMatrix as iM
from PIL import Image
import os
from matplotlib.pyplot import imshow
import numpy as np
from cv2 import cv2


def LogisticDecryption(imageName, key):
    N = 256
    key_list = [ord(x) for x in key]

    G = [key_list[0:4] ,key_list[4:8], key_list[8:12]]
    g = []
    R = 1
    for i in range(1,4):
        s = 0
        for j in range(1,5):
            s += G[i-1][j-1] * (10**(-j))
        g.append(s)
        R = (R*s) % 1
    
    L_x = (R + key_list[12]/256) % 1
    S_x = round(((g[0]+g[1]+g[2])*(10**4) + L_x *(10**4)) % 256)
    V1 = sum(key_list)
    V2 = key_list[0]
    for i in range(1,13):
        V2 = V2 ^ key_list[i]
    V = V2/V1

    L_y = (V+key_list[12]/256) % 1
    S_y = round((V+V2+L_y*10**4) % 256)
    C1_0 = S_x
    C2_0 = S_y
    
    C = round((L_x*L_y*10**4) % 256)
    I_prev = C
    I_prev_r = C
    I_prev_g = C
    I_prev_b = C
    I = C
    I_r = C
    I_g = C
    I_b = C
    x_prev = 4*(S_x)*(1-S_x)
    y_prev = 4*(L_x)*(1-S_y)
    x = x_prev
    y = y_prev

    im = np.array(Image.open(imageName))
    if len(im.shape)<3:
        imageMatrix, size = iM.getImageMatrix_gray(imageName) 
        henonDecryptedImage = []
        for i in range(size):
            row = []
            for j in range(size):
                while x <0.8 and x > 0.2 :
                    x = 4*x*(1-x)
                while y <0.8 and y > 0.2 :
                    y = 4*y*(1-y)
                x_round = round((x*(10**4))%256)
                y_round = round((y*(10**4))%256)
                C1 = x_round ^ ((key_list[0]+x_round) % N) ^ ((C1_0 + key_list[1])%N)
                C2 = x_round ^ ((key_list[2]+y_round) % N) ^ ((C2_0 + key_list[3])%N) 
                
                I = ((((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((I_prev+key_list[7]) % N) ^ imageMatrix[i][j]) + N-key_list[6])%N
                I_prev = imageMatrix[i][j]
                row.append(I)
                x = (x +  imageMatrix[i][j]/256 + key_list[8]/256 + key_list[9]/256) % 1
                y = (x +  imageMatrix[i][j]/256 + key_list[8]/256 + key_list[9]/256) % 1
                for ki in range(12):
                    key_list[ki] = (key_list[ki] + key_list[12]) % 256
                    key_list[12] = key_list[12] ^ key_list[ki]
            henonDecryptedImage.append(row)
        
        im = Image.new("L", (size, size)) # L is for Black and white pixels



    elif len(im.shape)==3:
        imageMatrix, size, color = iM.getImageMatrix(imageName) 
        henonDecryptedImage = []
        for i in range(size):
            row = []
            for j in range(size):
                while x <0.8 and x > 0.2 :
                    x = 4*x*(1-x)
                while y <0.8 and y > 0.2 :
                    y = 4*y*(1-y)
                x_round = round((x*(10**4))%256)
                y_round = round((y*(10**4))%256)
                C1 = x_round ^ ((key_list[0]+x_round) % N) ^ ((C1_0 + key_list[1])%N)
                C2 = x_round ^ ((key_list[2]+y_round) % N) ^ ((C2_0 + key_list[3])%N) 
                
                I_r = ((((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((I_prev_r + key_list[7]) % N) ^ imageMatrix[i][j][0]) + N-key_list[6])%N
                I_g = ((((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((I_prev_g + key_list[7]) % N) ^ imageMatrix[i][j][1]) + N-key_list[6])%N
                I_b = ((((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((I_prev_b + key_list[7]) % N) ^ imageMatrix[i][j][2]) + N-key_list[6])%N
                I_prev_r = imageMatrix[i][j][0]
                I_prev_g = imageMatrix[i][j][1]
                I_prev_b = imageMatrix[i][j][2]
                row.append((I_r,I_g,I_b))
                x = (x +  imageMatrix[i][j][0]/256 + key_list[8]/256 + key_list[9]/256) % 1
                y = (x +  imageMatrix[i][j][0]/256 + key_list[8]/256 + key_list[9]/256) % 1  
                for ki in range(12):
                    key_list[ki] = (key_list[ki] + key_list[12]) % 256
                    key_list[12] = key_list[12] ^ key_list[ki]
            henonDecryptedImage.append(row)
        
        im = Image.new("RGB", (size, size))
        


    pix = im.load()
    for x in range(size):
        for y in range(size):
            pix[x, y] = henonDecryptedImage[x][y]
    im.save("LogisticDec.png", "PNG")
    absPath = os.path.abspath("LogisticDec.png")
    return absPath