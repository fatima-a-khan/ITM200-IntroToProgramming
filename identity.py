# identity.py
# Author: Fatima Khan 500766544

n = int(input("Enter a positive integer: \n"))

for r in range(0, n):
        for c in range(0, n):
            if r == c:
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()


