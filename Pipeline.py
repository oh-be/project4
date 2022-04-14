import pandas as pd
import numpy as np


def investment_calc(rent, total_price, maintenance, insurance, taxes): 
    # taxes = taxes/12
#def rent_total(rent):
    monthly_rent = rent
    yearly_rent = rent * 12
    #return monthly_rent, yearly_rent

#def gross_rent_multiplier (total_price, yearly_rent):
    GRM = total_price / yearly_rent
    GRM = "{:.2f}".format(GRM)
    #return GRM

#def operating_expenses(maintenance, insurance, taxes, management, other):
    op_ex = (maintenance + insurance + taxes + management + other)
    op_exyearly = (maintenance + insurance + taxes + management + other) * 12
    #return op_ex_monthly, op_ex_yearly

#def noi(monthly_rent, op_ex_monthly, yearly_rent, op_ex_yearly):
    noi_monthly = monthly_rent - op_ex
    noi_yearly = yearly_rent - op_exyearly
    #return noi_monthly, noi_yearly

#def one_percent_rule(monthly_rent, total_price):
    one_percent = (total_price * .01)
    boolean = monthly_rent >= one_percent
    #return boolean

#def cap_rate(noi_yearly, total_price):
    c_rate = (noi_yearly / total_price)*100
    c_rate = "{:.2f}".format(c_rate)
    #return c_rate
    
    results = {
        'Cap Rate': c_rate,
        'Gross Rent Multiplier': GRM,
        'Net Operating income (Monthly)': noi_monthly,
        'Net Operating income (Annual)': noi_yearly,
        'Is the One Percent Rule in effect?': boolean
    }
    
    return results

# rent = int(input('Enter Approximate Monthly Rent'))
# total_price = int(input('Enter Total Property Price'))
# maintenance = int(input('Enter Approximate Monthly Property Maintenance Cost'))
# insurance = int(input('Enter Approximate Monthly Property Insurance Cost'))
# taxes = (int(input('Enter Approximate Yearly Property Tax'))) / 12
# management = int(input('Enter Approximate Monthly Property Management Cost'))
# other = int(input('Enter Any other Approximate Monthly Property Expenses'))

    
# c_rate, GRM, noi_monthly, noi_yearly, boolean = investment_calc(rent, total_price, maintenance, insurance, management, taxes, other)
    
# print('\n')
# print(f'Cap Rate: {c_rate}%')
# print(f'Gross Rent Multiplier: {GRM}')
# print(f'Net Operating income: ${noi_monthly} Monthly')
# print(f'Net Operating income: ${noi_yearly} Annual')
# print(f'Is the One Percent Rule in effect?: {boolean}')

# Cap Rate: 7.18%
# Gross Rent Multiplier: 7.92
# Net Operating income: $1136.5 Monthly
# Net Operating income: $13638.0 Annual
# Is the One Percent Rule in effect?: True