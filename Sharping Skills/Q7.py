#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

#Question and Its Code
#Second Largest Problem Code: FLOW017

for i in range(int(input())):
	# #Method 1
	# a,b,c = map(int,input().split())
	# print(a,b,c)

	# #Method 2
	# n = input()
	# n = n.split(' ')
	# n = list(map(int,n))
	# a = n[0]
	# b = n[1]
	# c = n[2]

	#method3
	arr = list(map(int,input().split()))

	#method1
	arr.sort()
	print(arr[1])

