import logging
import cv2
import numpy as np
import pywt
import dwt_rgb as dr

logging.basicConfig(level=logging.DEBUG)

IMAGES_DIR = "processed_images\\"
RGB_WATERMARKING_CONDITION = 0.10


def DWT_RGB_HL_EXTRACT(coverImagePath, watermarkImagePath, watermarked_img):
    cover_img = read_file(coverImagePath, "RGB")
    watermark_img = read_file(watermarkImagePath, "RGB")
    watermarked_img = read_file(watermarked_img, "RGB")

    cover_red_dwt_layers, cover_green_dwt_layers, cover_blue_dwt_layers = dr.dwt_rgb_image(cover_img)

    watermark_red_dwt_layers, watermark_green_dwt_layers, watermark_blue_dwt_layers = dr.dwt_rgb_image(watermark_img)

    watermarked_red_layers, watermarked_green_layers, watermarked_blue_layers = dr.dwt_rgb_image(watermarked_img)

    extracted_watermark_HL = extract_watermark_from_HL_rgb(cover_red_dwt_layers, cover_green_dwt_layers,
                                                           cover_blue_dwt_layers,
                                                           watermarked_red_layers, watermarked_green_layers,
                                                           watermarked_blue_layers)
    watermark_red_dwt_layers[2] = extracted_watermark_HL[0]
    watermark_green_dwt_layers[2] = extracted_watermark_HL[1]
    watermark_blue_dwt_layers[2] = extracted_watermark_HL[2]

    red_channel, green_channel, blue_channel = dr.reverse_dwt_rgb(
        watermark_red_dwt_layers, watermark_green_dwt_layers, watermark_blue_dwt_layers
    )

    extracted_watermark = dr.combine_rgb_channels_to_bgr_img(red_channel, green_channel, blue_channel)

    out_path = IMAGES_DIR + 'extracted_watermark_DWT_RBG_HL.jpg'
    cv2.imwrite(out_path, extracted_watermark)

    return out_path


def extract_watermark_from_HL_rgb(cover_red_layers, cover_green_layers, cover_blue_layers, watermarked_red,
                                  watermarked_green, watermarked_blue):
    extracted_watermark_red = (watermarked_red[2] - cover_red_layers[2]) / RGB_WATERMARKING_CONDITION
    extracted_watermark_green = (watermarked_green[2] - cover_green_layers[2]) / RGB_WATERMARKING_CONDITION
    extracted_watermark_blue = (watermarked_blue[2] - cover_blue_layers[2]) / RGB_WATERMARKING_CONDITION
    return extracted_watermark_red, extracted_watermark_green, extracted_watermark_blue




#grayscale
GRAY_WATERMARKING_CONDITION = 0.1

def DWT_GRAY_HL_EXTRACT(coverImagePath, watermarkImagePath, watermarked_img):
    cover_img = read_file(coverImagePath, "GRAY")
    watermark_img = read_file(watermarkImagePath, "GRAY")
    watermarked_img = read_file(watermarked_img, "GRAY")

    cover_LL, (cover_LH, cover_HL, cover_HH) = pywt.dwt2(cover_img, 'haar')
    watermark_LL, (watermark_LH, watermark_HL, watermark_HH) = pywt.dwt2(watermark_img, 'haar')
    watermarked_LL, (watermarked_LH, watermarked_HL, watermarked_HH) = pywt.dwt2(watermarked_img, 'haar')

    extracted_watermark = extract_gray_watermark_HL(cover_HL, watermarked_HL)

    extracted_watermark = pywt.idwt2((watermark_LL, (watermark_LH, extracted_watermark, watermark_HH)), 'haar')
    extracted_watermark = np.uint8(extracted_watermark)

    out_path = IMAGES_DIR + 'extracted_watermark_DWT_GRAY_HL.jpg'
    cv2.imwrite(out_path, extracted_watermark)

    return out_path


def extract_gray_watermark_HL(cover_band, watermarked_band):
    extracted_watermark = (watermarked_band - cover_band) / GRAY_WATERMARKING_CONDITION
    return extracted_watermark



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
    coverImagePath = 'images\\mandrill_512.jpg'
    watermarkImagePath = 'images\\lenna_512.jpg'
    watermarked_img = 'images\\watermarked_LogisticDec_HenonDec.png'
    #watermarked_img_rbg = DWT_RGB_LL_EMBED(coverImagePath, watermarkImagePath)
    #extracted_img_rbg = DWT_RGB_LL_EXTRACT(coverImagePath, watermarkImagePath, read_file(watermarked_img_rbg, "RGB"))

    #watermarked_img_rbg = DWT_RGB_HL_EMBED(coverImagePath, watermarkImagePath)
    DWT_RGB_HL_EXTRACT(coverImagePath, watermarkImagePath, watermarked_img) 
    DWT_GRAY_HL_EXTRACT(coverImagePath, watermarkImagePath, watermarked_img) 