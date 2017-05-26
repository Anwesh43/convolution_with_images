import numpy as np
from ImageConvolution import *

HX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]],np.float32)
HY = HX.T
imageConvolution = ImageConvolution('wenger.png')
sx_im = imageConvolution.convolve_and_plot(HX)
sy_im = imageConvolution.convolve_and_plot(HY)
s_im = np.sqrt(sx_im*sx_im+sy_im*sy_im)
plt.imshow(s_im,cmap='gray')
plt.show()
