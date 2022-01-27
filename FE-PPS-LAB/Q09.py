# Method 1 - Strings
# number = input("Enter a number: ")

# -3 -2 -1
# 234 = 432 ->  
# 012

# 023 --> 23 -> 32

# for i in range(len(number)-1,-1,-1):
# 	print(number[i],end="")

# for i in range(1,len(number)+1):
# 	print("i is ",-i)
# 	print(number[-i])


# number = number[::-1] #a-starting index(0) , b-ending index(last index), c-step(1)
# print(number)

# revnum = ''

# for i in number:
# 	revnum = i + revnum  # revnum = '2' + '' -> '2'
# 							# revenum = '3' + '2' -> '32'
# 							# revenum = '4' + '32' -> '432'
# print(revnum)


# Method 2 - Int
# number = int(input("Enter a number: "))

# numofdigit = len(str(number))

# 234 - 4 3 2
		# 23 - quotient (// floor division)
  #  10 | 234
  #      -230
  #         4 - remainder (% modulus)



# revernum = ""

# for i in range(numofdigit):
# 	revernum += str(number % 10)
# 	number = number // 10

# print(revernum)

