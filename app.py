import cv2 as cv
from cv2 import threshold
import pytesseract
from pytesseract import Output
import numpy
import os
from pathlib import Path
from utils.pdf2img import pdf2img
import utils.image_preprocess as image_preprocess
from utils.image_rotation import image_rotation
import utils.image_preprocess as image_preprocess

# Images folder
image_dir = 'img'

# Converting PDF to image
pdf2img()

# Verify and rotate wrong orientations
image_rotation()

# Images array
images = []

for file in os.scandir(image_dir):
    image = cv.imread(".\\"+image_dir+"\\"+file.name)  # Read next image

    # Applying diferente preprocessing techniques to the current image
    grayscale_image = image_preprocess.get_grayscale(
        image)  # Apply grayscale preprocess

    # Processing the image in Tesseract
    raw_output = pytesseract.image_to_data(
        grayscale_image, output_type=Output.DICT)

    # Extract text from Tesseract output
    text_output = numpy.asanyarray(raw_output['text'])
    filename = Path(file.name).stem  # Extract file name from image file

    # Save extracted text from image to txt file
    numpy.savetxt('.\\txt\\{}.txt'.format(filename),
                  text_output, fmt='%s', newline=" ",)
