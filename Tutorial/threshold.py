import cv2
import os

# simple threshold

bali_img = cv2.imread(os.path.join('.' , 'data' , 'bali.jpg'))
bali_resize_img = cv2.resize(bali_img , (640,480))
gray_img = cv2.cvtColor(bali_resize_img , cv2.COLOR_BGR2GRAY)

# pixels > 80 will be set to 255
ret , thresh = cv2.threshold(gray_img , 80 , 255 , cv2.THRESH_BINARY)

simple_thresh = cv2.blur(thresh , (2,2))

ret , thresh = cv2.threshold(thresh , 80 , 255 , cv2.THRESH_BINARY)

# adaptive threshold


img = cv2.imread(os.path.join('.' , 'data' , 'handwritten.png'))

gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray_img , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 21 , 30)

cv2.imshow('img' , img)
cv2.imshow('threshold' , simple_thresh)
cv2.imshow('threshold' , thresh)
cv2.waitKey(0)

