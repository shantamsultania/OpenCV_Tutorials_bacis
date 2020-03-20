import cv2

img = cv2.imread("r123456.jpeg")

#display an image
cv2.imshow("image ",img)

#gray image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image',gray)

#saving this image
cv2.imwrite('sha.jpg',gray)

#printing the image
print(img)
cv2.waitKey(0)
