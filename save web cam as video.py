import cv2

fourcc = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter("the_new_video_is.avi", fourcc , 25, (852, 480))
camera = cv2.VideoCapture(0)
while True:
    ret, frame = camera.read()
    cv2.imshow("frame", frame)
    key = cv2.waitKey(30)
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()