from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("C://Users//danie//Documents//Declaracao_2020//SAQUES//Agosto_2020//comprovante.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("C://Users//danie//Documents//Declaracao_2020//SAQUES//Agosto_2020//document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)