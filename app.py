import cv2 as cv
import image_preprocess as imgPre
import pytesseract
from pytesseract import Output
import numpy
from pdf2img import pdf2img
import os
from pathlib import Path
from imageRotation import imgRotation

imgDir = 'img'

# Converting PDF to image
pdf2img()

imgRotation()

images = []

for file in os.scandir(imgDir):
    img = cv.imread(".\\"+imgDir+"\\"+file.name)
    grayImg = imgPre.get_grayscale(img)
    rawText = pytesseract.image_to_data(grayImg, output_type=Output.DICT)
    txtOutput = numpy.asanyarray(rawText['text'])
    filename = Path(file.name).stem
    numpy.savetxt('.\\txt\\{}.txt'.format(filename), txtOutput, fmt='%s', newline=" ",)
