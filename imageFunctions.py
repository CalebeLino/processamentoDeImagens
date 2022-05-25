import cv2
import numpy as np


def clone_img(img):
    clone = np.zeros_like(img)

    for z in range(np.shape(img)[2]):
        for x in range(np.shape(img)[1]):
            for y in range(np.shape(img)[0]):
                clone[y, x, z] = img[y, x, z]
    cv2.imshow("", clone)
    cv2.waitKey(0)
    return clone


def midmirror_img(img):
    midmirr = np.zeros_like(img)

    for z in range(np.shape(img)[2]):
        for x in range(int(np.shape(img)[1]/2)):
            for y in range(np.shape(img)[0]):
                midmirr[y, int(np.shape(img)[1]/2 - 1) + x, z] = img[y, int(np.shape(img)[1]/2 - 1) + x, z]
                midmirr[y, int(np.shape(img)[1] / 2 - 1) - x, z] = img[y, int(np.shape(img)[1] / 2 - 1) + x, z]
    cv2.imshow("", midmirr)
    cv2.waitKey(0)
    print(img)
    print("-------")
    print(midmirr)
    return midmirr


def reverse_img(img):
    reverse = np.zeros_like(img)

    for z in range(np.shape(img)[2]):
        for x in range(np.shape(img)[1]):
            for y in range(np.shape(img)[0]):
                reverse[y, x, z] = img[y, np.shape(img)[1]-1-x, z]
    cv2.imshow("",  reverse)
    cv2.waitKey(0)
    print(img)
    print("-------")
    print(reverse)
    return reverse


def rotate90(img):
    rotated = np.zeros((np.shape(img)[1], np.shape(img)[0], np.shape(img)[2]))

    for z in range(np.shape(img)[2]):
        for x in range(np.shape(img)[1]):
            for y in range(np.shape(img)[0]):
                rotated[np.shape(img)[0]-1-x, y, z] = img[y, x, z]
    cv2.imshow("", rotated)
    print(img[:, :, 0])
    print("-------")
    print(rotated[:, :, 0])
    cv2.waitKey(0)


test_img = cv2.imread("testImg.png")
cv2.imwrite("clone.png", clone_img(test_img))
rotate90(test_img)
cv2.imwrite("reversed.png", reverse_img(test_img))
cv2.imwrite("centerMirrored.png", midmirror_img(test_img))



