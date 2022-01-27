# To count total characters in file, total words in file, total lines in file and frequency of
# given word in file.

file = open('FE-PPS-LAB/input.txt','r')

content = file.read()

charcount = len(list(content))

print("Charcount: ", charcount)


numofline = len(content.split('\n'))

print("Line Count: ", numofline)

words = content.split(' ')

for i in range(len(words)):
	if '\n' in words[i]:
		# words = words + words[i].split('\n')
		# words.remove(words[i])
		sepratewords = words[i]
		words.remove(words[i])
		words = words + sepratewords.split('\n')

wordcount = len(words)

print("Word Count: ", wordcount)


wordfreq = {}

for i in words:
	if wordfreq.get(i):
		wordfreq[i] += 1
	else:
		wordfreq[i] = 1

print("Word Frequency: ",wordfreq)
