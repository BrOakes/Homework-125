import random
while True:
	playerInput = raw_input("Choose your weapon(Rock, Paper, Scissors)! ")
	if playerInput.lower() != "scissors" and playerInput.lower() != "rock" and playerInput.lower() != "paper":	print("Thats not a valid choice")
	else:
		computerChoice = random.randrange(3)
		if(computerChoice == 0 and playerInput.lower() == "paper" or computerChoice == 1 and playerInput.lower() == "scissors" or computerChoice == 2 and playerInput.lower() == "rock"):	print("You Win!")
		elif(computerChoice == 0 and playerInput.lower() == "rock" or computerChoice == 1 and playerInput.lower() == "paper" or computerChoice == 2 and playerInput.lower() == "scissors"):	print ("Draw!")
		else:	print("Get ReKt m9!")