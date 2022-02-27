from PIL import Image
from numpy import median


def findTheMedian(row, column, n, height, width, im):
  tmpR,tmpG,tmpB ="","",""
  arrR, arrG, arrB = [],[],[]
  N = int(n)
  k = N//2
  for i in range(N):
      for j in range(N):
          if(row+k-i<0 or row+k-i>height-1):
              tmpR, tmpG, tmpB = 0, 0, 0
          elif(column+k-j<0 or column +k -j > width-1):
              tmpR, tmpG, tmpB = 0, 0, 0
          else:
              tmpR,tmpG,tmpB = im.getpixel((column+k-j, row+k-i))
          arrR.append(tmpR)
          arrG.append(tmpG)
          arrB.append(tmpB)
  medianR = int(median(arrR))
  medianG = int(median(arrG))
  medianB = int(median(arrB))
  arrB, arrG, arrR.clear()
  return medianR, medianG, medianB

def setup():
  fileName = input("\nEnter file name here: ")
  im = Image.open(fileName)
  rgb_im = im.convert('RGB')
  rgb_im.save('img1.jpg')
  im = Image.open('img1.jpg')
  return im


def getInput():
  try:
      im = setup()
      width, height = im.size
      im.show()
      return im, width, height
  except:
      userInput = input("File not found! \nEnter 'exit' to exit OR anything else to continue.")
      if (userInput == "exit") or (userInput == 'EXIT') or (userInput == 'Exit'):
           exit()
      else:
          return getInput()


def getN():
   try:
       temp = int(input("Input window size, i.e. 3 for 3x3..."))
       print(repr(temp))
       if temp>=2 and temp <=10:
           return temp
       else:
           print("\n**********Window size range is 2 to 10**********")
           return getN()
   except:
       print("\n**********Wrong input! Try again.**********")
       getN()


def main():
   im, width, height = getInput()
   img= Image.new(im.mode, im.size) #without changing the image value
   pixelMap = im.load()
   pixelMapNew = img.load() # pixelmap of new image
   N = getN()

   print("Image is Processing.", end="")
   for i in range(0, height):
       if (i % 50 == 0): print(".", end="")
       for j in range(0, width):
           #pixelMap[j, i] = findTheMedian(i, j, N, height, width, im) #changes the original image
           pixelMapNew[j, i] = findTheMedian(i, j, N, height, width, im) #without changing the original image
   img.show()  #new image
   img.save('new.jpg') #new image
   #im.show()
   #im.save('new.jpg')

   print("\nDONE")

   ui = input("Press 0 to filter another Image, 1 to exit!")
   if (ui == '0'):
       main()
   else:
       exit()


if __name__ == '__main__':

   main()
