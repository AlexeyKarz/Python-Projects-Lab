import fitz  # PyMuPDF
import os
from pathlib import Path
import PyPDF2

def combine_pdf_pages(input_pdf_path, output_pdf_path):
    """
    Combine the pages of a PDF file into a new PDF file.
    """
    # Open the source PDF file
    source_pdf = fitz.open(input_pdf_path)
    # Create a new PDF for the output
    output_pdf = fitz.open()
    pageNumber = 1

    for page_num in range(0, len(source_pdf), 6):
        """
        Create a new A4 page. You might need to adjust the size.
        Standard A4 size: 842x1190. The width increased by 25 pixels
        in purpose to avoid cut edges (for printing):
        10px - Image1 - 5px - Image - 10px
        """
        rect = fitz.Rect(0, 0, 842 + 25, 595 * 2)
        print(f"Page №{pageNumber} is generated")
        new_page = output_pdf.new_page(width=rect.width, height=rect.height)

        # Load up to six pages
        pages = [source_pdf.load_page(i) for i in range(page_num, min(page_num + 6, len(source_pdf)))]

        # Define positions for each of the four pages on the new page
        positions = [(10, 0), (435, 0),
                     (10, 396), (435, 396),
                     (10, 792), (435, 792)]

        # Get the pixmaps (raster images) of the pages
        for i, page in enumerate(pages):
            try:
                # mat = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap()
                x, y = positions[i]
                # Insert each page image into the calculated position
                new_page.insert_image(fitz.Rect(x, y, x + 421, y + 396), pixmap=pix)
            except Exception as e:
                print(f"Error processing page {page_num + i}: {e}")
        pageNumber += 1

    # Save the output PDF
    print("The output file is saved to the path: ", output_pdf_path)
    output_pdf.save(output_pdf_path)


def combine_pdf_files(input_directory, output_file, endswith='.pdf'):
    """
    Combine all PDF files in the given directory into a single PDF file.
    """
    # Create a PdfWriter object for the output file
    writer = PyPDF2.PdfWriter()

    # List all files in the given directory
    for filename in sorted(os.listdir(input_directory)):
        if filename.endswith(endswith):
            # Construct the full file path
            file_path = os.path.join(input_directory, filename)

            # Open the PDF file
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)

                # Add all pages from the current PDF to the writer
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    writer.add_page(page)

    # Write the combined content to the output PDF file
    with open(output_file, 'wb') as out_file:
        writer.write(out_file)


def process_pdf_directory(source_directory, output_directory="LectureNoteCombined"):
    """
    Process all PDF files in the given directory by combining
    their pages into combined PDF files into new directory
    """
    # Create the output directory if it doesn't exist
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    # Go through all files in the source directory
    for file_name in os.listdir(source_directory):
        if file_name.endswith(".pdf"):
            # Construct full file paths
            input_pdf_path = os.path.join(source_directory, file_name)
            output_pdf_path = os.path.join(output_directory, f"combined_{file_name}")

            # Process each PDF file
            print(f"Processing {file_name}...")
            combine_pdf_pages(input_pdf_path, output_pdf_path)
            print(f"Saved combined file to {output_pdf_path}")


# Example usage
dir_name = "PATH_TO_YOUR_PDF_FILES"
output_dir = dir_name + "OUTPUT_DIRECTORY_NAME"
# process_pdf_directory(dir_name, output_dir) # Call the combining pdf files function UNCOMMENT TO RUN

# Example of usage
dir_path = "PATH_TO_YOUR_PDF_FILES"
original_pdf_name = "PATH_TO_PDF.pdf"  # Update this to the path of your PDF
output_pdf_name = "OUTPUT_NAME.pdf"  # Update this to your desired output path
input_pdf_path = dir_path + original_pdf_name
output_pdf_path = dir_path + output_pdf_name
# combine_pdf_pages(input_pdf_path, output_pdf_path)  # Call the combining pages function UNCOMMENT TO RUN


# Example usage
input_directory = "PATH_TO_YOUR_PDF_FILES"
output_file = 'OUTPUT_FILE_NAME.pdf'
# combine_pdf_files(input_directory, output_file)  # Call the combining pdf files function in one
