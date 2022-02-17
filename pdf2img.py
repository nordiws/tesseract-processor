import glob
import re
import fitz
from numpy import matrix


def pdf2img():
    pdfPath = '.\pdf\\'
    imgPath = '.\img\\'

    zoom = 3
    mat = fitz.Matrix(zoom, zoom)

    all_files = glob.glob(pdfPath + "*.pdf")

    for file in all_files:
        filename = re.search('(?<=pdf\\\)\w+', file).group(0)
        doc = fitz.open(file)
        for page in doc:
            img = page.get_pixmap(matrix=mat)
            img.save(imgPath+filename+"-"+str(page.number)+".png")
