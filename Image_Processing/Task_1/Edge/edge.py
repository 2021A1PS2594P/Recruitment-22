import numpy as np
import matplotlib.pyplot as plt

Img=plt.imread('flower.jpg')
vertical_filter=[[-1,-2,-1],[0,0,0],[1,2,1]]
horizontal_filter=[[-1,0,1],[-2,0,2],[-1,0,1]]
edge_Img = np.zeros_like(Img)
n, m, d = Img.shape
for r in range(3, n-2):
    for c in range(3, m-2):
        local_pixels=Img[r-1:r+2, c-1:c+2, 0]
        
        vertical_transformed_pixels = vertical_filter*local_pixels
        vertical_score = vertical_transformed_pixels.sum()/4
        
        horizontal_transformed_pixels = horizontal_filter*local_pixels
        horizontal_score = horizontal_transformed_pixels.sum()/4
        
        edge_score = (vertical_score**2 + horizontal_score**2)**.5
        edge_Img[r,c] = [edge_score]*3
edge_Img = edge_Img/edge_Img.max()

plt.imshow(edge_Img)


