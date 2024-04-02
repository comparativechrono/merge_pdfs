import streamlit as st
import PyPDF2
from io import BytesIO

def merge_pdfs(paths):
    pdf_writer = PyPDF2.PdfWriter()
    for uploaded_file in paths:
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in range(len(reader.pages)):
            pdf_writer.add_page(reader.pages[page])
    return pdf_writer

st.title('PDF Merger')

uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type='pdf')
if uploaded_files:
    merged_pdf = merge_pdfs(uploaded_files)
    with BytesIO() as output_bytes:
        merged_pdf.write(output_bytes)
        st.download_button(label="Download Merged PDF",
                           data=output_bytes.getvalue(),
                           file_name="merged_file.pdf",
                           mime="application/pdf")
