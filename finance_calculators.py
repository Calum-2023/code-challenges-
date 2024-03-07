#finance_calculators
import math

""" 
Task 
1. show two outputs to user - invesment or bond
ask user to choose either of the two

2. caps should not effect the validity of the entry however 
if the user inputs anything other than the two options, output an error message

3. if user selects investment:
ask the following:
Deposit amount 
interest rate (output as percentage) from programme, not user
years on plan
ask user if they want simple of compound interest
output amount they will get back at the end of the given period 

4. if the user selects bond: 
ask the following:
value of property 
interest rate 
number of months they plan to take to repay the bond 
output the amount the user will have to pay each month 

process 
print description of the two options 
ask user to input one of the two options 
ensure capslock doesnt effect input however show error message if another option is input by user 

if user inputs investment 
request input for deposit amount, interest rate, years on plan and selection of type of interest
output amount they will get back a the end of the period 

if user inputs bond
request input for value of property, interest rate, number of months to repay bond
output amount they will need to pay each month

"""

print ("Investment - To calculate the amount of interest you'll earn on your investment")
print ("Bond - To calculate the amount you'll have to pay on a home loan")
print ("")
# Line 42-44 outline the options for the user

answer = input ("Enter either 'Investment' or 'Bond' from the menu above to proceed: ") # first input request 

answer_lower_case = answer.lower() #this ensures caps have no effect on output from user input

invest = "investment"
bond = "bond"
compound = "compound"
simple = "simple"
# setting up the variables for taking user input
compound_lower_case = compound.lower()
simple_lower_case = simple.lower()
# making sure the user input case does not effect output

if answer_lower_case == invest:
    # if user types investment, the value is held in variable invest. we can then request further input

    deposit = (input("Please enter deposit amout? "))
    interest_gain = (input("Please enter interest percentage amount? "))
    invest_period = (input("Please enter how many years you plan to invest your depoit? "))
    invest_type = (input)("Please choose your type of interest. Either 'simple' or 'compound' ")
    # line 62 - 65 requests more input from user

    if invest_type == simple: 
        # if user selects simple, below math is used to output line 71 from the input from line 62 - 64

        simple_interest_reduced_to_percentage = (float(interest_gain) / 100)
        simple_interest_outcome = (float(deposit) * (1 + simple_interest_reduced_to_percentage * (float(invest_period))))
        print ("if you invest using the input peramiters, your output at the end of the period will be £" + (str(simple_interest_outcome)))
    
    if invest_type == compound:
        # if user selects compound, below math is used to output information from line 62 - 64

        compound_interest_reduced_to_percentage = (float(interest_gain) / 100)
        compound_interest_outcome = (float(deposit) * math.pow((1 + compound_interest_reduced_to_percentage), (float(invest_period))))
        print ("If you invest using the input peramiters, your output at the end of the period will be £" + (str(compound_interest_outcome)))
    

elif answer_lower_case == bond:
    # if user selects bond, the below inputs are requestd 

    value = (input("Please enter the value of the property? "))
    value_num = (float(value))
    
    interest_loss = (input("Please enter the interest rate? "))
    interest_loss_num = (float(interest_loss))
    interest_loss_as_percentage = (interest_loss_num / 100) / 12 
    
    repay_period = (input("Please enter the number of months you have to repay your bond? "))
    repay_period_num = (float(repay_period))
    # converted the input from the user from str to float to make the math below simpler 

    monthly_repayment = (interest_loss_as_percentage * value_num) / (1 - (1 + interest_loss_as_percentage)**(-repay_period_num))
    print ("Your monthly repayment will be £" + (str(monthly_repayment)))

else:
    print ("Error, incorrect input")