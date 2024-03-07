#award

""" 
Task requirement 
record times each user completes 3 tasks - Swimming, Running and Cycling
record the time for each event in mins and add them together to display the total time 
show the qualification award based on the time

Process 
create variable for each event
get user to input time for each event
add 3 times together
output total time for triathlon 
depending on time taken, output following message after time to show the award
0-100 mins - Provincial Colours
101 - 105 mins - Provincial Half Colours 
106 - 110 mins - Provincial Scroll
111+ mins - No award 
"""

swimming_time = input("Please enter your Swimming time ")
running_time = input("Please enter your Running time ")
cycling_time = input("Please enter your cycling time ")
# Set up variables to gather each time (currently string, need to change to int before we can use in arithmetic operators)

triathlon_total_time = ((int(swimming_time)) + (int(running_time)) + (int(cycling_time)))
# Changed str into int and put all three events into 1 time

print ("Congratulations, your Triathlon time is " + (str(triathlon_total_time)) + "mins") 
# convert int variable triathlon_total_time into str to output print
# printed total time for triathlon - output on line 13 achived 

if triathlon_total_time <=100:
    print ("You have achived the highest award, Provincial Colours")
# create award output if less than or equal too for the highest award

elif triathlon_total_time >=101 and triathlon_total_time <= 105:
    print ("You have achived a high award of, Provincial Half Colours ")

elif triathlon_total_time >= 106 and triathlon_total_time <= 110:
    print ("You have achived, Provincial Scroll")
# both elif output need to be between or equal to the two numbers given

else:
    print ("Unfortunatley this time, you have not qualified for a reward, better luck next time")
# the final output can be else as anything over 100 is no award 

