import streamlit as st
import PyPDF2
from io import BytesIO

st.title('📚 PDF Merger Tool')

st.markdown("""
Merge your PDF documents into one file easily. Just upload your PDF files in the order you want them merged.
""")

uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type='pdf', help="You can select multiple files by holding down the 'Shift' or 'Ctrl' (Command on Mac) key while selecting.")

def merge_pdfs(paths):
    pdf_writer = PyPDF2.PdfWriter()
    for uploaded_file in paths:
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in range(len(reader.pages)):
            pdf_writer.add_page(reader.pages[page])
    return pdf_writer

if uploaded_files:
    with st.spinner('Merging your PDFs...'):
        merged_pdf = merge_pdfs(uploaded_files)
        with BytesIO() as output_bytes:
            merged_pdf.write(output_bytes)
            st.success('Your PDFs have been successfully merged!')
            st.download_button(label="📥 Download Merged PDF",
                               data=output_bytes.getvalue(),
                               file_name="merged_file.pdf",
                               mime="application/pdf")
