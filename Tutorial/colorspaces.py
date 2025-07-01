import cv2
import os


img = cv2.imread(os.path.join('data/bali.jpg'))

img_rgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

cv2.imshow('img hsv' , img_hsv)
cv2.imshow('img' , img)
# cv2.imshow('img RGB' , img_rgb)
# cv2.imshow('img gray' , img_gray)

cv2.waitKey(0)