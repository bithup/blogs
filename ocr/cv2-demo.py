import numpy as numpy
import cv2

img = cv2.imread('C:\\Users\\bithup\\Desktop\\0201.jpg')
img_median = cv2.medianBlur(img, 5)
cv2.imwrite('C:\\Users\\bithup\\Desktop\\0201-medianBlur.jpg', img_median)
