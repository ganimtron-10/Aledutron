# #Setup Code
# import sys

# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')

# ###########################################
# #Real Code Starts

mass = float(input())
velocity = float(input())

# momentum = mass * velocity * velocity

momentum = mass * (velocity**2)

print(f"momentum of mass {mass}kg and velocity {velocity}m/s is {momentum}kgm/s")