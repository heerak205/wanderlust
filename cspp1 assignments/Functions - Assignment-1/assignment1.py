"""
# Functions | Assignment-1 - Paying Debt off in a Year

# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the
# credit card company each month.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135

# So your program only prints out one thing: the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0

# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
def paying_Debt_Off_In_A_Year(p_balance, p_annualinterestrate, p_monthlypaymentrate):
    """
    This takes balance, annual interest rate, monthly payment rate
    """
    for p_pb in range(12):
        p_pb = p_balance
        p_mir = (p_annualinterestrate)/12.0
        p_mmp = p_monthlypaymentrate*p_pb
        p_mub = p_pb - p_mmp
        p_balance = p_mub + (p_mir*p_mub)
    p_balance = round(p_balance,2)
    print("Remaining balance: " + str(p_balance))

def main():
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    paying_Debt_Off_In_A_Year(data[0], data[1], data[2])

if __name__ == "__main__":
    main()

