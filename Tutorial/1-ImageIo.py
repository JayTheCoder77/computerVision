import cv2
import os

# read image 

image_path = os.path.join('.' , 'data' , 'bali.jpg')

img = cv2.imread(image_path)

# write image

cv2.imwrite(os.path.join('.' , 'data' , 'bali_out.jpg') , img)

# visualize image

cv2.imshow('bali' , img)
cv2.waitKey(0) 
# cv2.waitKey(5000) closes after 5 seconds 

