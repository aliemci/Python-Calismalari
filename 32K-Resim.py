import numpy as np
import math
import cv2

pi = 3.1415

width = 18000
height = 32000

part = 16

partWidth = int(width/part)
partHeigth = int(height/part)

partPi = 2*pi/part

img = np.memmap('img.mymemmap', dtype='uint8', mode='w+', shape=(width, height, 3))

for indexX in range(part):

    sayi_listesi_x = np.mod(np.linspace(indexX*partPi, (indexX+1)*partPi, partWidth), 2*pi)
    
    for indexY in range(part):
    
        sayi_listesi_y = np.mod(np.linspace(indexY*partPi, (indexY+1)*partPi, partHeigth), 2*pi)

        x,y = np.meshgrid(sayi_listesi_x, sayi_listesi_y)

        sayi_listesi = np.multiply(x,y)

        sayi_listesi = sayi_listesi.transpose()

        sayi_listesi_0 = np.sin(sayi_listesi) * 255
        sayi_listesi_1 = np.cos(sayi_listesi) * 255

        sayi_listesi_0 = sayi_listesi_0.astype(np.uint8)
        sayi_listesi_1 = sayi_listesi_1.astype(np.uint8)
        sayi_listesi = sayi_listesi.astype(np.uint8)

        img[indexX*partWidth:(indexX+1)*partWidth, indexY*partHeigth:(indexY+1)*partHeigth, :] = np.ones((partWidth, partHeigth, 3), np.uint8)
        img[indexX*partWidth:(indexX+1)*partWidth, indexY*partHeigth:(indexY+1)*partHeigth, 0] *= sayi_listesi_0
        img[indexX*partWidth:(indexX+1)*partWidth, indexY*partHeigth:(indexY+1)*partHeigth, 1] *= sayi_listesi_1
        img[indexX*partWidth:(indexX+1)*partWidth, indexY*partHeigth:(indexY+1)*partHeigth, 2] *= sayi_listesi_0 + sayi_listesi_1

cv2.imwrite("Photo1.jpg", img)
