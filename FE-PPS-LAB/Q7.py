#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts
import math


def isPrime(n):
	# 2 - (n-1) is dividing n or not
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n-1)

def findprimefactors(n):
	primelist = []
	for i in range(2,n):
		if isPrime(i) and n%i == 0:
			primelist.append(i)
	if isPrime(n):
		primelist.append(n)
	return primelist



for i in range(int(input())):
	n = int(input())

	print(f"Square root of {n} = {math.sqrt(n)}")
	print(f"Square of {n} = {n**2}")
	print(f"cube of {n} = {n**3}")

	if isPrime(n):
		print(f"{n} is prime")
	else:
		print(f"{n} is  not prime")

	print(f"factorial of {n} is {fact(n)}")

	print(f"Prime factors of {n} are :")
	for i in findprimefactors(n):
		print(i)

	print()