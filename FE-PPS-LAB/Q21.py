# Program that simulates rolling dice. When the program runs, it will randomly choose a
# number between 1 and 6 (Or other integer you prefer). Print that number. Request user to
# roll again. Set the min and max number that dice can show. For the average die, that
# means a minimum of 1 and a maximum of 6.


import random

user_input = 'y'
while user_input == 'y':

	low = int(input("Enter a minimum value to be shown on dice: "))
	high = int(input("Enter a maximum value to be shown on dice: "))

	print("The Random Value is",random.randint(low, high))
	user_input = input("Wanna Roll the Dice Again(y/n): ")
