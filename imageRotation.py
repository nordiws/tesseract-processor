import pytesseract
from pytesseract import Output
import cv2
import os
from utils.rotateImage import rotateImage


def imgRotation():
    imgDir = 'img'  # Defining folder name

    # Iterating through each image in folder and extracting OSD information
    for img in os.scandir(imgDir):
        osd = pytesseract.image_to_osd(".\img\\" + img.name, output_type=Output.DICT)

        # If the orientation is different from horizontal rotate the image
        if osd['orientation'] != 0:
            original_image = cv2.imread(".\img\\" + img.name)
            rotated_image = rotateImage(original_image, osd['orientation'])
            cv2.imwrite(".\img\\"+"r-"+img.name, rotated_image)
