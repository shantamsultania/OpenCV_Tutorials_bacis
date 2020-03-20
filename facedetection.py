import cv2

#importing image
img = cv2.imread('ttr.jpg')

#importing haarcascade
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#grey scale conversion
face_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#search for the co-ordinates of the image
face_de = face.detectMultiScale(face_grey, scaleFactor = 1.05, minNeighbors=5)

for x,y,w,h in face_de:
    img = cv2.rectangle(img , (x,y), (x+w,y+h),(0,255,0),3)

cv2.imshow("t",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
