import PyPDF2

# the program may not able to read pdf file
# use the 'rb' to read the binary of the pdf file
# this create a file stream object, to convert the file object to binary mode, the file reader can read
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as file2:
        writer.write(file2)
        # create pdf and use the rotated page as the first page
