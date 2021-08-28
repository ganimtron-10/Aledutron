#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

#Question and Its Code
#Lucky Four Problem Code: LUCKFOUR

for i in range(int(input())):
	n = input()
	counter = 0
	for i in n:
		if i == "4":
			counter += 1
	print(counter)

