import numpy as np
import pywt
import os
from PIL import Image
from scipy.fftpack import dct
from scipy.fftpack import idct
import embed as em
import extract as ex

current_path = str(os.path.dirname(__file__))  

image = 'x-ray.jpg'   
watermark = 'qrcode.png' 

def print_image_from_array(image_array, name):
    # image_array *= 255;
    # image_array =  np.uint8(image_array)
    image_array_copy = image_array.clip(0, 255)
    image_array_copy = image_array_copy.astype("uint8")
    img = Image.fromarray(image_array_copy)
    img.save('./result/' + name)


def w2d(img):
    model = 'haar'
    level = 1
    image_array = em.convert_image(image, 2048)
    watermark_array = em.convert_image(watermark, 128)

    coeffs_image = em.process_coefficients(image_array, model, level=level)
    #print_image_from_array(coeffs_image[0], 'LL_after_DWT.jpg')

    dct_array = em.apply_dct(coeffs_image[0])
    #print_image_from_array(dct_array, 'LL_after_DCT.jpg')

    dct_array = em.embed_watermark(watermark_array, dct_array)
    #print_image_from_array(dct_array, 'LL_after_embeding.jpg')

    coeffs_image[0] = em.inverse_dct(dct_array)
    #print_image_from_array(coeffs_image[0], 'LL_after_IDCT.jpg')


# reconstruction
    image_array_H=pywt.waverec2(coeffs_image, model)
    print_image_from_array(image_array_H, 'image_with_watermark.jpg')


# recover images[]
    ex.recover_watermark(image_array = image_array_H, model=model, level = level)



w2d("test")