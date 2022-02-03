import numpy as np
import matplotlib.pyplot as plt


image=plt.imread('bees.jpg')
R,G,B=image[:,:,0],image[:,:,1],image[:,:,2]
gray=0.2989*R + 0.5870*G + 0.1140*B
G=plt.imshow(gray,cnap='gray')
plt.show()









        

        


                    
    