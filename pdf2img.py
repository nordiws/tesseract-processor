import glob
import re
import fitz
from numpy import matrix


def pdf2img():

    # Folder paths
    pdfPath = '.\pdf\\'
    imgPath = '.\img\\'

    # Defining image quality
    zoom = 3
    mat = fitz.Matrix(zoom, zoom)

    # Importing all PDF on folder
    all_files = glob.glob(pdfPath + "*.pdf")

    for file in all_files:
        filename = re.search('(?<=pdf\\\)\w+', file).group(0)  # Extracting name of file
        doc = fitz.open(file)  # Opening PDF

        # Iterating through each page and saving as image
        for page in doc:
            img = page.get_pixmap(matrix=mat)
            img.save(imgPath+filename+"-"+str(page.number)+".png")
