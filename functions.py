#file: 		functions.py
#author:	atctwo
#defines functions that do the actual pdf and directory searching

from os import walk
from PyPDF2 import PdfFileReader
from sys import stdout


def getfilenames(pdfpath):
	'''gets all of the filenames of files in a directory'''
	pdfdir = []
	for (pdf, dirnames, filenames) in walk(pdfpath):
		pdfdir.extend(filenames)
		break
	return pdfdir
	
def getpagenum(pdfpath,pdfdir):
	'''get total number of pages of all pdfs in dir'''
	'''returns: (int) number of pages'''
	pages=0
	for doc in pdfdir:
		#only count if file is actually a pdf
		components=doc.split(".")
		if components[len(components)-1]!="pdf": continue
		#create PdfFileReader object
		pdf = PdfFileReader(open(pdfpath+doc, "rb"),warndest=stdout)
		pages+=pdf.getNumPages()
		del pdf	#clean up
	return pages
	
def getpages(pdfpath,pdfdir,query,sb,totalpages,case_sensitive=False):
	'''checks if query is in any pdf in pdfdir'''
	#pdfpath 		- (str)  path to pdf files
	#pdfdir 		- (list) list of pdf files to check
	#query  		- (str)  string to check for
	#case_sensitive	- (bool) whether or not to ignore case
	#returns a 2d list of filenames and pages
    
	occurances=[]
	for doc in pdfdir:
		#only count if file is actually a pdf
		components=doc.split(".")
		if components[len(components)-1]!="pdf": continue
		#create PdfFileReader object
		pdf = PdfFileReader(open(pdfpath+doc, "rb"),warndest=stdout)
		pages=pdf.getNumPages()

		for p in range(0,pages):
			#print("\rSearching...{:0.2f}".format((p/pages)*100),end="")
			sb.set(((sb.get()+1)/totalpages)*100)	#update progressbar
			text = pdf.getPage(p).extractText()
			if not case_sensitive: 
				text=text.lower()
				query=query.lower()
			if query in text: occurances.append([doc,p+1])
		del pdf	#clean up
	return occurances