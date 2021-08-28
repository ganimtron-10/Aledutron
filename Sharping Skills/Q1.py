#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

#Question and Its Code
# ATM Problem Code:HS08TEST

t = input()
t = t.split(' ')
x = int(t[0])
y = float(t[1])


if x%5 == 0 and (x+0.5) < y:
	print("{:0.2f}".format(y-(x+0.5)))
else:
	print("{:0.2f}".format(y))