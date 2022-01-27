#Setup Code
import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

###########################################
#Real Code Starts

basic_pay = int(input())

hra = 10/100 * basic_pay
ta = 5/100 * basic_pay

gross_salary = int(basic_pay + hra + ta)

pt = 2/100 * gross_salary

net_salary = gross_salary - int(pt)

print(net_salary)