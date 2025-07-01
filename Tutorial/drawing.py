import cv2 , os

img = cv2.imread(os.path.join('.' , 'Tutorial' , 'data' , 'whiteboard.png'))
print(img.shape)

# line - image x1 y1 x2 y2 color thickness
cv2.line(img , (100,150) , (300,450) , (0 , 255 , 0) , 3)

# rectangle - image x1 y1 x2 y2 color thickness
cv2.rectangle(img , (200,350) , (450,600) , (0 , 0 , 255) , 30) # -1 for fill

# circle - image center radius color thickness
cv2.circle(img , (500,190) , 115 , (0 , 255 , 255) , 10) 

# text - image text location font scale color thickness
cv2.putText(img , 'Jay Jr!' , (600,450) , cv2.FONT_HERSHEY_COMPLEX ,2, (255,255,0) , 7)

cv2.imshow('img' , img)

cv2.waitKey(0)