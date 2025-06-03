# pip install fitz
# pip install PyMuPDF

import fitz


def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle):
    pdf = fitz.open(pdfPath)

    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)

        pm = page.get_pixmap(matrix=trans, alpha=False)

        pm.pil_save(imgPath + str(pg) + ".png")
    pdf.close()


pdf_image("static/images/framework.pdf", "./", 3, 3, 0)
