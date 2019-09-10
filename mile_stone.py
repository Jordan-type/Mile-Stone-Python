# kick start  # letina = Employees(1200,120) # letina.basic_salary
# attributes  # letina.payee
# test case   # letina.nhif
#https://justpaste.it/1lfbg
# Rate and limits
# Class variables
class Employee:
    basic_salary = 0
    net_salary = 0
    benefits = 0
    payee = 0
    nhif = 0
    nssf = 0
    gross_salary = 0

# make use of constructor
    def __init__(self, basic_sal, benefit):
        self.basic_salary = basic_sal
        self.benefits = benefit
        # self.getInputs()
        self.get_Gross_salary()
        self.getPayee()
        self.getNHIF()
        self.get_NSSF()
        self.get_NetSalary()

    # def getInputs(self):
    #     # self.firstname = input("Enter your name:")
    #     # self.basic_salary = float(input("Enter gross pay:"))
    #     # self.benefits = float(input("Enter Benefits:"))
    #      return self.basic_salary, self.firstname

    def get_Gross_salary(self):
        self.gross_salary = self.basic_salary + self.benefits
        return self.gross_salary

    def getPayee(self):
        taxable_pay = self.gross_salary - self.nssf
        if taxable_pay >= 0 and taxable_pay <= 12298:
            self.payee = 0.1 * taxable_pay
            return self.payee
        elif taxable_pay >= 12299 and taxable_pay <= 23885:
            tax_amount_one =0.1* 12298
            tax_amount_two = 0.15 * (taxable_pay - 12298)
            self.payee = tax_amount_one + tax_amount_two
            return self.payee
        elif taxable_pay >= 23886 and taxable_pay <= 35472:
            tax_amount_one = 0.1 * 12298
            tax_amount_two = 0.15 * 11587
            tax_amount_three = 0.2 * (taxable_pay - 23885)
            self.payee = tax_amount_one + tax_amount_two + tax_amount_three
            return self.payee
        elif taxable_pay >= 35473 and taxable_pay <= 47059:
            tax_amount_one = 0.1 * 12298
            tax_amount_two = 0.15 * 11587
            tax_amount_three = 0.2 * 11587
            tax_amount_four = 0.25 * (taxable_pay - 35472)
            self.payee = tax_amount_one + tax_amount_two + tax_amount_three + tax_amount_four
            return self.payee
        elif taxable_pay > 47059:
            tax_amount_one = 0.1 * 12298
            tax_amount_two = 0.15 * 11587
            tax_amount_three = 0.2 * 11587
            tax_amount_four = 0.25 * 11587
            tax_amount_five = (0.3 * (taxable_pay - 47059)) - 1408
            self.payee = tax_amount_one + tax_amount_two + tax_amount_three + tax_amount_four + tax_amount_five
            return self.payee

    def getNHIF(self):
        gross = self.gross_salary - self.nssf - self.payee
        if gross >= 100000:
            self.nhif = 1700
            return self.nhif
        elif gross >= 90000 and gross  <= 99999:
            self.nhif = 1600
            return self.nhif
        elif gross >= 80000 and gross <= 89999:
            self.nhif = 1500
            return self.nhif
        elif gross >= 70000 and gross  <= 79999:
            self.nhif = 1400
            return self.nhif
        elif gross >= 60000 and gross <= 69999:
            self.nhif = 1300
            return self.nhif
        elif gross >= 50000 and gross <= 59999:
            self.nhif = 1200
            return self.nhif
        elif gross >= 45000 and gross <= 49999:
            self.nhif = 1100
            return self.nhif
        elif gross >= 40000 and gross <= 44999:
            self.nhif = 1000
            return self.nhif
        elif gross >= 35000 and gross <= 39999:
            self.nhif = 950
            return self.nhif
        elif gross >= 30000 and gross <= 34999:
            self.nhif = 900
            return self.nhif
        elif gross >= 25000 and gross <= 29999:
            self.nhif = 850
            return self.nhif
        elif gross >= 20000 and gross <= 24999:
            self.nhif = 750
            return self.nhif
        elif gross >= 15000 and gross <= 19999:
            self.nhif = 600
            return self.nhif
        elif gross >= 12000 and gross <= 14999:
            self.nhif = 500
            return self.nhif
        elif gross >=  8000 and gross <= 11999:
            self.nhif = 400
            return self.nhif
        elif gross >=  6000 and gross <= 7999:
            self.nhif = 300
            return self.nhif
        elif gross <= 5999:
            self.nhif = 150
        return self.nhif
# Tier  Pensionable Pay # I     Up to 6, 000
    def get_NSSF(self):
         # pensionable_pay = self.gross_salary * 1# time/years
         # if pensionable_pay >= 6000:
         #     self.nssf = 0.06 * pensionable_pay
         #     return self.nssf
         pensionable_pay = self.gross_salary
         if pensionable_pay <= 6000:
          self.nssf = 0.06 * pensionable_pay
          return self.nssf
         if pensionable_pay > 6000 and pensionable_pay < 18000:
           self.nssf = 0.06 * 6000 + 0.06 * (pensionable_pay - 6000)
           return self.nssf
         if pensionable_pay >= 18000:
            self.nssf = 0.06 * pensionable_pay
            return self.nssf
    # NetPay = GrossPay – Deductions
    def get_NetSalary(self):
        self.net_salary = self.gross_salary - self.payee - self.nssf - self.nhif
        return self.net_salary
