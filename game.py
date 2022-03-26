# important packages to extend python (just like we extend sublime, atom, or VScode)
from random import randint

# [] -> this is an array
# name = [value1, value2, value3]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contents are assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3

# True or False are Boolean data types
# essentially, booleans are equivalent to an on or off switch, 1 or 0.
player_choice = False

#define a win or lose function
def winorlose(status):
	#version 1 of function
	# print("inside winorlose funtion; status is: ", status)
	print("you", status, "! would you like to play again?")
	choices = input("Y / N?")

	if choices == "N" or choices == "n":
		print("you chose to quit! better luck next time!")
		exit()
	elif choices == "Y" or choices == "y":
		#reset the player lives and computer lives
		# and then reset player choice to False, so our loop restarts
		global player_lives
		global computer_lives
		global total_lives

		player_lives = total_lives
		computer_lives = total_lives
	else:
		print("please make a valid choice - Y or N?")
		#this might generate a bug that we need to fix later
		choice = input("Y / N?")

# player_choice == False
while player_choice is False:
	print("===========*/ RPS GAME */===========")
	print("computer lives:", computer_lives, "/", total_lives)
	print("player lives:", player_lives, "/", total_lives)
	print("=====================================")
	# version 1, to explain array indexing
	# player_choice = choices[1]
	# print("index 1 in the choice array is " + player_choice + ", which is paper")

	print("choose your weapon!! or type quit to exit game\n")

	player_choice = input("choose rock, paper, or scissors: \n")
	#player_choice now equals TRUE -> because it has a value

	if player_choice == "quit":
		print("youchose to quit")
		exit()

	print("user chose: " + player_choice)

	# this will be the AI choice -> a random pick from the choice array
	computer_choice = choices[randint(0, 2)]

	print("computer chose: " + computer_choice)

	if computer_choice == player_choice:
		print("tie")

	elif computer_choice == "rock":
		if player_choice == "scissors":
			print("you lose!")
			#verbose way
			# player_lives = player_lives - 1
			#simplified way
			player_lives -= 1
		else:
			print("you win!")
			computer_lives -= 1

	elif computer_choice == "paper":
		if player_choice == "scissors":
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			computer_lives -= 1

	elif computer_choice == "scissors":
		if player_choice == "paper":
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			computer_lives -= 1

	elif computer_choice == "rock":
		if player_choice == "paper":
			print("you lose!")
			player_lives -= 1
		else:
			print("you win!")
			computer_lives -= 1

	if player_lives == 0:
		winorlose("lose")
		
	if computer_lives == 0:
		winorlose("won")
		
	print("Player lives:", player_lives)
	print("Computer lives:", computer_lives)

	# map the loop keep running by setting player_choice back to False unset, so that our loop  condition will evaluate to True
	player_choice = False 







