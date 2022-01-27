import ImageMatrix as iM
import generateHenonMap as ghm
from PIL import Image
import os
from matplotlib.pyplot import imshow
import numpy as np
from cv2 import cv2

def HenonDecryption(imageNameEnc):
    im = np.array(Image.open(imageNameEnc))
    if len(im.shape)<3:
        imageMatrix, size = iM.getImageMatrix_gray(imageNameEnc) 
        transformationMatrix = ghm.genHenonMap(size)
        henonDecryptedImage = []
        for i in range(len(imageMatrix)):
            row = []
            for j in range(len(imageMatrix)):
                try:
                    row.append(imageMatrix[i][j] ^ transformationMatrix[i][j])
                except:
                    row = [imageMatrix[i][j] ^ transformationMatrix[i][j]]

            try:
                henonDecryptedImage.append(row)
            except:
                henonDecryptedImage = [row]

        width  = len(imageMatrix[0])
        height = len(imageMatrix)

        im = Image.new("L", (width, height))


    elif len(im.shape)==3:
        imageMatrix, size, color = iM.getImageMatrix(imageNameEnc) 
        transformationMatrix = ghm.genHenonMap(size)
        henonDecryptedImage = []
        for i in range(size):
            row = []
            for j in range(size):
                try:
                    row.append(tuple([transformationMatrix[i][j] ^ x for x in imageMatrix[i][j]]))
                except:
                    row = [tuple([transformationMatrix[i][j] ^ x for x in imageMatrix[i][j]])]
            try:
                henonDecryptedImage.append(row)
            except:
                henonDecryptedImage = [row]

        im = Image.new("RGB", (size, size))
    

    pix = im.load()
    for x in range(size):
        for y in range(size):
            pix[x, y] = henonDecryptedImage[x][y]
    im.save("HenonDec.png", "PNG")
    absPath = os.path.abspath("HenonDec.png")
    return absPath