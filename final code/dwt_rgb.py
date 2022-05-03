import logging
import cv2
import numpy as np
import pywt


def reverse_dwt_rgb(watermark_red, watermark_green, watermark_blue):
    red_channel = pywt.idwt2(
        (watermark_red[0], (watermark_red[1], watermark_red[2], watermark_red[3])), 'haar')
    green_channel = pywt.idwt2(
        (watermark_green[0], (watermark_green[1], watermark_green[2], watermark_green[3])), 'haar')
    blue_channel = pywt.idwt2(
        (watermark_blue[0], (watermark_blue[1], watermark_blue[2], watermark_blue[3])), 'haar')
    return red_channel, green_channel, blue_channel


def combine_rgb_channels_to_bgr_img(red, green, blue):
    bgr_img = np.dstack((blue, green, red))  # BGR format
    return bgr_img


def dwt_rgb_image(coverImage):
    # get color cover chanels BGR
    cover_red1 = coverImage[:, :, 2]
    cover_green1 = coverImage[:, :, 1]
    cover_blue1 = coverImage[:, :, 0]
    # dwt on cover image on particular color channels
    cr_LL, (cr_LH, cr_HL, cr_HH) = pywt.dwt2(cover_red1, 'haar')
    cg_LL, (cg_LH, cg_HL, cg_HH) = pywt.dwt2(cover_green1, 'haar')
    cb_LL, (cb_LH, cb_HL, cb_HH) = pywt.dwt2(cover_blue1, 'haar')
    return [cr_LL, cr_LH, cr_HL, cr_HH], [cg_LL, cg_LH, cg_HL, cg_HH], [cb_LL, cb_LH, cb_HL, cb_HH]
