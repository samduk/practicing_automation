import pdfplumber
import io

# with pdfplumber.open("protected.pdf", password="Totaltechnology1234") as f1:
with io.open("password.txt") as f2:
    pwd=f2.read()
    f2.close()
    #print(pwd)
with pdfplumber.open("protected.pdf", password=pwd) as f1:
    print(f1)
    #get metadata
    meta_data = f1.metadata
    print(meta_data)

    #get the count of pages

    pages = f1.pages
    print(len(f1.pages))

    # get the text from the pages

    for page in pages:
        print(page.extract_text())
