from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

import io
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont

packet=io.BytesIO()
data_file = 'olimpik.csv'


can=canvas.Canvas(packet,pagesize=letter)
can.setFontSize(200)
can.setFillColor('white')
can.drawCentredString(318,140,"1000")
can.setFillColor('black')
can.setFontSize(24)
can.drawString(603,15,"M")
can.save()

packet.seek(0)
new_pdf =PdfFileReader(packet)
existing_pdf=PdfFileReader(open("test.pdf","rb"))
output=PdfFileWriter()
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

outputStream = open("1000.pdf","wb")
output.write(outputStream)
outputStream.close()