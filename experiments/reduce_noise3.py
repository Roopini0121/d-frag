import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('sample1.jpg')
dst = cv.fastNlMeansDenoisingColored(img,None,10000,100,7,21)
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()