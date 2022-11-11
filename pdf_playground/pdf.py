# 'rb' is read binary
# with open('dummy.pdf', 'rb') as dummy:
# 	# print(dummy)
# 	reader = PyPDF2.PdfFileReader(dummy)
# 	# print(reader.numPages)
# 	# print(reader.getPage(0))
# 	page = reader.getPage(0)
# 	page.rotateCounterClockwise(90)
# 	writer = PyPDF2.PdfFileWriter()
# 	writer.addPage(page)
# 	with open('tilt.pdf', 'wb') as new_dummy:
# 		writer.write(new_dummy)

# Combine dummy.pdf and twopages.pdf

# python3 pdf.py dummy.pdf twopage.pdf tilt.pdf
import PyPDF2
import sys

pdf_file = 'super.pdf'
inputs = sys.argv[1:]
def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write(pdf_file)

pdf_combiner(inputs)

# use wtr.pdf and write it on all the pages of super.pdf

with open(pdf_file, 'rb') as input_file, open('wtr.pdf', 'rb') as watermark_file:
	input_pdf = PyPDF2.PdfFileReader(input_file)
	watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
	watermark_page = watermark_pdf.getPage(0)
	watermarked_pdf = 'watermarked.pdf'

	output = PyPDF2.PdfFileWriter()

	for i in range(input_pdf.getNumPages()):
		pdf_page = input_pdf.getPage(i)
		pdf_page.mergePage(watermark_page)
		output.addPage(pdf_page)

	with open (watermarked_pdf, 'wb') as watermarked:
		output.write(watermarked)