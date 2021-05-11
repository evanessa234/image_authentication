from PIL import Image
import numpy as np
import functools

def embedding_info(picname, savename, text):
    text += '#%#' # as the end tag
    im = np.array(Image.open(picname))        
    rows, columns = im.shape
    embed = []
    for c in text:
        bin_sign = (bin(ord(c))[2:]).zfill(16)
        for i in range(16):
            embed.append(int(bin_sign[i]))
    
    count = 0
    for row in range(rows):
        for col in range(columns):
                if count < len(embed):
                    im[row][col] = im[row][col] // 2 * 2 + embed[count]
                    count += 1
 
    Image.fromarray(im).save(savename)


def extract_info(picname):
    im = np.array(Image.open(picname))
    rows, columns = im.shape
    text = ""
    extract = np.array([], dtype = int)
 
    count = 0
    for row in range(rows):
        for col in range(columns):
                extract = np.append(extract, im[row][col] % 2)
                count += 1
                if count % 16 == 0:
                    bcode = functools.reduce(lambda x, y: str(x) + str(y), extract)
                    cur_char = chr(int(bcode, 2))
                    text += cur_char
                    if cur_char == '#' and text[-3:] == '#%#':
                        print(text[:-3])
                    extract = np.array([], dtype=int)


                 
    
if __name__ == '__main__':
    text = "Hello, Sampada!"
    embedding_info('images/testEncryp.png', 'images/graylena.png', text)
    extract_info('images/graylena.png') 
