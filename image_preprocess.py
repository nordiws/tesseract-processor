import cv2 as cv
import numpy as np


def get_grayscale(image):  # get grayscale image
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


def remove_noise(image):  # noise removal
    return cv.medianBlur(image, 5)


def thresholding(image):  # thresholding
    return cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]


def dilate(image):  # dilation
    kernel = np.ones((5, 5), np.uint8)
    return cv.dilate(image, kernel, iterations=1)


def erode(image):  # erosion
    kernel = np.ones((5, 5), np.uint8)
    return cv.erode(image, kernel, iterations=1)


def opening(image):  # opening - erosion followed by dilation
    kernel = np.ones((5, 5), np.uint8)
    return cv.morphologyEx(image, cv.MORPH_OPEN, kernel)


def canny(image):  # canny edge detection
    return cv.Canny(image, 100, 200)


def deskew(image):  # skew correction
    coords = np.column_stack(np.where(image > 0))
    angle = cv.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90+angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv.warpAffine(
        image, M, (w, h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
    return rotated


def match_template(image, template):  # template matching
    return cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
