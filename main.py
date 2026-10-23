# main.py
import os
import sys
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from pdf_processor import PDFProcessor
from word_processor import WordProcessor
from utils import ensure_directory_exists, setup_logging

logger = setup_logging(__name__)

def main():
    docs_dir = os.path.join(os.path.dirname(__file__), 'documents')
    ensure_directory_exists(docs_dir)

    pdf_proc = PDFProcessor()
    word_proc = WordProcessor()

    logger.info("--- Starting Week 11 Automation Workflows ---")

    pdf1 = os.path.join(docs_dir, 'dummy_doc1.pdf')
    pdf2 = os.path.join(docs_dir, 'dummy_doc2.pdf')
    merged_output = os.path.join(docs_dir, 'merged_docs.pdf')
    if os.path.exists(pdf1) and os.path.exists(pdf2):
        pdf_proc.merge_pdfs([pdf1, pdf2], merged_output)

    input_pdf = os.path.join(docs_dir, 'input_article.pdf')
    report_output = os.path.join(docs_dir, 'generate_report.docx')
    extracted_text = pdf_proc.extract_text_from_pdf(input_pdf)

    if extracted_text:
        doc = word_proc.create_document()
        word_proc.add_heading(doc, "Automated Task Manager & Document Report", level=1)
        word_proc.add_paragraph(doc, "This report was generated as part of Week 11 Project Planning.", bold=True)
        word_proc.add_paragraph(doc, extracted_text)

        table_data = [
            ["Metric", "Status / Value", "Notes"],
            ["PDF Merging", "Merged successfully", "Merged into merged_docs.pdf"],
            ["Watermarking", "Applied overlay", "Created watermarked_document.pdf"],
            ["Docx Gen", "Completed", "Saved as generate_report.docx"],
            ["Generated", datetime.date.today().isoformat(), "Automated timestamp"]
        ]
        word_proc.add_table(doc, table_data, col_widths=[2.0, 2.0, 2.5])
        word_proc.save_document(doc, report_output)

    logger.info("--- Automation Pipeline Completed Successfully ---")

if __name__ == "__main__":
    main()
