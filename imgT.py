import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('0.jpg', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
# 参数  1,0 :只在  x 方向求1階導數，最大可以求2階導數。
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# 参数  0,1 :只在  y 方向求1階導數，最大可以求2階導數。
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()