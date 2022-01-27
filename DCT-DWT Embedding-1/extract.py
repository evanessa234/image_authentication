import numpy as np
import pywt
import os
from PIL import Image
from scipy.fftpack import dct
from scipy.fftpack import idct
import embed as em

def get_watermark(dct_watermarked_coeff, watermark_size):
    # watermark = [[0 for x in range(watermark_size)] for y in range(watermark_size)] 

    subwatermarks = []

    for x in range (0, dct_watermarked_coeff.__len__(), 8):
        for y in range (0, dct_watermarked_coeff.__len__(), 8):
            coeff_slice = dct_watermarked_coeff[x:x+8, y:y+8]
            subwatermarks.append(coeff_slice[5][5])

    watermark = np.array(subwatermarks).reshape(watermark_size, watermark_size)

    return watermark


def recover_watermark(image_array, model='haar', level = 1):


    coeffs_watermarked_image = em.process_coefficients(image_array, model, level=level)
    dct_watermarked_coeff = em.apply_dct(coeffs_watermarked_image[0])
    

    watermark_array = get_watermark(dct_watermarked_coeff, 128)

    # watermark_array *= 255;
    watermark_array =  np.uint8(watermark_array)

#Save result
    img = Image.fromarray(watermark_array)
    img.save('./result/eye_HenonEnc_LogisticEnc.png')







