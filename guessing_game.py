"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
Written by Dan Reyes-Cairo
--------------------------------
"""

import random
import os

best_score = 0

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


def start_game():

	playing = True
	best_score = 0
	answer = random.randrange(1, 101)
	attempts = 0
	lower_guess = 0
	upper_guess = 0

	clear_screen()
	input("Welcome to the Number Master guessing game!\n\nTry to guess a number between 1 and 100 in as few attempts as possible!\n\n(Press ENTER)")

	while playing == True:
		clear_screen()
		print("** Number Master **")
		print("\nTry to guess a number between 1 and 100 in as few attempts as possible!\n")

		if best_score > 0:
			print("BEST SCORE: {} (Can you beat it?)\n".format(best_score))
		else:
			pass

		print("Low guess: {}".format(lower_guess))
		print("High guess: {}".format(upper_guess))
		print("\nEnter your guess here (or 'QUIT' at any time):  ")

		try:
			guess = input(">  ")
			if guess.lower() == 'quit':
				clear_screen()
				quit_response = input("Are you sure you want to quit? [Y/n]")
				if quit_response.upper() == 'Y':
					print("\nSorry to see you go. Come back soon!\n")
					break
				elif quit_response.upper() == "N":
					continue
				else:
					input("\nCouldn't say yes, could ya?\n\n(Press ENTER)")
					continue
			elif guess.isdigit() == False:
				raise ValueError
			else:
				pass

		except ValueError:
				input("\nI'm sorry, '{}' is not a valid number! Please try again.\n\n(Press ENTER)".format(guess))
		else:
			guess = int(guess)
			if guess > 100:
				input("\nI'm sorry, please choose a number lower than 100\n\n(Press ENTER)")
				continue
			elif guess < 1:
				input("\nI'm sorry, please choose a number greater than 1\n\n(Press ENTER)")
				continue
			elif guess > answer:
				if  upper_guess == 0:
					upper_guess = guess
				elif guess < upper_guess:
					upper_guess = guess
				else:
					input("\n ** Please enter a number less than {} **\n(Press ENTER)".format(upper_guess))
					continue

				attempts += 1
				input("\n ** The answer is lower than that, please try again! **\n\n(Press ENTER)")
				continue
			elif guess < answer:
				if lower_guess == 0:
					lower_guess = guess
				elif guess > lower_guess:
					lower_guess = guess
				else:
					input("\n ** Please enter a number greater than {} **\n\n(Press ENTER)".format(lower_guess))
					continue
				attempts += 1
				input("\n ** The answer is higher than that, please try again! **\n\n(Press ENTER)")
				continue
			else:
				clear_screen()
				print("\nYou guessed it! Great job.\n")
				print("Attempt count: {}\n".format(attempts))
				if best_score == 0:
					best_score = attempts
				elif attempts < best_score:
					print("You beat the best score, congratulations!!")
					best_score = attempts
				else:
					pass

				play_again = input("Would you like to play again? [Y/n]\n>  ")
				if play_again.upper() == 'N':
					clear_screen()
					print("\nThanks for playing. See you soon!\n")
					playing = False
				else:
					attempts = 0
					lower_guess = 0
					upper_guess = 0
					pass


if __name__ == '__main__':
	start_game()
