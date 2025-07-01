import cv2
import os

img = cv2.imread(os.path.join('.' , 'data' , 'bali.jpg'))

print(img.shape)

cropped_img = img[320:640,420:840]

cv2.imshow('img' , cropped_img)
cv2.waitKey(0)