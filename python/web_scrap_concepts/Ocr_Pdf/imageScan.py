import pytesseract
from PIL import Image
import pandas as pd
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\DELL\Pictures\1.png"
only_image_pdg = r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\pdf_with_only_images.pdf"
mix_pdf = r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\pdf_mix__imgText.pdf" # text and image

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

        df.to_excel(r"D:\Repositories\2025\python\web_scrap_concepts\Ocr_Pdf\ocr_output.xlsx",index=False, header=False)
        print("done")

    def pdf_read(self):
        images = convert_from_path(mix_pdf) #pdf with text also working because the whole page gets converted to an image. 
        for img in images:
            text = pytesseract.image_to_string(img)
            print(text) 


read_obj = Read()
read_obj.pdf_read()