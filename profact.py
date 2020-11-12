#profact.py
#Author: Fatima Khan 500766544

n = int(input("Enter a positive integer:\n"))
fact = 1

for i in range(1,n+1):
    fact = fact * i

print (str(n)+"! = ", end="")
print(fact)
