from gameComponents import gamevariables

if gamevariables.computer_choice == gamevariables.player_choice:
	print("you both lose ya bafoons!")
elif gamevariables.computer_choice == "rock":
	if gamevariables.player_choice == "scissors":
		print("you lose haaahaaaa! player lives: ", gamevariables.player_lives)
		#verbose way
		# player_lives = player_lives - 1
		#simplified way
		gamevariables.player_lives -= 1
	else:
		print("WINNER WINNER CHICKEN DINNER! player lives: ", gamevariables.computer_lives)
		gamevariables.computer_lives -= 1
elif gamevariables.computer_choice == "paper":
	if gamevariables.player_choice == "scissors":
		print("you lose haaahaaaa! player lives: ", gamevariables.player_lives)
		gamevariables.player_lives -= 1
	else:
		print("WINNER WINNER CHICKEN DINNER!", gamevariables.computer_lives)
		gamevariables.computer_lives -= 1
elif gamevariables.computer_choice == "scissors":
	if gamevariables.player_choice == "paper":
		print("you lose haaahaaaa! player lives: ", gamevariables.player_lives)
		gamevariables.player_lives -= 1
	else:
		print("WINNER WINNER CHICKEN DINNER!", gamevariables.computer_lives)
		gamevariables.computer_lives -= 1
elif gamevariables.computer_choice == "rock":
	if gamevariables.player_choice == "paper":
		print("you lose haaahaaaa! player lives: ", gamevariables.player_lives)
		gamevariables.player_lives -= 1
	else:
		print("WINNER WINNER CHICKEN DINNER!", gamevariables.player_lives)
		gamevariables.computer_lives -= 1