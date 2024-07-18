from io import BytesIO
from PyPDF2 import PdfReader

def get_text_from_pdf(pdf: BytesIO) -> str:
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
