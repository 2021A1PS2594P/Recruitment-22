import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageOps



img=plt.imread('hills.jpg')

img=img.sum(axis=-1)
def blur(img):
    for i in range(1,img.shape[0]-1):
        for j in range(1,img.shape[1]-1):
            img[i,j]=(4*img[i,j]+ img[i-1,j] + img[i+1,j] + img[i,j+1])/8.0
    return img

blur(img)
plt.imshow(img,cmap='gray')

