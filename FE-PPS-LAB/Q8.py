#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

def findlcm(a,b):
	for i in range(2,min(a,b)):
		if a%i == 0 and b%i == 0:
			return i
	return 1

def findhcf(a,b):
	for i in range(min(a,b),1,-1):
		if a%i == 0 and b%i == 0:
			return i
	return 1


for i in range(int(input())):
	a,b = map(int,input().split())
	print(f'Lcm of {a} and {b} is {findlcm(a,b)}')
	print(f'HCF of {a} and {b} is {findhcf(a,b)}',"\n")