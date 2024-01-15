from filestack import Client
from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amounts
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmates, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("flatmates_bill/files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Set font for flatmate details
        pdf.set_font(family="Times", size=12)

        # Iterate over all flatmates and their payment details
        for flatmate in flatmates:
            other_flatmates = [fm for fm in flatmates if fm != flatmate]
            total_days = sum(fm.days_in_house for fm in other_flatmates)
            fm_share = flatmate.days_in_house / (total_days + flatmate.days_in_house)
            amount_due = fm_share * bill.amount

            pdf.cell(w=100, h=25, txt=flatmate.name, border=0)
            pdf.cell(w=150, h=25, txt=f"{amount_due:.2f}", border=0, ln=1)

        # Save the PDF in the 'static' directory
        pdf.output("static/" + self.filename)


class FileSharer:

    def __init__(self, filepath, api_key="INSERT YOUR API KEY"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
