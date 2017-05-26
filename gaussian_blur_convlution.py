import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.signal import convolve2d
im = mpimg.imread('wenger.png')
im = im.mean(axis=2)
print im.shape
plt.imshow(im,cmap='gray')
plt.show()

ga = np.zeros((20,20))
for i in range(20):
    for j in range(20):
        dist = (i-9.5)**2 + (j-9.5)**2
        ga[i][j] = np.exp(-dist/50)
plt.imshow(ga,cmap='gray')
plt.show()
im_ga_c = convolve2d(im,ga)
plt.imshow(im_ga_c,cmap='gray')
plt.show()
