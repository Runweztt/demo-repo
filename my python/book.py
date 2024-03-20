from PyPDF2 import PdfReader

reader = PdfReader("frankenstein.pdf")
all_pages = reader.pages
all_texts= []
for page in all_pages:
    all_texts.append( page.extract_text())

all_text_combined = "".join(all_texts)

individualsentence = all_text_combined.split(".")
for sentences in individualsentence:
    if("monster" in sentences):
      print(sentences)
