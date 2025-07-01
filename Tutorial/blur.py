import cv2 , os , requests
import numpy as np

url = 'https://ars.els-cdn.com/content/image/3-s2.0-B978012374457900007X-f07-06.jpg'
response = requests.get(url)

img_array = np.array(bytearray(response.content), dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)



k_size = 3
# blurred_img = cv2.blur(img , (k_size , k_size))
# blurred_img = cv2.GaussianBlur(img , (k_size , k_size) , 8)
blurred_img = cv2.medianBlur(img , k_size)

cv2.imshow('img' , img)
cv2.imshow('blurred_img' , blurred_img)
cv2.waitKey(0)
