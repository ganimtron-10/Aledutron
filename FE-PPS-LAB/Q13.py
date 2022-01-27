# To accept the number of terms a finds the sum of sine series.

# sin(a) + sin(a+b) + sin(a+2b) + sin(a+3b) + ..... + sin(a+(n-1)b)


# num_of_terms = int(input("Enter the number of terms required in sine serires: "))


# for n in range(num_of_terms):
# 	if n == 0:
# 		print("sin(a)", end = '')
# 		continue
# 	print(f" + sin(a+{n}b)",end = '')

import math

num_of_terms = int(input("Enter the number of terms required in sine serires: "))
a = int(input("Enter Initial Angle(a): "))
b = int(input("Enter Incremental Angle(b): "))

sum_of_sine = 0

for n in range(num_of_terms):
	if n == 0:
		print(f"sin({a})", end = '')
		continue
	print(f" + sin({a+n*b})",end = '')
	sum_of_sine += math.sin(a+n*b)

print(f"\nSum of Sine upto {num_of_terms} terms is {sum_of_sine}")
