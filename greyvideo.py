import cv2
cam = cv2.VideoCapture(0)
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while(True):
    checker,frame = cam.read()
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_de = face.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in face_de:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("g",frame)
    key = cv2.waitKey(30)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()