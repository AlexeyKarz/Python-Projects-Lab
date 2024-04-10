from pikepdf import Pdf, Rectangle
from math import ceil


def nup_pdf(input_pdf, output_pdf="combined.pdf", slides_per_page=9):

    # return error if the number of slides per page is not supported
    if slides_per_page not in [2, 4, 6, 9, 12]:
        raise ValueError("The number of slides per page is not supported. Supported values are 2, 4, 6, 9, 12")

    # Open the input PDF
    pdf = Pdf.open(input_pdf)

    # Calculate the number of pages in the output PDF
    num_of_pages = len(pdf.pages)

    # Calculate the number of pages in the output PDF
    num_of_new_pages = ceil(num_of_pages / slides_per_page)

    # get the first page of the PDF
    page1 = pdf.pages[0]
    # calculate the width for the blank pages and convert to float
    original_width = float(page1.trimbox[2])
    original_height = float(page1.trimbox[3])
    if slides_per_page == 2:
        width = float(original_width)
        height = float(original_height) * 2
    elif slides_per_page == 4:
        width = float(original_width) * 2
        height = float(original_height) * 2
    elif slides_per_page == 6:
        width = float(original_width) * 2
        height = float(original_height) * 3
    elif slides_per_page == 9:
        width = float(original_width) * 3
        height = float(original_height) * 3
    elif slides_per_page == 12:
        width = float(original_width) * 3
        height = float(original_height) * 4
    else :
        # return error if the number of slides per page is not supported (p.s. supposed to be unreachable)
        raise ValueError("The number of slides per page is not supported. Supported values are 2, 4, 6, 9, 12")

    # add blank pages to the original PDF (the pages for combined PDF)
    for i in range(num_of_new_pages):
        pdf.add_blank_page(page_size=(width, height))

    # create the position grid based on the number of slides per page
    # positions = [[0, height * (2 / 3), width / 3, height],
    #              [width / 3, height * (2 / 3), width * (2 / 3), height],
    #              [width * (2 / 3), height * (2 / 3), width, height],
    #              [0, height / 3, width / 3, height * (2 / 3)],
    #              [width / 3, height / 3, width * (2 / 3), height * (2 / 3)],
    #              [width * (2 / 3), height / 3, width, height * (2 / 3)],
    #              [0, 0, width / 3, height / 3],
    #              [width / 3, 0, width * (2 / 3), height / 3],
    #              [width * (2 / 3), 0, width, height / 3]]

    positions = {
        2: [(0, height / 2, width, height), (0, 0, width, height / 2)],
        3: [(0, height * 2 / 3, width, height), (0, height / 3, width, height * 2 / 3), (0, 0, width, height / 3)],
        4: [(0, height / 2, width / 2, height), (width / 2, height / 2, width, height), (0, 0, width / 2, height / 2),
            (width / 2, 0, width, height / 2)],
        6: [(0, height * 2 / 3, width / 2, height), (width / 2, height * 2 / 3, width, height),
            (0, height / 3, width / 2, height * 2 / 3), (width / 2, height / 3, width, height * 2 / 3),
            (0, 0, width / 2, height / 3), (width / 2, 0, width, height / 3)],
        9: [(0, 2 * height / 3, width / 3, height), (width / 3, 2 * height / 3, 2 * width / 3, height),
            (2 * width / 3, 2 * height / 3, width, height),
            (0, height / 3, width / 3, 2 * height / 3), (width / 3, height / 3, 2 * width / 3, 2 * height / 3),
            (2 * width / 3, height / 3, width, 2 * height / 3),
            (0, 0, width / 3, height / 3), (width / 3, 0, 2 * width / 3, height / 3),
            (2 * width / 3, 0, width, height / 3)],
        12: [(0, height * 3 / 4, width / 3, height), (width / 3, height * 3 / 4, 2 * width / 3, height),
             (2 * width / 3, height * 3 / 4, width, height),
             (0, height / 2, width / 3, height * 3 / 4), (width / 3, height / 2, 2 * width / 3, height * 3 / 4),
             (2 * width / 3, height / 2, width, height * 3 / 4),
             (0, height / 4, width / 3, height / 2), (width / 3, height / 4, 2 * width / 3, height / 2),
             (2 * width / 3, height / 4, width, height / 2),
             (0, 0, width / 3, height / 4), (width / 3, 0, 2 * width / 3, height / 4),
             (2 * width / 3, 0, width, height / 4)]
    }

    # get the first blank page
    idx_first_blank_page = num_of_pages

    # fill the blank pages with the original PDF pages
    blank_page_num = 0
    for page_num in range(idx_first_blank_page, idx_first_blank_page + num_of_new_pages):
        for i in range(0, slides_per_page):
            p = positions[slides_per_page][i]
            if (i + blank_page_num * slides_per_page) < num_of_pages:
                pdf.pages[page_num].add_overlay(pdf.pages[i + blank_page_num * slides_per_page],
                                                Rectangle(*p))
                if i == slides_per_page - 1:
                    blank_page_num += 1

    # delete the old PDF pages
    del pdf.pages[0:num_of_pages]

    # save the output PDF
    pdf.save(output_pdf)
