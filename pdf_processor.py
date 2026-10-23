# src/pdf_processor.py
import os
from PyPDF2 import PdfReader, PdfWriter
from utils import setup_logging

logger = setup_logging(__name__)

class PDFProcessor:
    def __init__(self):
        logger.info("PDFProcessor initialized.")

    def extract_text_from_pdf(self, pdf_path):
        if not os.path.exists(pdf_path):
            logger.error(f"File not found: {pdf_path}")
            return None
        text_content = ""
        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                text_content += page.extract_text() + "\n"
            return text_content
        except Exception as e:
            logger.error(f"Error extracting text: {e}")
            return None

    def merge_pdfs(self, pdf_paths, output_path):
        writer = PdfWriter()
        for path in pdf_paths:
            if os.path.exists(path):
                reader = PdfReader(path)
                for page in reader.pages:
                    writer.add_page(page)
        with open(output_path, 'wb') as f:
            writer.write(f)
        logger.info(f"PDFs merged successfully into '{output_path}'.")
        return True

    def apply_watermark(self, input_pdf, watermark_pdf, output_pdf):
        watermark_reader = PdfReader(watermark_pdf)
        watermark_page = watermark_reader.pages[0]
        input_reader = PdfReader(input_pdf)
        writer = PdfWriter()

        for page in input_reader.pages:
            page.merge_page(watermark_page)
            writer.add_page(page)

        with open(output_pdf, 'wb') as f:
            writer.write(f)
        logger.info(f"Watermark applied -> '{output_pdf}'.")
        return True
