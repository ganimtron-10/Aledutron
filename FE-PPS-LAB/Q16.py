inputfile = open("FE-PPS-LAB/input.txt",'r')
outputfile = open("FE-PPS-LAB/output.txt",'w')

content = list(inputfile.read())

print("".join(content))

for i in range(len(content)):
	if content[i] == ".":
		content[i] = ","
	if content[i].islower():
		content[i] = content[i].upper()
	else:
		content[i] = content[i].lower()

outputfile.write("".join(content))