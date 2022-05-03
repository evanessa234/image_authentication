import math
import cv2
import numpy as np
import PIL.Image as Image
import io

def psnr(img1, img2):
        mse = np.mean( (img1 - img2) ** 2 )
        if mse == 0:
            return 100
        PIXEL_MAX = 255.0
        return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
        
def NCIndex(img1,img2):
    return abs(np.mean(np.multiply((img1-np.mean(img1)),(img2-np.mean(img2))))/(np.std(img1)*np.std(img2)))

def ssim(img1, img2):
    C1 = (0.01 * 255)**2
    C2 = (0.03 * 255)**2

    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())

    mu1 = cv2.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(img2, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(img1**2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(img2**2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def calculate_ssim(img1, img2):
    if not img1.shape == img2.shape:
        raise ValueError('Input images must have the same dimensions.')
    if img1.ndim == 2:
        return ssim(img1, img2)
    elif img1.ndim == 3:
        if img1.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim(img1, img2))
            return np.array(ssims).mean()
        elif img1.shape[2] == 1:
            return ssim(np.squeeze(img1), np.squeeze(img2))
    else:
        raise ValueError('Wrong input image dimensions.')

def ber():
        i1 = Image.open('images/img_wm.png')
        i2 = Image.open('processed_images/ArnoldDecryptedWatermark.jpg')
        try:

            #assert i1.mode == i2.mode, "Different kinds of images."
            assert i1.size == i2.size, "Different sizes."
 
            pairs = zip(i1.getdata(), i2.getdata())
            if len(i1.getbands()) == 1:
                dif = sum(abs(p1-p2) for p1,p2 in pairs)
            else:
                dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 
            ncomponents = i1.size[0] * i1.size[1] * 120
            value = (dif / 255.0 * 100) / ncomponents
        except AssertionError as msg:
            print(msg)
        
        return value

def main():
     original = cv2.imread("dataset/cover_img_512.jpg")
     watermarked_img = cv2.imread("processed_images/watermarked_Image_DWT_GRAY_HL.jpg", 1)
     value1 = mse(original, watermarked_img)
     print(f"MSE value is {value1} dB")


     value2 = psnr(original, watermarked_img)
     print(f"PSNR value is {value2} dB")

     value3 = calculate_ssim(original, watermarked_img)
     print(f"SSIM value is {value3} dB")
     

     origwatermark = cv2.imread('images/hospital_gray.jpg')
     extracted_watermark = cv2.imread('processed_images/ArnoldDecryptedWatermark.jpg')
     value4 = NCIndex(origwatermark, extracted_watermark)
     print(f"NCC value is {value4} dB")
       
     ber()
     #rint(f"BER value is {value5} dB")

if __name__ == "__main__":
    main()