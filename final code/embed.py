import logging
import cv2
import numpy as np
import pywt
import dwt_rgb as dr

logging.basicConfig(level=logging.DEBUG)

IMAGES_DIR = "processed_images\\"
RGB_WATERMARKING_CONDITION = 0.10




def DWT_RGB_HL_EMBED(coverImagePath, watermarkImagePath):
    image = Image.open(coverImagePath)
    newsize = (512, 512)
    new_image = image.resize(newsize)
    new_image.save("dataset//cover_img_512.jpg")
    cover_img = read_file("dataset//cover_img_512.jpg", "RGB")
    watermark_img = read_file(watermarkImagePath, "RGB")

    cover_red_dwt_layers, cover_green_dwt_layers, cover_blue_dwt_layers = dr.dwt_rgb_image(cover_img)

    watermark_red_dwt_layers, watermark_green_dwt_layers, watermark_blue_dwt_layers = dr.dwt_rgb_image(watermark_img)

    watermarked_cover_img_HL = embed_watermark_to_HL_rgb(cover_red_dwt_layers, cover_green_dwt_layers,
                                                         cover_blue_dwt_layers, watermark_red_dwt_layers,
                                                         watermark_green_dwt_layers,
                                                         watermark_blue_dwt_layers)

    cover_red_dwt_layers[2] = watermarked_cover_img_HL[0]
    cover_green_dwt_layers[2] = watermarked_cover_img_HL[1]
    cover_blue_dwt_layers[2] = watermarked_cover_img_HL[2]

    red_channel, green_channel, blue_channel = dr.reverse_dwt_rgb(cover_red_dwt_layers, cover_green_dwt_layers,
                                                               cover_blue_dwt_layers)

    watermarked_img = dr.combine_rgb_channels_to_bgr_img(red_channel, green_channel, blue_channel)

    out_path = IMAGES_DIR + 'watermarked_image_DWT_RGB_HL.jpg'
    cv2.imwrite(out_path, watermarked_img)

    return out_path


def embed_watermark_to_HL_rgb(cover_red_layers, cover_green_layers, cover_blue_layers, watermark_red, watermark_green,
                              watermark_blue):
    watermarked_red = cover_red_layers[2] + RGB_WATERMARKING_CONDITION * watermark_red[2]
    watermarked_green = cover_green_layers[2] + RGB_WATERMARKING_CONDITION * watermark_green[2]
    watermarked_blue = cover_blue_layers[2] + RGB_WATERMARKING_CONDITION * watermark_blue[2]
    return watermarked_red, watermarked_green, watermarked_blue




#GRAYSCALE IMAGE


GRAY_WATERMARKING_CONDITION = 0.1
def DWT_GRAY_HL_EMBED(coverImagePath, watermarkImagePath):
    
    cover_img = read_file(coverImagePath, "GRAY")
    watermark_img = read_file(watermarkImagePath, "GRAY")

    # DWT on cover image
    cover_ll, (cover_LH, cover_HL, cover_HH) = pywt.dwt2(cover_img, 'haar')

    # DWT on watermark image
    watermark_ll, (watermark_LH, watermark_HL, watermark_HH) = pywt.dwt2(watermark_img, 'haar')

    # Embedding watermark
    coeffW = (cover_ll, (cover_LH, cover_HL + GRAY_WATERMARKING_CONDITION * watermark_HL, cover_HH))

    watermarked_img = pywt.idwt2(coeffW, 'haar')
    out_path = IMAGES_DIR + 'watermarked_Image_DWT_GRAY_HL.jpg'
    cv2.imwrite(out_path, watermarked_img)

    return out_path


    
def read_file(path, color):  # color == GRAY or RGB
    if color == "GRAY":
        img = cv2.imread(path, 0)
        return img
    elif color == "RGB":
        img = cv2.imread(path, 8)
        return img
    else:
        print("failed to read image")


# Run rgb tests
if __name__ == "__main__":
    #coverImagePath = 'images\\mandrill_512.jpg'
    #watermarkImagePath = 'images\\lenna_512.jpg'
    #watermarked_img = 'images\\watermarked_LogisticDec_HenonDec.png'
    #watermarked_img_rbg = DWT_RGB_LL_EMBED(coverImagePath, watermarkImagePath)
    #extracted_img_rbg = DWT_RGB_LL_EXTRACT(coverImagePath, watermarkImagePath, read_file(watermarked_img_rbg, "RGB"))

    DWT_RGB_HL_EMBED(coverImagePath, watermarkImagePath)
    DWT_GRAY_HL_EMBED(coverImagePath, watermarkImagePath)

    #extracted_img_rbg = DWT_RGB_HL_EXTRACT(coverImagePath, watermarkImagePath, read_file(watermarked_img, "RGB"))