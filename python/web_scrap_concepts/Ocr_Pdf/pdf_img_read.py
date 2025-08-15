import pdfplumber
import pytesseract
from PIL import Image
import pandas as pd
from pdf2image import convert_from_path
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = r"C:\Users\DELL\Pictures\1.png"
only_image_pdg = r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\pdf_with_only_images.pdf"
mix_pdf = r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\pdf_mix__imgText.pdf"
california_rahul = r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\CA_rahul_sharma.pdf"
ocr_excel_path = r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\ocr_output.xlsx"

def preprocess_image(img):
    img = img.convert('L') 
    img = img.point(lambda x: 0 if x < 140 else 255, '1') 
    return img

class Read:
    def __init__(self):
        pass

    def image_scan(self):
        img = Image.open(image_path)
        img = preprocess_image(img)
        get_text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
        print(get_text)

        lines = get_text.strip().split('\n')
        rows = []
        for line in lines:
            if line.strip():
                data = line.split()
                rows.append(data)

        df = pd.DataFrame(rows)
        df.to_excel(ocr_excel_path, index=False, header=False)
        print(f"Image OCR saved to Excel at: {ocr_excel_path}")

    def pdf_read(self):
        images = convert_from_path(california_rahul, dpi=300) 

        text_data = []

        for i, img in enumerate(images):
            processed_img = preprocess_image(img)
            text = pytesseract.image_to_string(processed_img, lang='eng', config='--psm 6')
            print(f"Page {i+1} - Text length: {len(text)}")
            text_data.append({'Page': i + 1, 'Text': text})

        df = pd.DataFrame(text_data)
        df.to_excel(ocr_excel_path, index=False)
        print(f"OCR data from scanned PDF saved to Excel at: {ocr_excel_path}")

    def pdf_read_hybrid(self, pdf_path):
        final_text = []

        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text and text.strip():
                    print(f"[Plumber] Page {i+1} - Extracted")
                    final_text.append({'Page': i + 1, 'Text': text})
                else:
                    print(f"[OCR] Page {i+1} - OCR fallback")
                    image = convert_from_path(pdf_path, first_page=i+1, last_page=i+1, dpi=300)[0]
                    processed_img = preprocess_image(image)
                    ocr_text = pytesseract.image_to_string(processed_img, lang='eng', config='--psm 6')
                    final_text.append({'Page': i + 1, 'Text': ocr_text})

        df = pd.DataFrame(final_text)
        df.to_excel(ocr_excel_path, index=False)
        print(f"Hybrid PDF text extraction saved to Excel at: {ocr_excel_path}")


read_obj = Read()
read_obj.pdf_read() 

# read_obj.image_scan()  # single image 
# read_obj.pdf_read_hybrid(california_rahul)  # mixed PDF(text + images)
