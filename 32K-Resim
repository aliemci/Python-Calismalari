import numpy as np
import math
import cv2

img = np.memmap('img.mymemmap', dtype='uint8', mode='w+', shape=(32000,18000,3))

sayi_listesi_x = np.linspace(0,255,16000)
sayi_listesi_y = np.linspace(0,255,9000)

x,y = np.meshgrid(sayi_listesi_x, sayi_listesi_y)

del sayi_listesi_x
del sayi_listesi_y

sayi_listesi = np.multiply(x,y)

del x
del y

sayi_listesi = sayi_listesi.reshape((16000,9000))

sayi_listesi_0 = np.sin(sayi_listesi) * 255
sayi_listesi_1 = np.cos(sayi_listesi) * 255

sayi_listesi_0 = sayi_listesi_0.astype(np.uint8)
sayi_listesi_1 = sayi_listesi_1.astype(np.uint8)
sayi_listesi = sayi_listesi.astype(np.uint8)

img[0:16000,0:9000,:] = np.ones((16000,9000,3), np.uint8)
img[0:16000,0:9000,0] *= sayi_listesi_0
img[0:16000,0:9000,1] *= sayi_listesi_1
img[0:16000,0:9000,2] *= sayi_listesi

img[0:16000,9000:18000,0] = img[0:16000,0:9000,0]
img[0:16000,9000:18000,1] = img[0:16000,0:9000,1]
img[0:16000,9000:18000,2] = img[0:16000,0:9000,2]

img[16000:32000,0:9000,0] = img[0:16000,0:9000,0]
img[16000:32000,0:9000,1] = img[0:16000,0:9000,1]
img[16000:32000,0:9000,2] = img[0:16000,0:9000,2]

img[16000:32000,9000:18000,0] = img[0:16000,0:9000,0]
img[16000:32000,9000:18000,1] = img[0:16000,0:9000,1]
img[16000:32000,9000:18000,2] = img[0:16000,0:9000,2]


cv2.imwrite("Photo2.jpg", img)
