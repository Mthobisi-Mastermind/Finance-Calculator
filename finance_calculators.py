# PROGRAM CALCULATES AMOUNT TO BE EARNED FROM AN INVESTMENT AND/OR MONTHLY BOND REPAYMENT AMOUNT
import math

# User selects the type of calculation they want to do, with an explanation for each type of calculation
calculation_type = input('''Choose either 'investment' or 'bond' from the menu below to proceed: \n
Investment- to calculate the amount you will have after investing for a certain period.
Bond- to calculate the amount you will have to repay monthly on a home loan. \n-''')

calc_type = calculation_type.strip(" ").capitalize()     # Input from user is stripped of any leading or trailing spaces
                                                         # First letter of input is then capitalized so the user doesn't have to worry about case sensitivity

# IF USER WISHES TO CALCULATE AN INVESTMENT:
# In the following section the Program will prompt the user for all the info needed to do an investment calculation.
# \n is used for appearance neatness to the user
if (calc_type == "Investment"):
     deposit_amount = float(input("\nPlease enter the amount you are willing to deposit: \n-R"))
     interest_rate = float(input("\nPlease enter the interest rate.\n(Do not include '%', enter the number only e.g '12' instead of '12%') : \n-"))
     years = float(input("\nEnter the number of years you planning on investing for: \n- "))
     interest_type = input("\nDo you want simple interest or compound interest? \n Enter 'Simple' or 'Compound' \n-")
     int_type = interest_type.strip().capitalize() # Interest type is stripped of any empty leading and trailing characters and capitalized for compatibility

     # Nested elif statement:
     # Calculation and amount will be as follows if user chose simple interest in the interest type
     if (int_type == "Simple"):               
         amount_earn = (deposit_amount)*(1+((interest_rate/100)*years))                                         # Simple interest formula
         print("\nAmount to be earned at the end of the investment period is R" + str(round(amount_earn, 2)))   # Display of amount at the end of investment
         
     # Calculation and amount will be as follows if user chose compound interest in interest type
     elif (int_type == "Compound"):
           amount_earn = (deposit_amount)*((1+interest_rate/100)**years)                                        # Compound interest formula
           print("\nAmount to be earned at the end of the investment period is R" + str(round(amount_earn, 2))) # Display of amount at the end of investment

     # Error message to user when neither SIMPLE or COMPOUND was selected on the interest type        
     else :
          print("\nYou did not enter Simple or Compound. Please try again!")

          
# IF USER WISHES TO CALCULATE BOND REPAYMENT AMOUNT:
# Program will prompt the user for all the needed details to perform a bond repayment calculation
# \n is used for spacing between sentences for neatness
elif (calc_type == "Bond"):
           pv = float(input("\nPlease enter the present value of the house: \n-R"))
           r_ann = float(input("\nPlease enter the annual interest rate.\n(Do not include %, enter the number only. E.g '12' instead of '12%') : \n-"))
           n = float(input("\nPlease enter the number of months that will be taken to repay the loan: \n-"))
           r = (r_ann/100)/12                                                                # Converting annual interest to monthly interest rate for accuracy calculations
           repay_monthly = (pv)*(((r*(1+r)**n))/(((1+r)**n)-1))                              # Repayment formula 
           print("\nYour monthly repayment amount will be R" + str(round(repay_monthly, 2))) # Display of the monthly repayment amount to user
# Error message to user when neither 'INVESTMENT' OR 'BOND ' was not choosen           
else:
        print("\nYou did not enter Investment or Bond. Please try again!")



    

