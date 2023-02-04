# Imports "random" library
import random
# Imports "time" library
import time

# Prints welcome message
print("Welcome to: Rock, Paper Scissor\n")
# Main function
def main():
	# Input from the user
	my_input = input("Choice: ")
	
	# Takes input
	match my_input:
		# If it's rock
		case 'Rock':
			choice = 1

		# If it's paper	
		case 'Paper':
			choice = 2

		# If it's scissor
		case 'Scissor':
			choice = 3
		# If it's none of the above
		case _:
			print("Selection not avaliable. Retry")
			main()
		
	# Choses a random number
	num = random.randint(1, 3)
	match num:
		# If number it's 1, rock
		case 1:
			print("Bot: Rock")

		# If number it's 2, paper
		case 2:
			print("Bot: Paper")

		# If number it's 1, scissor
		case 3:
			print("Bot: Scissor")

	# Checks for every choice in rock, paper, scissor rules
	# If it's equal, draw
	if choice == num:
		print("Draw!")
		time.sleep(1)
	# If it's any combination of rock, paper, and scissor, victory
	elif choice == 2 and num == 1 or choice == 3 and num == 2 or choice == 1 and num == 3:
		print("Victory!")
		time.sleep(1)
	# If it's none of the above, lose
	else:
		print("Loss!")
		time.sleep(1)
	# Checks if the player wants to resart or not the game
	def repeat_func():
		# Checks for input
		repeat = input("Retry? Yes/No\n")
		# Delets the space (If there are any)
		repeat = repeat.strip(" ")
		# If it's yes, restart the game
		if repeat == 'Yes':
			print("\nRestarting Game...")
			time.sleep(1)
			main()
		# If it's no, stop the game
		elif repeat == 'No':
			# We don't talk about that...
			print("Fu**ing loser...")
			exit()
		# If it's none of the above, print the condition
		else:
			print("Input Invalid\n")
			time.sleep(1)
			repeat_func()
	# Calls the function
	repeat_func()

# Calls the function for starting the game
main()