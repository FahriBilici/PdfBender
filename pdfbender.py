from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import csv

pdfmetrics.registerFont(TTFont('preloblack', 'preloblack.ttf'))
pdfmetrics.registerFont(TTFont('prelobold', 'prelobold.ttf'))
pdfmetrics.registerFont(TTFont('prelolight', 'prelolight.ttf'))
pdfmetrics.registerFont(TTFont('prelomedium', 'prelomedium.ttf'))
pdfmetrics.registerFont(TTFont('prelosemibold', 'prelosemibold.ttf'))

data_file = 'Erkmen 11 - 10K.csv'


path = os.getcwd()
dosyaismi="Runatolia 10K"
dosyayol=path+"/"+dosyaismi
#print ("The current working directory is %s" % path)
if not os.path.exists(dosyayol):
    os.mkdir(dosyayol)
def import_data(data_file):
    attendee_data=csv.reader(open(data_file))
    for row in attendee_data:
        bibnumber=row[0]
        tshirtSize=""
        pdfName=bibnumber + tshirtSize + '.pdf'
        generate_pdf(bibnumber,tshirtSize,pdfName)

def generate_pdf(bibnumber,tshirtSize,pdfName):
    attendee_bib = bibnumber
    attendee_tshirt=tshirtSize
    can=canvas.Canvas("a.pdf", pagesize=letter)
    can.setFont('preloblack', 175)
    can.setFillColor('white')
    can.drawCentredString(320, 150, attendee_bib)
    print(attendee_bib)
    can.setFont('prelomedium', 21)
    if attendee_tshirt == 'XL':
        can.setFont('prelomedium',15)
    can.drawString(603,21,attendee_tshirt)
    can.save()
    new_pdf =PdfFileReader("a.pdf")
    f=open("10Ktemp.pdf","rb")
    existing_pdf=PdfFileReader(f)
    output=PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    outputStream = open(dosyayol+"/"+pdfName, "wb")
    output.write(outputStream)
    outputStream.close()
    f.close()

import_data(data_file)