from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

bp = "C:\\Users\\21jan\\OneDrive - The Ohio State University\\Desktop\\OSU\FEH\\App 11-01\\"

# input_pdf = PdfFileReader(bp + "APP-C10COMPLETE.pdf")
# output = PdfFileWriter()
#
# # for i in range(5):
# #     output.addPage(input_pdf.getPage(i))
#
# with open(bp + "APP-C10COMPLETE.pdf", "wb") as output_stream:
#     output.write(output_stream)

pdf_file1 = PdfFileReader(bp+"APP_C11-01firstpart.pdf")
pdf_file2 = PdfFileReader(bp + "APP_11_01secondpart.pdf")
output = PdfFileMerger()
output.append(pdf_file1)
output.append(pdf_file2)

with open(bp + "merged.pdf", "wb") as output_stream:
    output.write(output_stream)