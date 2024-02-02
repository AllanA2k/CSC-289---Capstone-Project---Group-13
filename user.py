class User:

    def __init__(self, first, last, taxable_amount, total_income):
        self.first = first
        self.last = last
        self.taxable_amount = taxable_amount
        self.total_income = total_income
        # https://www.ncdor.gov/taxes-forms/individual-income-tax/north-carolina-standard-deduction-or-north-carolina-itemized-deductions
        # standard deduction for single status is $12,750.
        # income tax rate is 4.75%
        
        standard_deduction = 12750 if taxable_amount == "Single" else 0
        taxable_income = max(0, total_income - standard_deduction)
        
        self.tax = round(taxable_income * 0.0475, 2)


