import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import pandas as pd

from skimage.color import rgb2gray
from skimage.transform import rescale, resize, downscale_local_mean

from skimage import data, color, feature
from skimage.feature import hog

img_test_path = './fruits-360_dataset/fruits-360/test-multiple_fruits/apple_apricot_nectarine_peach_peach(flat)_pomegranate_pear_plum.jpg'

def showImg(img, name):
    plt.axis("off")
    plt.title(name)
    plt.imshow(img)
    plt.show()

def ExtractHOG(img):
    ftr, hog_image =hog(img, orientations=8, pixels_per_cell=(16, 16),
            cells_per_block=(1, 1), visualize=True, multichannel=False)
    print(hog_image)
    return ftr

img = cv2.imread(img_test_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = mpimg.imread(img_test_path)
imgplot = plt.imshow(img)

