import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text.strip()

def extract_text_from_scanned_pdf(pdf_path):
    """Extract text from scanned PDFs using Tesseract OCR."""
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img) + "\n"
    return text.strip()

def extract_text(pdf_path):
    """Decides whether to use PyMuPDF or Tesseract based on content."""
    text = extract_text_from_pdf(pdf_path)
    if len(text.strip()) > 50:  # If there's enough text, return it
        return text
    else:
        return extract_text_from_scanned_pdf(pdf_path)

if __name__ == "__main__":
    pdf_file = "sample.pdf"  # Replace with your test PDF
    if os.path.exists(pdf_file):
        extracted_text = extract_text(pdf_file)
        print("Extracted Text:\n", extracted_text)
    else:
        print(f"File {pdf_file} not found!")

        
# Save the extracted text for processing
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(extracted_text)

