import pytesseract
from pytesseract import Output
import os
from PIL import Image


def image_rotation():
    image_dir = 'img'  # Defining folder name

    # Iterating through each image in folder and extracting OSD information
    for img in os.scandir(image_dir):
        osd = pytesseract.image_to_osd(
            ".\img\\" + img.name, output_type=Output.DICT)
        print(osd)

        # If the orientation is different from horizontal rotate the image
        if osd['orientation'] != 0:
            image = Image.open(".\img\\" + img.name)
            rotated_image = image.rotate(osd['orientation'], expand=True)
            rotated_image.save(".\img\\"+img.name)
