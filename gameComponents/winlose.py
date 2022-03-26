from gameComponents import gamevariables

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
		gamevariables.player_lives = gamevariables.total_lives
		gamevariables.computer_lives = gamevariables.total_lives
		gamevariables.player_choice = False
	else:
		print("please make a valid choice - Y or N?")
		#this might generate a bug that we need to fix later
		choice = input("Y / N?")