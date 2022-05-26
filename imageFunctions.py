import cv2
import numpy as np


def clone_img(img):
    clone = np.zeros_like(img)  # Creating a Matrix filled with zeros which has the same shape as the Image (img)

    for z in range(np.shape(img)[2]):   # Each 'z' represents a depth
        for y in range(np.shape(img)[0]):   # Each 'y' represents a line (group of values in a depth)
            for x in range(np.shape(img)[1]):   # Each 'x' represents a column (values in a line)
                clone[y, x, z] = img[y, x, z]   # Copying each pixel to the 'clone' matrix. Pixels are accessed as [line, column, depth]
    cv2.imshow("", clone)
    cv2.waitKey(0)
    return clone


def midmirror_img(img):
    midmirr = clone_img(img)

    for z in range(np.shape(img)[2]):
        for y in range(np.shape(img)[0]):
            for x in range(int(np.shape(img)[1] / 2)):  # Iterating just half the image
                midmirr[y, np.shape(img)[1] - 1 - x, z] = img[y, x, z]  # Mirroring each pixel, so the first pixel in original image is the last in the copy and so on
    cv2.imshow("", midmirr)
    cv2.waitKey(0)
    print(img)
    print("-------")
    print(midmirr)
    return midmirr


def reverse_img(img):
    reverse = np.zeros_like(img)

    for z in range(np.shape(img)[2]):
        for y in range(np.shape(img)[0]):
            for x in range(np.shape(img)[1]):
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
        for y in range(np.shape(img)[0]):
            for x in range(np.shape(img)[1]):
                rotated[x, np.shape(img)[0]-1-y, z] = img[y, x, z]
    cv2.imshow("", rotated)
    print(img)
    print("-------")
    print(rotated)
    cv2.waitKey(0)


test_img = cv2.imread("testImg.png")
cv2.imwrite("clone.png", clone_img(test_img))
rotate90(test_img)
cv2.imwrite("reversed.png", reverse_img(test_img))
cv2.imwrite("centerMirrored.png", midmirror_img(test_img))



