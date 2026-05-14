import pdfplumber

with pdfplumber.open('Aditya_Kumar_Sah_resume.pdf') as pdf:
    for page_num, page in enumerate(pdf.pages):
        print(f'=== PAGE {page_num + 1} ===')
        text = page.extract_text()
        print(text)
        print('\n')
