# Fibonacci Series
#  0        1        1     2 3 5 8 13 ....
# (i-2)0  (i-1)=1  i=2

n = int(input("Enter number of Fibonacci terms required: "))

fiboseries = [0,1]

for i in range(2,n):
	fiboseries.append(fiboseries[i-2]+fiboseries[i-1])

for i in fiboseries:
	print(i,end=" ")