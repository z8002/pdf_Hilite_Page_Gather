import pypdf


def extract_highlighted_pages(input_pdf_path, output_pdf_path):
    highlighted_pages = set()

    # Open the PDF file in binary mode
    pdf_file = open(input_pdf_path, 'rb')
    pdf_reader = pypdf.PdfReader(pdf_file)
    # Iterate through each page
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]

        # Check if the page has annotations/highlights
        if '/Annots' in page:
            annots = page['/Annots']
            for annot_ref in annots:
                annot = pdf_reader.get_object(annot_ref)
                if annot.get('/Subtype') == '/Highlight':
                    highlighted_pages.add(page_num + 1)  # Page numbers start from 1


    # Create a new PDF with only the highlighted pages
    output_pdf =  open(output_pdf_path, 'wb')
    pdf_writer = pypdf.PdfWriter()

    for page_numf in highlighted_pages:
        pdf_writer.add_page(pdf_reader.pages[page_numf-1])  # Adjust page number

    pdf_writer.write(output_pdf)


if __name__ == "__main__":
    input_pdf_path = "C:\\prgPrinciple.pdf"  # Replace with the path to your input PDF file
    output_pdf_path = "D:\\output.pdf"  # Replace with the desired output PDF file

    extract_highlighted_pages(input_pdf_path, output_pdf_path)
