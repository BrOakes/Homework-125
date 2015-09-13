import random
winLoss = []
for num in range(0,50):
	choices = { 1: 'Bust', 2: 'Bust', 3: 'Bust'}
	choices[random.randrange(1,4)] = "Car"
	# playerChoice = raw_input("Please choose a curtain(1,2 or 3) ")
	playerChoice = random.randrange(1,4)
	optionLeft = 0
	if(int(playerChoice) != 1 and int(playerChoice) != 2 and int(playerChoice) != 3):
	    print("That is not a valid option")
	else:
		prize = choices[int(playerChoice)]
		del choices[int(playerChoice)]
		for choice in choices:
			if choices[choice] == "Bust":
				del choices[choice]
				break
		for choice in choices:
			optionLeft = choice
	# switch = raw_input("We have removed one of the options, the only option left is " + str(optionLeft) + ". Would you like to swap? (y or n) ")
	switch = 'y'
	if(switch == 'y'):
		playerChoice = optionLeft
		prize = choices[int(playerChoice)]

	# print(choices[playerChoice])
	if (prize == "Car"):
		winLoss.append("W")
	else:
		winLoss.append("L")

print(winLoss)
	#print("Behind the curtain you chose is a " + prize)
