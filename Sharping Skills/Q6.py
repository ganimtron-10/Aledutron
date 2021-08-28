#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

#Question and Its Code
#Finding Square Roots Problem Code: FSQRT

import math

for i in range(int(input())):
    n = int(input())
    ans = math.sqrt(n)
    print(int(ans))

# #checking int working
# print(math.floor(3.01),math.floor(3.7))