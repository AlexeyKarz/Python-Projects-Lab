from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField
from flatmates_bill import flat, reports
from reportlab.pdfgen import canvas
from io import BytesIO
from flask import jsonify, send_from_directory

app = Flask(__name__)


@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    data = request.json
    bill_amount = float(data['amount'])
    period = data['period']

    # Create Flatmate objects from the JSON data
    flatmates = [flat.Flatmate(fm['name'], float(fm['daysInHouse'])) for fm in data['flatmates']]
    the_bill = flat.Bill(bill_amount, period)

    # Generate PDF
    pdf_report = reports.PdfReport("report.pdf")
    pdf_report.generate(flatmates, the_bill)

    # Send the generated PDF file
    return send_from_directory('static', 'report.pdf', as_attachment=True)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform=bill_form)


class ResultsPage(MethodView):

    def post(self):
        data = request.json

        bill_amount = float(data['amount'])
        period = data['period']
        flatmates = [flat.Flatmate(fm['name'], float(fm['daysInHouse'])) for fm in data['flatmates']]

        the_bill = flat.Bill(bill_amount, period)

        # Calculate payments considering other flatmates

        payments = {}
        for fm in flatmates:
            other_flatmates = [other_fm for other_fm in flatmates if other_fm != fm]
            total_days = sum(other_fm.days_in_house for other_fm in other_flatmates)
            fm_share = fm.days_in_house / (total_days + fm.days_in_house)
            payments[fm.name] = fm_share * the_bill.amount

        return jsonify(payments)


def create_pdf(payment_data):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Simple PDF Generation - you might want to format this nicely
    y_position = 800
    for name, amount in payment_data.items():
        p.drawString(72, y_position, f"{name} owes: ${amount:.2f}")
        y_position -= 40

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer.getvalue()


class BillForm(Form):
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Period: ", default="December 2020")

    name1 = StringField("Name: ", default="John")
    days_in_house1 = StringField("Days in the house: ", default="20")

    name2 = StringField("Name: ", default="Marry")
    days_in_house2 = StringField("Days in the house: ", default="12")

    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form',
                 view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results',
                 view_func=ResultsPage.as_view('results_page'))

if __name__ == "__main__":
    app.run(debug=True)
