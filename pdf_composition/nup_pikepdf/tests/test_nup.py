import os
import unittest
from math import ceil
from pikepdf import Pdf
from func import nup_pdf


def assert_pdf_equal(pdf1, pdf2, number=9):
    new_pdf = Pdf.open(pdf1)
    old_pdf = Pdf.open(pdf2)
    assert len(new_pdf.pages) == ceil(len(old_pdf.pages) / number)


# write test cases to test the nup_pdf function with all possible values of slides_per_page
class TestNupPdf(unittest.TestCase):
    def test_nup_pdf_2_slides_per_page(self):
        input_pdf = "../sample.pdf"
        output_pdf = "output_2_slides_per_page.pdf"
        slides_per_page = 2
        nup_pdf(input_pdf, output_pdf, slides_per_page)
        # Add assertions to verify the correctness of the output PDF file
        assert_pdf_equal(output_pdf, input_pdf, slides_per_page)
        # delete the output file
        os.remove(output_pdf)

    def test_nup_pdf_4_slides_per_page(self):
        input_pdf = "../sample.pdf"
        output_pdf = "output_4_slides_per_page.pdf"
        slides_per_page = 4
        nup_pdf(input_pdf, output_pdf, slides_per_page)
        # Add assertions to verify the correctness of the output PDF file
        assert_pdf_equal(output_pdf, input_pdf, slides_per_page)
        # delete the output file
        os.remove(output_pdf)

    def test_nup_pdf_6_slides_per_page(self):
        input_pdf = "../sample.pdf"
        output_pdf = "output_6_slides_per_page.pdf"
        slides_per_page = 6
        nup_pdf(input_pdf, output_pdf, slides_per_page)
        # Add assertions to verify the correctness of the output PDF file
        assert_pdf_equal(output_pdf, input_pdf, slides_per_page)
        # delete the output file
        os.remove(output_pdf)

    def test_nup_pdf_9_slides_per_page(self):
        input_pdf = "../sample.pdf"
        output_pdf = "output_9_slides_per_page.pdf"
        slides_per_page = 9
        nup_pdf(input_pdf, output_pdf, slides_per_page)
        # Add assertions to verify the correctness of the output PDF file
        assert_pdf_equal(output_pdf, input_pdf, slides_per_page)
        # delete the output file
        os.remove(output_pdf)

    def test_nup_pdf_12_slides_per_page(self):
        input_pdf = "../sample.pdf"
        output_pdf = "output_12_slides_per_page.pdf"
        slides_per_page = 12
        nup_pdf(input_pdf, output_pdf, slides_per_page)
        # Add assertions to verify the correctness of the output PDF file
        assert_pdf_equal(output_pdf, input_pdf, slides_per_page)
        # delete the output file
        os.remove(output_pdf)

# if __name__ == '__main__':
#     unittest.main()
