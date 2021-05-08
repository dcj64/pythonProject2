# This is a sample Python script.

import PyPDF2
pdffileobj=open('test2.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(x-1)
text=pageobj.extractText()

file1=open(r"C:/Users/David/Downloads\\1.txt","a")
file1.writelines(text)
file1.close()
