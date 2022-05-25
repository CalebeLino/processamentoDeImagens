import cv2
import numpy as np

test_img = cv2.imread("testImg.png")
cv2.imshow("Load", test_img)
cv2.waitKey(0)

print("Image matrix dimensions:", np.ndim(test_img))
