import cv2
import numpy as np 
face_detection = cv2.CascadeClassifier('src\haarcascade_frontalface_default.xml')
img = cv2.imread('images/5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_detection.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
cv2.imwrite('write/'+str(x)+'.jpg',img)
cv2.imshow('edge_images',cv2.imread('write/'+str(x)+'.jpg'))
cv2.waitKey(0)
cv2.destroyAllWindow()