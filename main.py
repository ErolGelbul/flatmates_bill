from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat


# initialise the Flask class
app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)
        # data property of the widget returns the info

        the_bill = flat.Bill(float(billform.amount.data), billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))

        return render_template('results.html',
                               name1=flatmate1.name,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name,
                               amount2=flatmate2.pays(the_bill, flatmate1))


class BillForm(Form):
    # Adding widgets
    amount = StringField("Bill Amount: ", default="350")
    period = StringField("Bill Period: ", default="December 2020")

    name1 = StringField("Name: ", default="John")
    days_in_house1 = StringField("Days in the house: ", default=20)

    name2 = StringField("Name: ", default="Marry")
    days_in_house2 = StringField("Days in the house: ", default=12)

    button = SubmitField("Calculate")


# Assigning URLs
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
