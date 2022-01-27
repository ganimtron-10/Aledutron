n = int(input("Enter number of elements: "))

glist = []
evenl = []
oddl = []
raisedlist = ["th","st","nd","rd"]

for i in range(n):
	if not i in [1,2,3]:
		raisei = 0
	else:
		raisei = i
	x = int(input(f"Enter {i}{raisedlist[raisei]} element: "))
	glist.append(x)

for num in glist:
	if num%2 == 0:
		evenl.append(num)
	else:
		oddl.append(num)

print("Even List: ",evenl)
print("Odd List: ",oddl)