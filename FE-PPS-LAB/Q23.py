# Guess Number: Randomly generate a number unknown to the user. The user needs to
# guess what that number is. If the user’s guess is wrong, the program should return some
# sort of indication as to how wrong (e.g. the number is too high or too low). If the user
# guesses correctly, a positive indication should appear. Write functions to check if the user
# input is an actual number, to see the difference between the inputted number and the
# randomly generated numbers, and to then compare the numbers.

import random

def guess_num(low=0,high=100):
	num = random.randint(low, high)

	while True:
		player_input = int(input("Enter your Guess: "))
		if player_input == num:
			print("Congratulations!! You Guessed Correct!!")
			break
		else:
			if(player_input < num):
				print("Actual Number is Greater than your guess!!")
			if(player_input > num):
				print("Actual Number is Less than your guess!!")



guess_num()