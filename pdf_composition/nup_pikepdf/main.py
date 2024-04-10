from func import *

if __name__ == '__main__':

    # define the number of slides per page (possible values are 2, 3, 4, 6, 9, 12)
    slides_per_page = 3
    # define the path of the input pdf  (modify this path to your own path)
    pdf_path = "sample.pdf"
    # define the path of the output pdf (modify this path if you want to save the output in a different format)
    output_path = f"{pdf_path.strip('.pdf')}_{slides_per_page}_combined.pdf"

    # run the nup function
    nup_pdf(pdf_path, output_path, slides_per_page)


