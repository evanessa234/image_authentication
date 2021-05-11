from PIL import Image
import numpy as np
import functools




def embedding_info(picname, savename, text):
    text += '#%#' # as the end tag
    im = np.array(Image.open(picname))        
    rows, columns, colors = im.shape
    embed = []
    for c in text:
        bin_sign = (bin(ord(c))[2:]).zfill(16)
        for i in range(16):
            embed.append(int(bin_sign[i]))
    
    count = 0
    for row in range(rows):
        for col in range(columns):
            for color in range(colors):
                if count < len(embed):
                    im[row][col][color] = im[row][col][color] // 2 * 2 + embed[count]
                    count += 1
 
    Image.fromarray(im).save(savename)

def extract_info(picname):
    im = np.array(Image.open(picname))
    rows, columns, colors = im.shape
    text = ""
    extract = np.array([], dtype = int)
 
    count = 0
    for row in range(rows):
        for col in range(columns):
            for color in range(colors):
                extract = np.append(extract, im[row][col][color] % 2)
                count += 1
                if count % 16 == 0:
                    bcode = functools.reduce(lambda x, y: str(x) + str(y), extract)
                    cur_char = chr(int(bcode, 2))
                    text += cur_char
                    if cur_char == '#' and text[-3:] == '#%#':
                        print(text[:-3])
                        print(text[:-3])
                        return text[:-3]
                    extract = np.array([], dtype=int)



text = "Hello, Sampada!"
embedding_info('images/pic3.png', 'images/afternew.png', text)
a = extract_info('images/afternew.png') 
print(a)