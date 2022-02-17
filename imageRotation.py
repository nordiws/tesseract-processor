import pytesseract
from pytesseract import Output
import cv2
import os
from utils.rotateImage import rotateImage


def imgRotation():
    imgDir = 'img'
    for img in os.scandir(imgDir):
        osd = pytesseract.image_to_osd(".\img\\" + img.name, output_type=Output.DICT)
        print(osd)
        if osd['orientation'] != 0:
            original_image = cv2.imread(".\img\\" + img.name)
            rotated_image = rotateImage(original_image, osd['orientation'])
            cv2.imwrite(".\img\\"+"r-"+img.name, rotated_image)
