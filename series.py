#series.py
#Author: Fatima Khan 500766544

import sys

x = float(input("Enter the value of x: \n"))
n = int(input("Enter the value of n: \n"))

op = 1
sum = 0
count = 1
if (n % 2 == 1) and (n > 0) and (x>0) and (x < 10):
    formula = True
else:
    sys.exit()

for count in range (1, n + 1, 2):
    prime = True
    fact = 1

    for i in range (count, 0, -1):
        if (i % fact) == 0:
            prime = False
        fact = (fact * i)

    exp = (x ** count) / fact
    sum = sum + exp * op
    op = -1 * op

print("Sum: ", sum)

