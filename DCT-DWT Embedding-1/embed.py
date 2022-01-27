import numpy as np
import pywt
import os
from PIL import Image
from scipy.fftpack import dct
from scipy.fftpack import idct



def convert_image(image_name, size):
    img = Image.open('./pictures/' + image_name).resize((size, size), 1)
    img = img.convert('L')
    img.save('./dataset/' + image_name)

    # image_array = np.array(img)
    # image_array = np.float32(image_array) 
    # image_array /= 255 
    image_array = np.array(img.getdata(), dtype=float).reshape((size, size))
    #print image_array[0][0]               #qrcode white color = 1.0
    #print image_array[10][10]             #qrcode black color = 0.0  

    return image_array

def process_coefficients(imArray, model, level):
    coeffs=pywt.wavedec2(data = imArray, wavelet = model, level = level)
    # print coeffs[0].__len__()
    coeffs_H=list(coeffs) 
   
    return coeffs_H


def embed_mod2(coeff_image, coeff_watermark, offset=0):
    for i in xrange(coeff_watermark.__len__()):
        for j in xrange(coeff_watermark[i].__len__()):
            coeff_image[i*2+offset][j*2+offset] = coeff_watermark[i][j]

    return coeff_image

def embed_mod4(coeff_image, coeff_watermark):
    for i in xrange(coeff_watermark.__len__()):
        for j in xrange(coeff_watermark[i].__len__()):
            coeff_image[i*4][j*4] = coeff_watermark[i][j]

    return coeff_image

            
    
def embed_watermark(watermark_array, orig_image):
    watermark_array_size = watermark_array[0].__len__()
    watermark_flat = watermark_array.ravel()
    ind = 0

    for x in range (0, orig_image.__len__(), 8):
        for y in range (0, orig_image.__len__(), 8):
            if ind < watermark_flat.__len__():
                subdct = orig_image[x:x+8, y:y+8]
                subdct[5][5] = watermark_flat[ind]
                orig_image[x:x+8, y:y+8] = subdct
                ind += 1 


    return orig_image
      


def apply_dct(image_array):
    size = image_array[0].__len__()
    all_subdct = np.empty((size, size))
    for i in range (0, size, 8):
        for j in range (0, size, 8):
            subpixels = image_array[i:i+8, j:j+8]
            subdct = dct(dct(subpixels.T, norm="ortho").T, norm="ortho")
            all_subdct[i:i+8, j:j+8] = subdct

    return all_subdct


def inverse_dct(all_subdct):
    size = all_subdct[0].__len__()
    all_subidct = np.empty((size, size))
    for i in range (0, size, 8):
        for j in range (0, size, 8):
            subidct = idct(idct(all_subdct[i:i+8, j:j+8].T, norm="ortho").T, norm="ortho")
            all_subidct[i:i+8, j:j+8] = subidct

    return all_subidct





