import cv2
import numpy as np

test_img = cv2.imread("testImg.png")
cv2.imshow("R", test_img[:, :, 2])
print("Displaying red channel")
cv2.waitKey(0)


