#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

#Question and Its Code
#Reverse The Number Problem Code: FLOW007

#Method 1
for i in range(int(input())):
	n = input()
	
	print(int(n[::-1]))


#Method 2
for i in range(int(input())):
	n = input()
	revn = ''
	for i in n:
		revn = i + revn
	print(int(revn))

#  '' -> revn = '1' + '' -> revn = "1"
# revn = '2' + '1' -> "54321"