from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import  letter
from reportlab.lib.pagesizes import landscape

import csv

data_file = 'csvtest.csv'

def import_data(data_file):
    attendee_data = csv.reader(open(data_file))
    for row in attendee_data:
        bibnumber = row[0]
        tshirtSize = row[1]
        pdf_file_name = bibnumber + tshirtSize + '.pdf'
        generate_pdf(bibnumber, tshirtSize, pdf_file_name)

def generate_pdf(bibnumber,tshirtSize,pdf_file_name):
    attendee_number = bibnumber
    attendee_tshirt = tshirtSize
    c = canvas.Canvas(pdf_file_name,pagesize=landscape(letter))
    c.drawString(415,500,attendee_number)
    c.drawString(430,520,attendee_tshirt)
    c.showPage()
    print('writing')
    c.save()

import_data(data_file)