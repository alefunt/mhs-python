import os

from my_tex.document import create_document
from my_tex.tabular import create_table
from my_tex.image import create_image
from my_tex.image import preamble as img_preamble
from pdflatex import PDFLaTeX


def main():
    with open("artifacts/table.tex", "w") as f:
        f.write(create_document(create_table([["a1", "a2"], ["b1", "b2"]])))
    with open("artifacts/full.tex", "w") as f:
        body = img_preamble("./images") + "\n"
        body += create_table([["a1", "a2"], ["b1", "b2"]]) + "\n"
        body += create_image("InterestingImagesEx1.png")
        f.write(create_document(body))
    pdfl = PDFLaTeX.from_texfile("artifacts/full.tex")
    pdf,_,_ = pdfl.create_pdf()
    # print(pdf)

if __name__ == "__main__":
    main()
