import random
choices = { 1: 'Bust', 2: 'Bust', 3: 'Bust'}
choices[random.randrange(1,4)] = "Car"
playerChoice = raw_input("Please choose a curtain(1,2 or 3) ")
if(playerChoice != 1 or playerChoice != 2 or playerChoice != 3):
    print("That is not a valid option")
else:
    ####Start here

for choice in choices:
    print (choices[choice])
    
