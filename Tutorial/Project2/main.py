import cv2  , os
import mediapipe as mp
# read -> detect -> blur -> save

img = cv2.imread(os.path.join('.' , 'Tutorial' , 'data' , 'face.jpg'))

mp_face_detection = 

cv2.imshow('img' , img)
cv2.waitKey(0)