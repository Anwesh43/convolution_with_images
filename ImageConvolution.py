import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.signal import convolve2d
class ImageConvolution:
    def __init__(self,image):
        im = mpimg.imread('wenger.png')
        self.im = im.mean(axis=2)
    def convolve_and_plot(self,A):
        im_convolved = convolve2d(self.im,A)
        plt.imshow(im_convolved,cmap='gray')
        plt.show()
