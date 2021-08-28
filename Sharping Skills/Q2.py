#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

#Question and Its Code
#Small factorials Problem Code:FCTRL2

def factorial(n):
	# if n <= 0:
	# 	return 1
	# else:
	# 	return n * factorial(n-1)
	ans = 1
	while n>0:
		ans *= n #ans = ans * n
		n = n-1
	return ans

t = int(input())
for i in range(t):
	n = int(input())
	print(factorial(n))


#Factorial
# n! = n*n-1!
# eg. 5! = 5*4*3*2*1*1 = 120