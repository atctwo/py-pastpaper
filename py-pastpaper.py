#py-pastpaper
#searches pdfs for a specified substring
#requires non-std module PyPDF2 (http://mstamy2.github.io/PyPDF2/)

#imports
from tkinter import *
import tkinter.ttk as ttk
from threading import Thread
from tkinter import filedialog
from tkinter.messagebox import *
from functions import *

#definitions
#other functions that do the actual work are in functions.py
def startSearch():
	'''initiates the pdf search process'''
	pagesprocessed.set(0.0)
	pdfs=getfilenames(pdfpath.get())
	totalpages=getpagenum(pdfpath.get(),pdfs)
	results=getpages(pdfpath.get(),pdfs,searchquery.get(),pagesprocessed,totalpages,case_sensitive.get())
	print(results)
	if not results: showwarning("Hello?","No matches were found...")
	else:
		tree.delete(*tree.get_children())
		for p in results:
			tree.insert("","end",values=(p[0],p[1]))

def actuallyStartSearch():
	'''created a new thread to handle pdf searching'''
	searchthread=Thread(target=startSearch)
	searchthread.start()
		
#set up tk stuff
window=Tk()
window.title("py-pastpaper")

pdfpath=StringVar()			#path to pdfs
pdfpath.set("c:/")
searchquery=StringVar()		#substring to search for
searchquery.set("")
case_sensitive=IntVar()		#whether or not to ignore case
case_sensitive.set(0)
pagesprocessed=DoubleVar()	#how many pages have been processed
pagesprocessed.set(0.0)

#title lable thing
Label(window,text="py-pastpaper",font=("MS Sans Serif",8,"bold")).grid(row=0,column=0,columnspan=6,sticky=W)

#pdf dir entry field and "Browse" button
Label(window,text="PDF Directory:").grid(row=1,column=0)
Entry(window,textvariable=pdfpath,width=40).grid(row=1,column=1,columnspan=5,padx=3,pady=3)
Button(window,text="Browse",command=lambda:pdfpath.set(filedialog.askdirectory()+"/")).grid(row=1,column=6)

#search query entry field
Label(window,text="Search query:").grid(row=2,column=0)
Entry(window,textvariable=searchquery,width=47).grid(row=2,column=1,columnspan=6,padx=3,pady=3)

#"Case sensitive" checkbox
Checkbutton(window,text="Case sensitive",variable=case_sensitive).grid(row=3,column=0,columnspan=2)
#"Search" button
Button(window,text="Search",command=lambda: actuallyStartSearch()).grid(row=3,column=4)

#"Completion" indicator
ttk.Progressbar(window,mode="determinate",orient=HORIZONTAL,length=400,variable=pagesprocessed).grid(row=4,column=0,columnspan=7,padx=3,pady=3)

#Results treeview 
tree=ttk.Treeview(window,columns=("File","Page"))
tree.grid(row=5,column=0,rowspan=1,columnspan=7,padx=3,pady=3)

tree.column("#0",width=0)
tree.heading("#1",text="File")
tree.column("#1",width=300)
tree.heading("#2",text="Page")
tree.column("#2",width=100)

window.mainloop()
#print(pdf.getPage(28).extractText())