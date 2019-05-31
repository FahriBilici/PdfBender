from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime
import csv

pdfmetrics.registerFont(TTFont('preloblack', 'preloblack.ttf'))
pdfmetrics.registerFont(TTFont('prelobold', 'prelobold.ttf'))
pdfmetrics.registerFont(TTFont('prelolight', 'prelolight.ttf'))
pdfmetrics.registerFont(TTFont('Helvetica', 'Helvetica.ttf'))
pdfmetrics.registerFont(TTFont('prelosemibold', 'prelosemibold.ttf'))

data_file = 'Yeşil.csv'


path = os.getcwd()
dosyaismi="Gelibolu Olimpik"
dosyayol=path+"/"+dosyaismi+"/"+"Yeşil"
#print ("The current working directory is %s" % path)
if not os.path.exists(dosyayol):
    os.mkdir(dosyayol)
def import_data(data_file):
    attendee_data=csv.reader(open(data_file))
    for row in attendee_data:
        attendeeBib=row[0]
        attendeename=row[1]
        attendeegender=row[3]
        tshirtSize=row[5]
        attendeeAge=row[4]
        pdfName=attendeeBib + '.pdf'
        generate_pdf(attendeeBib,attendeename,tshirtSize,attendeegender,attendeeAge,pdfName)

def generate_pdf(attendeeBib,attendeename,tshirtSize,attendeegender,attendeeAge,pdfName):
    name = attendeename.upper()
    attendee_tshirt=tshirtSize
    can=canvas.Canvas("a.pdf", pagesize=letter)
    can.setFont('Helvetica', 221)
    can.setFillColor('white')
    can.drawCentredString(297, 105, attendeeBib)
    can.setFont('Helvetica', 45)
    if(len(name)>12):
        can.setFont('Helvetica', 40)
    can.setFillColor('black')
    can.drawCentredString(305, 20, name)
    ''' corpcount=len(corp)
    print(bibnumber)
    can.setFont('preloblack', 55)
    if corpcount > 20:
        can.setFont('preloblack', 40)
    can.drawCentredString(318, 142,str.upper(corp))'''
    can.setFont('Helvetica',33)
   # if attendee_tshirt == 'XL':
   #    can.setFont('prelomedium',15)
    can.drawString(550,20,attendee_tshirt)
    if(attendeegender=="Male"):
        attendeegender="M"
    elif(attendeegender==""):
        attendeegender=""
    else:
        attendeegender="F"
    can.setFont('Helvetica',33)
    can.drawString(34,20,attendeegender)
    today=datetime.date.today()
    if(attendeeAge!=""):
        birthdate=datetime.datetime.strptime(attendeeAge,'%d.%m.%Y')
        age=today.year-birthdate.year
        if(age>=17 and age<=19):
            can.drawString(68,20,"18-19")
        elif(age>=20 and age<=24):
            can.drawString(68, 20, "20-24")
        elif (age >= 25 and age <= 29):
            can.drawString(68, 20, "25-29")
        elif (age >= 30 and age <= 34):
            can.drawString(68, 20, "30-34")
        elif (age >= 35 and age <= 39):
            can.drawString(68, 20, "35-39")
        elif (age >= 40 and age <= 44):
            can.drawString(68, 20, "40-44")
        elif (age >= 45 and age <= 49):
            can.drawString(68, 20, "45-49")
        elif (age >= 50 and age <= 54):
            can.drawString(68, 20, "50-54")
        elif (age >= 55 and age <= 59):
            can.drawString(68, 20, "55-59")
        elif (age >= 60 and age <= 64):
            can.drawString(68, 20, "60-64")
        elif (age >= 65 and age <= 69):
            can.drawString(68, 20, "25-29")
        elif (age >= 70 and age <= 74):
            can.drawString(68, 20, "25-29")
        elif (age >= 75 and age <= 79):
            can.drawString(68, 20, "75-79")
    can.save()

    new_pdf =PdfFileReader("a.pdf")
    f=open("gelibolutemp.pdf","rb")
    existing_pdf=PdfFileReader(f)
    output=PdfFileWriter()
    page = existing_pdf.getPage(3)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    if not os.path.exists(dosyayol+"/"):
        os.mkdir(dosyayol+"/")
    outputStream = open(dosyayol+"/"+"/"+pdfName, "wb")
    output.write(outputStream)
    outputStream.close()
    f.close()
    print(attendeeBib)

import_data(data_file)