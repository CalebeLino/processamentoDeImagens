import cv2
import numpy as np


def mirror_img(img):
    for channel in range(np.shape(img)[2]):
        print("Channel: ", channel)
        for x in range(np.shape(img)[1]):
            print("X: ", x)
            img[:, x, channel] = img[:, np.shape(img)[1]-1-x, channel]
    return img


test_img = cv2.imread("testImg.png")
cv2.imshow("Mirrored", mirror_img(test_img))
cv2.imwrite("centerMirrored.png", mirror_img(test_img))
cv2.waitKey(0)


