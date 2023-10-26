n = int(input("enter a positive integer : "))

# list to store the numbers
numbers = []

# read N 
for i in range(n):
    num = int(input(f"enter {i + 1}.th number: "))
    numbers.append(num)


X = int(input("enter X"))

# check if x is in the list and find its index
if X in numbers:
    index = numbers.index(X) + 1
    print(f"index of {X}: {index}")
else:
    print("-1")
