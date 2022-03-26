from random import randint

# re-import game variables
from gameComponents import gamevariables, winlose

# player_choice == False
while gamevariables.player_choice is False:
	print("===========*/ RPS GAME */===========")
	print("computer lives:", gamevariables.computer_lives, "/", gamevariables.total_lives)
	print("player lives:", gamevariables.player_lives, "/", gamevariables.total_lives)
	print("=====================================")
	print("choose your weapon!! or type quit to exit game")
	gamevariables.player_choice = input("choose rock, paper, or scissors: \n")
	#player_choice now equals TRUE -> because it has a value	

	if gamevariables.player_choice == "quit":
		print("you chose to quit")
		exit()

	gamevariables.computer_choice = gamevariables.choices[randint(0, 2)]

	print("user chose: " + gamevariables.player_choice)
	print("computer chose: " + gamevariables.computer_choice)

	if gamevariables.computer_choice == gamevariables.player_choice:
		print("tie")
	elif gamevariables.computer_choice == "rock":
		if gamevariables.player_choice == "scissors":
			print("you lose! player lives: ", gamevariables.player_lives)
			#verbose way
			# player_lives = player_lives - 1
			#simplified way
			gamevariables.player_lives -= 1
		else:
			print("you win! player lives: ", gamevariables.player_lives)
			gamevariables.computer_lives -= 1
	elif gamevariables.computer_choice == "paper":
		if gamevariables.player_choice == "scissors":
			print("you lose! player lives: ", gamevariables.player_lives)
			gamevariables.player_lives -= 1
		else:
			print("you win!")
			gamevariables.computer_lives -= 1
	elif gamevariables.computer_choice == "scissors":
		if gamevariables.player_choice == "paper":
			print("you lose! player lives: ", gamevariables.player_lives)
			gamevariables.player_lives -= 1
		else:
			print("you win!")
			gamevariables.computer_lives -= 1
	elif gamevariables.computer_choice == "rock":
		if gamevariables.player_choice == "paper":
			print("you lose! player lives: ", gamevariables.player_lives)
			gamevariables.player_lives -= 1
		else:
			print("you win!")
			gamevariables.computer_lives -= 1

	if gamevariables.player_lives == 0:
		winlose.winorlose("lose")
		
	if gamevariables.computer_lives == 0:
		winlose.winorlose("won")
		

	print("Player lives:", gamevariables.player_lives)
	print("Computer lives:", gamevariables.computer_lives)

	# map the loop keep running by setting player_choice back to False unset, so that our loop  condition will evaluate to True
	gamevariables.player_choice = False 

