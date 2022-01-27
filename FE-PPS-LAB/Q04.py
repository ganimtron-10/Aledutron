#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

def grade_cal(per):
	if per>75:
		return "Distinction"
	elif per >= 60 and per<75:
		return "First Div"
	elif per >= 50 and per<60:
		return "Second Div"
	elif per >= 40 and per<50:
		return "Third Div"

for i in range(int(input())):
	arr = list(map(int,input().split()))
	iseligible = all(x>=40 for x in arr)
	# print(iseligible)
	stud_per = sum(arr)/5
	# print(stud_per)
	if iseligible:
		print(f"You Obtained {stud_per}% and Your Grade is {grade_cal(stud_per)}")
	else:
		print("You failed!!")