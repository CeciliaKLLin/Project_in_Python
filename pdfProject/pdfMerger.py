import PyPDF2
import sys

pdfs = (sys.argv[1:])  # we can include as much pdfs as we can


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('result.pdf')


pdf_combiner(pdfs)
