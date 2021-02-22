import requests
from zipfile import ZipFile
from os import listdir
from os.path import isfile, join
import PyPDF2
import pdfPlumber

url = 'https://e-disclosure.ru/portal/FileLoad.ashx?Fileid=1681307';
r = requests.get(url, allow_redirects=True)
open('report.zip', 'wb').write(r.content)


with ZipFile ('report.zip', 'r') as zipObj:
   zipObj.extractall('New Report')

print(listdir('New Report'))

file_to_read = 'C:\\Users\\tkachenkov\\Desktop\\Python\\PDF_Report_Reader\\New Report\\4-2020.pdf' #meanwhile put manually
pdfFileObj = open (file_to_read, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
lastPage = (pdfReader.numPages)
pageObj = pdfReader.getPage()
print(pageObj.extractText())