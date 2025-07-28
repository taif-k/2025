import pdfplumber
import pytesseract
from PIL import Image
import pandas as pd
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\DELL\Pictures\1.png"
only_image_pdg = r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\pdf_with_only_images.pdf"
mix_pdf = r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\pdf_mix__imgText.pdf"
ocr_excel_path = r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\ocr_output.xlsx"

class Read:
    def __init__(self):
        pass

    def image_scan(self):
        img = Image.open(image_path)
        get_text = pytesseract.image_to_string(img)
        print(get_text)


        lines = get_text.strip().split('\n')
        
        rows = []
        for line in lines:
            if line.strip():
                data = line.split()
                rows.append(data)

        df = pd.DataFrame(rows)
        with pd.ExcelWriter(ocr_excel_path) as writer:
            df.to_excel(writer)
        print("saved in excel")
        # df.to_excel(r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\ocr_output.xlsx",index=False, header=False)

    def pdf_read(self):
        images = convert_from_path(mix_pdf) #pdf with text also working(not accurate) because the whole page gets converted to an image. 
        for img in images:
            text = pytesseract.image_to_string(img)
            print(text) 


read_obj = Read()
# read_obj.pdf_read()
read_obj.image_scan()



















# def read_pdf_hybrid(pdf_path):
#     final_text = []

#     with pdfplumber.open(pdf_path) as pdf:
#         for i, page in enumerate(pdf.pages):
#             text = page.extract_text()
#             if text and text.strip(): #pdfpulmber
#                 print(f" Page {i+1}")
#                 final_text.append(text)
#             else: #ocr
#                 print(f"Page {i+1} ")
#                 image = convert_from_path(pdf_path, first_page=i+1, last_page=i+1, dpi=300)[0]
#                 ocr_text = pytesseract.image_to_string(image)
#                 final_text.append(ocr_text)

#     return "\n".join(final_text)
