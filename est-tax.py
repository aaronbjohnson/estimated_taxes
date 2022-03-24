from decimal import * 

"""Note, you'll have to remake parts of this if Aline starts working again, or you
get a W2 somehow. In short, instead of just using income, you'll have to add all income
together and save that as AGI variable"""

## should run with python -i 'nameofprogram' to run and then go straight into interpreter.

# intialize constants
STANDARD_DEDUCTION = Decimal('25100')
QBI_RATE = Decimal('0.2')
LOWER_BOUND_TAX_TABLE = Decimal('20550') # Will need to change this if your income significantly increases (hopefully so)
TAX_TABLE_ADD = Decimal('2055') # Just got this from the correct row of tax table for 2022
TAX_TABLE_ROW_RATE = Decimal('0.12') # Got this percentage from correct row of tax table 2022
SE_TAX_MULTIPLIER = Decimal('0.9235')
SE_LINE_9_MULTIPLIER = Decimal('0.124') 
CENTS = Decimal('.01')

def main():

    # get earnings so far for the year
    raw_income = input('Enter your income so far this year (no commas): ')
    quarters_paid = Decimal(input("How many quarterly payments have you made so far: "))
    paid_so_far = Decimal(input("How much have you paid in estimated taxes so far: "))
    income = Decimal(raw_income)
    qbi = income * QBI_RATE
    taxable_income = income - (STANDARD_DEDUCTION + qbi)
    tax_table_amt = get_tax_table_amt(taxable_income) 
    se_tax = get_self_employment_tax(income)
    total_tax_liability = Decimal(tax_table_amt + se_tax)
    ninety_percent = Decimal(total_tax_liability * Decimal('0.9'))
    quarter_payment = compute_quarter_payment(ninety_percent, quarters_paid)
    print()
    print("You should pay " + str(quarter_payment) + " for quarter " + str((1 + quarters_paid)) + ".")

def compute_quarter_payment(remaining_due, quarters_paid):
    quarters_remaining = 4 - quarters_paid
    payment = remaining_due / quarters_remaining
    formatted_payment = payment.quantize(CENTS, ROUND_HALF_UP)
    return formatted_payment

assert compute_quarter_payment(Decimal('10032.25'), 0) == Decimal('2508.06') 
    

def get_self_employment_tax(income):
    line_3 = Decimal(income * SE_TAX_MULTIPLIER)
    intermediate = Decimal(line_3 * SE_LINE_9_MULTIPLIER)
    unformatted_tax = Decimal(intermediate + Decimal(line_3 * Decimal('0.029')))
    formatted_tax = unformatted_tax.quantize(CENTS, ROUND_HALF_UP)
    return formatted_tax 



assert get_self_employment_tax(Decimal('61400')) == Decimal('8675.54')

def get_tax_table_amt(agi):
    return (TAX_TABLE_ADD + ((agi - LOWER_BOUND_TAX_TABLE) * TAX_TABLE_ROW_RATE))


def compute_est_tax(total_income:Decimal) -> Decimal:
   return Decimal('2508.06') 

assert compute_est_tax(Decimal('15350')) == Decimal('2508.06')


# Call the main function
main()
