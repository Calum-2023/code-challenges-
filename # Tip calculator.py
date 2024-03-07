#Tip calculator - day 2

""" Goal - build a tip calculator 

Ask total bill amount
Ask how many people to split the tip by 
Ask percentage tip
Print the amount each person has to pay 

Process 
User input bill amount
User input amount to split bill by
User input tip percentage (10%, 12% or 15%)
output value each person should pay"""

print ("Welcome to the tip calculator.")

bill_total = (float(input("How much was your total Bill? £")))

party_number = (int(input("How many people are in your party? ")))

tip = (int(input("What percentage tip would you like to leave? 10, 12 or 15 ")))

bill_with_tip = tip / 100 * bill_total + bill_total

split_bill = bill_with_tip / party_number

final_amount = "{:.2f}".format(split_bill)

print (f"Your bill comes to £{final_amount} each.")