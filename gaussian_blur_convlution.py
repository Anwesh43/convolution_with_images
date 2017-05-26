import numpy as np
from ImageConvolution import *
imageConvolution = ImageConvolution('wenger.png')
ga = np.zeros((20,20))
for i in range(20):
    for j in range(20):
        dist = (i-9.5)**2 + (j-9.5)**2
        ga[i][j] = np.exp(-dist/50)
imageConvolution.convolve_and_plot(ga)
