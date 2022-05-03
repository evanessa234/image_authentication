import keygen as kg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread("images/hospital_gray.jpg")

#plt.imshow(img)
#plt.show()

#Generate chaotic keys
height = img.shape[0]
width = img.shape[1]
print(width)
#key = kg.keygen(0.01,3.95,height*width)
#print(key)

#Encryption

#z=0
#enimg = np.zeros(shape=[height,width,4], dtype=np.uint8)
#for i in range(height):
#	for j in range(width):
#		enimg[i,j]=img[i,j]^key[z]
#		z+=1

#plt.imshow(enimg)
#plt.show()
#plt.imsave("processed_images/ChaosEncrypted.jpg", enimg)

