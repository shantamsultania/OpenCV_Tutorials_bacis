import cv2
import os
import time

camera = cv2.VideoCapture(0)

try:
    if not os.path.exists('framecollection'):
        os.makedirs('framecollection')
except OSError:
    print('directorry not created')


current_frame_count = 0
total_time =10
start_time =time.time()


while(int(time.time()-start_time)<total_time):

    ret,frame = camera.read()
    cv2.imshow("frame",frame)
    if ret:
        name = './framecollection/count' + str(current_frame_count) + '.jpg'
        print(name)
        cv2.imwrite(name, frame)
        current_frame_count += 1
    else:
        break
    key = cv2.waitKey(1)
    if key == 27:
        break
camera.release()
cv2.destroyAllWindows()