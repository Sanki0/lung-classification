# -*- coding: utf-8 -*-
"""semana1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nmW2q7t3c1AlRGDH4NHEogsgluxi1txT

Types of kernel: \
https://aishack.in/tutorials/image-convolution-examples/ \
https://en.wikipedia.org/wiki/Kernel_(image_processing) \
To read: \
https://arxiv.org/ftp/arxiv/papers/1806/1806.07996.pdf
"""

import numpy as np
import matplotlib.pyplot as ptl
from skimage.io import imread, imshow, imsave
from PIL import Image
from scipy.signal import convolve2d


def shit(filename):
    im = imread('./static/uploads/{}'.format(filename))
    im_arr = np.asarray(im)


    im_copy = im_arr.copy()

    kernel = np.array([[-1, -1, -1], [2, 2, 2], [-1, -1, -1]]).T
    pic_out = convolve2d(im_copy, kernel, mode='same')

    im= Image.fromarray(np.abs(pic_out))

    # im_copy=Image.fromarray(np.abs(im_copy))

    #return im.show()
    return im
    # return im_copy

#shit('descarga.png')