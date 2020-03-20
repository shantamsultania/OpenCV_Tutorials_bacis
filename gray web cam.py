import cv2

cam = cv2.VideoCapture(0)

while True:
    check,frame = cam.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('gray video',gray)

    key = cv2.waitKey(0)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()