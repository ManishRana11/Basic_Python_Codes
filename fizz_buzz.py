def fizz_buzz(a):
    if a % 5 == 0 and a % 3 == 0:
        return "Fizz Buzz"
    elif a % 3 == 0:
        return "Fizz"
    elif a % 5 == 0:
        return "Buzz"
    else:
        return a


a = int(input("Enter the number:"))
print(fizz_buzz(a))
