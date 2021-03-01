def maximum_number(x1, x2):
    if x1 > x2:
        print(f"{x1} is greater")
    else:
        print(f"{x2} is greater")


x1 = int(input("Enter the first number:"))
x2 = int(input("Enter the second number:"))
maximum_number(x1, x2)

# Alternate way
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
maximum = max(a, b)
print(maximum)
