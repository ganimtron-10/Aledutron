#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

n = int(input())

arr = []

for i in range(n):
	arr.append(int(input()))


print("Max Element is ",max(arr))
print("Min Element is ",min(arr))

print("Sum is ",sum(arr))
print("Avg is ",int(sum(arr)/n))