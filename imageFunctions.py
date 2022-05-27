import cv2
import numpy as np


def clone_img(img):
    clone = np.zeros_like(img)  # Creating a Matrix filled with zeros which has the same shape as the Image (img)

    for z in range(np.shape(img)[2]):   # Each 'z' represents a depth
        for y in range(np.shape(img)[0]):   # Each 'y' represents a line (group of values in a depth)
            for x in range(np.shape(img)[1]):   # Each 'x' represents a column (values in a line)
                clone[y, x, z] = img[y, x, z]   # Copying each pixel to the 'clone' matrix. Pixels are accessed as [line, column, depth]
    return clone


def reverse_img(img):
    reverse = np.zeros_like(img)

    for z in range(np.shape(img)[2]):
        for y in range(np.shape(img)[0]):
            for x in range(np.shape(img)[1]):
                reverse[y, x, z] = img[y, np.shape(img)[1]-1-x, z]  # Reversing means revert the order, so that the last pixel is the first and so on
    cv2.imshow("",  reverse)
    cv2.waitKey(0)
    print(img)
    print("-------")
    print(reverse)
    return reverse


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


def rotate90(img):
    rotated = np.zeros((np.shape(img)[1], np.shape(img)[0], np.shape(img)[2]))  # Creating a Matrix filled with zeros which has the number of columns and lines swapped

    for z in range(np.shape(img)[2]):
        for y in range(np.shape(img)[0]):
            for x in range(np.shape(img)[1]):
                rotated[x, np.shape(img)[0]-1-y, z] = img[y, x, z]  # Rotating means to transform each line into a column.
    cv2.imshow("", rotated)
    print(img)
    print("-------")
    print(rotated)
    cv2.waitKey(0)
    return rotated


def avg_blur(img):
    # This function uses a 3x3 kernel for 'blur average' effect
    blur = clone_img(img)

    sumt = 0
    for z in range(np.shape(img)[2]):
        y = 0   # Reset y everytime next channel is called
        while y < np.shape(img)[0] - (np.shape(img)[0] % 3):    # Can only iterate in numbers that are divisible by 3
            x = 0   # Reset x everytime next line is called
            while x < np.shape(img)[1] - (np.shape(img)[1] % 3):    # ''
                sumt += img[y, x, z]    # Summation of pixels in a kernel
                if (x+1) % 3 == 0:  # When reached the end of kernel column (it means that 'x' value is divisible by 3)
                    if (y+1) % 3 == 0:  # When reached the end of kernel lines ('' 'y' '')
                        avg = int(sumt / 9)     # Since there is 3x3 = 9 elements, divide the summation by 9
                        sumt = 0    # Reset summation variable
                        # This block stores the average value in all the positions of the last kernel
                        blur[y-2, x-2, z], blur[y-2, x-1, z], blur[y-2, x, z] = avg, avg, avg
                        blur[y - 1, x - 2, z], blur[y - 1, x - 1, z], blur[y - 1, x, z] = avg, avg, avg
                        blur[y, x - 2, z], blur[y, x - 1, z], blur[y, x, z] = avg, avg, avg
                        y -= 2  # Reset 'y' into the beginning line of the kernel
                        x += 1  # Jump to the next column, initializing a new kernel
                    else:   # It means that the kernel isn't fully iterated
                        x -= 2  # Reset 'x' into the beginning column of the kernel
                        y += 1  # Jump to the next line of the same kernel
                else:
                    x += 1  # Jump to the next column of the same kernel
            else:   # If it reached the end of the col size for this image
                y += 3  # The next step is to advance to the next 'kernel line', and, since it has reseted 'y', must compensate adding '3'

    cv2.imshow("", blur)
    print(img)
    print("-------")
    print(blur)
    cv2.waitKey(0)
    return blur


def shadowing(img, value):
    shadow = clone_img(img)

    for z in range(np.shape(img)[2]):
        for y in range(np.shape(img)[0]):
            for x in range(np.shape(img)[1]):
                if img[y, x, z] >= value:
                    shadow[y, x, z] = 0

    cv2.imshow("", shadow)
    print(img)
    print("-------")
    print(shadow)
    cv2.waitKey(0)
    return shadow


def shadowing_v2(img, value):
    shadow2 = clone_img(img)

    for z in range(np.shape(img)[2]):
        for y in range(np.shape(img)[0]):
            for x in range(np.shape(img)[1]):
                if img[y, x, z] >= value:
                    shadow2[y, x, z] = img[y, x, z] - value

    cv2.imshow("", shadow2)
    print(img)
    print("-------")
    print(shadow2)
    cv2.waitKey(0)
    return shadow2


def mod_img(img, number):
    modded = clone_img(img)

    for z in range(np.shape(img)[2]):
        for y in range(np.shape(img)[0]):
            for x in range(np.shape(img)[1]):
                if img[y, x, z] % number == 0:
                    modded[y, x, z] = 0

    cv2.imshow("", modded)
    print(img)
    print("-------")
    print(modded)
    cv2.waitKey(0)
    return modded


def sqrt_img(img):
    rooted2 = clone_img(img)

    for z in range(np.shape(img)[2]):
        for y in range(np.shape(img)[0]):
            for x in range(np.shape(img)[1]):
                rooted2[y, x, z] = int(np.sqrt(img[y, x, z])) * 10

    cv2.imshow("", rooted2)
    print(img)
    print("-------")
    print(rooted2)
    cv2.waitKey(0)
    return rooted2


def sine_img(img, distortion, period):
    sined = np.zeros_like(img)

    for z in range(np.shape(img)[2]):
        for y in range(np.shape(img)[0]):
            for x in range(np.shape(img)[1]):
                if 0 <= int(np.sin(x*period) * distortion + y) <= np.shape(sined)[0]-1:
                    sined[int(np.sin(x*period) * distortion + y), x, z] = img[y, x, z]

    cv2.imshow("", sined)
    print(img)
    print("-------")
    print(sined)
    cv2.waitKey(0)
    return sined


test_img = cv2.imread("testImg.png")
cv2.imshow("Original", test_img)
cv2.waitKey(0)
cv2.imwrite("clone.png", clone_img(test_img))
cv2.imwrite("reversed.png", reverse_img(test_img))
cv2.imwrite("centerMirrored.png", midmirror_img(test_img))
cv2.imwrite("rotated90.png", rotate90(test_img))
cv2.imwrite("avg_blurred.png", avg_blur(test_img))
cv2.imwrite("shadow.png", shadowing(test_img, 100))
cv2.imwrite("shadowV2.png", shadowing_v2(test_img, 30))
cv2.imwrite("modded.png", mod_img(test_img, 3))
cv2.imwrite("sqrt.png", sqrt_img(test_img))
cv2.imwrite("sineWavy.png", sine_img(test_img, 10, 0.1))
