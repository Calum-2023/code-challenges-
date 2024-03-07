
print ("Welcome to Tresure Island.")
print ("Your mission is to find the treasure")
choice1 = input ('You\'re at a crossroad, where do you want to go? \nType "Left" or "right".\n ').lower()

while choice1: 
    if choice1 == "left":
        choice2 = input ('You\'ve come into a lake. \nThere is an island in the middle of the lake. \nType "wait" to wait for the boat. Type "swim" to swim across.\n ').lower()
    
        if choice2 == "wait":
            choice3 = input ("You arrive at the island unharmed. \nThere is a house with 3doors. \none red, one yellow and one blue. Which colour do you choose.\n ").lower()
        
            if choice3 == "red": 
                print ("The room is full of fire. \nGame Over!\n")
            elif choice3 == "yellow":
                print ("You found the treasure! \nYou Win.\n")
                break
            elif choice3 == "blue":
                print ("You are attacked by a group of bandits. \nGame Over\n")
            else:
             print("You do not open any door and waste away into nothing over time. \nGame Over!\n")
        else:
            print("You got attacked by an angry croc, \nGame Over!\n")
    else:
        print ("You fell into a hole. \nGame Over.\n")
