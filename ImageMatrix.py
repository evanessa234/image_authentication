from PIL import Image

def getImageMatrix(image):
    im = Image.open(image) 
    pix = im.load()
    color = 1
    if type(pix[0,0]) == int:
      color = 0
    image_size = im.size 
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
           try:
               #Getting only the blue pixels
                row.append((pix[width,height]))
           except:
                row=[pix[width, height]]
        try:
            image_matrix.append(row)
        except:
            image_matrix = [row]
                
    return image_matrix,image_size[0],color


def getImageMatrix_gray(imageName):
    im = Image.open(imageName)
    pix = im.load()
    image_size = im.size 
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
           try:
               #Getting only the blue pixels
                row.append((pix[width,height]))
           except:
                row=[pix[width, height]]
        try:
            image_matrix.append(row)
        except:
            image_matrix = [row]
    return image_matrix,image_size[0]