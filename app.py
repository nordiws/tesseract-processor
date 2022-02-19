import cv2 as cv
import utils.image_preprocess as imgPre
import pytesseract
from pytesseract import Output
import numpy
from utils.pdf2img import pdf2img
import os
from pathlib import Path
from utils.image_rotation import image_rotation

imgDir = 'img'

# Converting PDF to image
pdf2img()

# Verify and rotate wrong orientations
image_rotation()

# Images array
images = []

for file in os.scandir(imgDir):
    img = cv.imread(".\\"+imgDir+"\\"+file.name)  # Read next image
    grayscale_image = imgPre.get_grayscale(img)  # Apply grayscale preprocess
    raw_output = pytesseract.image_to_data(grayscale_image, output_type=Output.DICT)  # Process image in Tesseract
    text_output = numpy.asanyarray(raw_output['text'])  # Extract text from Tesseract output
    filename = Path(file.name).stem  # Extract file name from image
    # Save extracted text from image to txt file
    numpy.savetxt('.\\txt\\{}.txt'.format(filename), text_output, fmt='%s', newline=" ",)
