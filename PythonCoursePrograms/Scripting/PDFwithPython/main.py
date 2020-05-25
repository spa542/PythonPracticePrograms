import PyPDF2

with open('dummy.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file) # reader object
	print(reader.numPages)
	print(reader.getPage(0))
	page = reader.getPage(0) # page objects
	page.rotateCounterClockwise(90)
	# print(page.rotate(180)) # can only be used from a page object not a reader object
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)
