#read pdf file using pdfplumber package

import pdfplumber   # https://pypi.org/project/pdfplumber/#files or pip install pdfplumber to get the module
with pdfplumber.open("samplereport.pdf") as f1:
    #getting the metadata
    file_metadata=f1.metadata
    print(file_metadata)

    # How to get the total number of the pages
    pages=f1.pages
    print(len(f1.pages))
    # print(type(pages))  #pages is a list type
    #parce through each pages and get text from the pages
    for page in pages:
        print(page.extract_text())

    # save the out to a file         
