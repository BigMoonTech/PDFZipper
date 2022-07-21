import pdfplumber
import fitz

# <------------------------------------ the following lines use pdfplumber ------------------------------------>
# with pdfplumber.open("/Users/joshraguilar/Desktop/huntington_evens.pdf") as evens:
#     even_pages = evens.pages
#
# with pdfplumber.open("/Users/joshraguilar/Desktop/huntington_odds.pdf") as odds:
#     odd_pages = odds.pages
#
# all_pages = zip(odd_pages, even_pages)

# <--------------------------------------- the following lines use fitz/PyMuPDF --------------------------------------->
fronts_odds = '/Users/joshraguilar/PycharmProjects/PDFZipper/seyma_odds.pdf'
backs_evens = '/Users/joshraguilar/PycharmProjects/PDFZipper/seyma_evens.pdf'

evens = fitz.Document(backs_evens)
print(evens.page_count)
odds = fitz.Document(fronts_odds)
print(odds.page_count)

total_pages = len(evens) + len(odds)

complete_pdf = fitz.Document()
for i in range(total_pages//2):
    complete_pdf.insert_pdf(odds, from_page=i, to_page=i)
    complete_pdf.insert_pdf(evens, from_page=i, to_page=i)

print(complete_pdf.page_count)

complete_pdf.delete_pages((1, 3, 5, 7, 21, 29, 33, 34, 35, 39))
complete_pdf.save('/Users/joshraguilar/Desktop/seyma_hunt_2019.pdf')