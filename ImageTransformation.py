import generateHenonMap as ghm
import ImageMatrix as iM
from PIL import Image
import os
from imageio import imread
import numpy as np


def pixelManipulation(imageName):
    im = np.array(Image.open(imageName))
    if len(im.shape)<3:
        imageMatrix, size = iM.getImageMatrix_gray(imageName) 
        transformationMatrix = ghm.genHenonMap(size)
        resultantMatrix = []
        for i in range(size):
            row = []
            for j in range(size):
                try:
                    row.append(transformationMatrix[i][j] ^ imageMatrix[i][j])
                except:
                    row = [transformationMatrix[i][j] ^ x for x in imageMatrix[i][j]]
            try:
                resultantMatrix.append(row)
            except:
                resultantMatrix = [row]
        

        # mode = "L", here mode L stands for black and white and Size = "512 * 512"
        #Creating Henon Transformed Image from resultant matrix
        im = Image.new("L", (size, size))
    


    elif len(im.shape)==3:
        imageMatrix, size, color = iM.getImageMatrix(imageName) 
        transformationMatrix = ghm.genHenonMap(size)
        resultantMatrix = []
        for i in range(size):
            row = []
            for j in range(size):
                try:
                   row.append(tuple([transformationMatrix[i][j] ^ x for x in imageMatrix[i][j]]))
                except:
                   row = [tuple([transformationMatrix[i][j] ^ x for x in imageMatrix[i][j]])]  
            try:    
                resultantMatrix.append(row)
            except:
                resultantMatrix = [row]
        im = Image.new("RGB", (size, size))
    
    

    pix = im.load()
    for x in range(size):
        for y in range(size):
            pix[x, y] = resultantMatrix[x][y]
    im.save("HenonEnc.png", "PNG")
    absPath = os.path.abspath("HenonEnc.png")
    return absPath
