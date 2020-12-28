import PyPDF2
import sys

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')

def main():
	if len(sys.argv) < 2:
		print('Must input at least one pdf to be merged: invalid # of args')
		exit()
	inputs = sys.argv[1:]
	pdf_combiner(inputs) 
	
if __name__ == '__main__':
	main();
	
