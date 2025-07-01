import cv2 , os
import numpy as np

img = cv2.imread(os.path.join('.' , 'Tutorial' , 'data' , 'messi.jpg'))

edge = cv2.Canny(img , 100 , 200)

# thicker
edge_d = cv2.dilate(edge , np.ones((3,3) , dtype=np.int8))
# thinner
edge_e = cv2.erode(edge_d , np.ones((3,3) , dtype=np.int8))

cv2.imshow('messi' , img)
cv2.imshow('edge messi' , edge)
cv2.imshow('edge messi dilate' , edge_d)
cv2.imshow('edge messi erode' , edge_e)
cv2.waitKey(0)