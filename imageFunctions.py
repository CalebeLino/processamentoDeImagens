import cv2


def mirror_img(img):
    img = img[:, ::-1, :]
    return img


test_img = cv2.imread("testImg.png")
cv2.imwrite("mirrored.png", mirror_img(test_img))


