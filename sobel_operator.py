import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.signal import convolve2d
import math
HX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]],np.float32)
HY = HX.T
im = mpimg.imread('wenger.png')
im = im.mean(axis=2)
plt.imshow(im,cmap='gray')
plt.show()
sx_im = convolve2d(im,HX)
plt.imshow(sx_im,cmap='gray')
plt.show()
sy_im = convolve2d(im,HY)
plt.imshow(sy_im,cmap='gray')
plt.show()
s_im = np.sqrt(sx_im*sx_im+sy_im*sy_im)
plt.imshow(s_im,cmap='gray')
plt.show()
