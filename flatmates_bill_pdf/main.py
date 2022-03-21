from flat import Bill, Flatmate
from report import PdfReport

the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John pays: ", john.pays(bill=the_bill, flatmate2=marry))
print("Marry pays: ", marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
