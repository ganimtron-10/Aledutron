#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

# Method 1
# for i in range(int(input())):
# 	n = input()
# 	if len(n) == 3:
# 		fn = int(n[0])
# 		sn = int(n[1])
# 		tn = int(n[2])
# 		sumofc = fn**3+sn**3+tn**3
# 		if int(n) == sumofc:
# 			print("Its Armstrong NUmber.")
# 		else:
# 			print("Its not an Armstrong Number.")
# 	else:
# 		print('Give Three Digit Number.')


# Method2
for i in range(int(input())):
	n = int(input())
	if n>99 and n<1000:
		fn = (n%10)
		sn = ((n//10)%10)
		tn = ((n//10)//10)
	if n == (fn**3+sn**3+tn**3):
		print('Yes')
	else:
		print("no")