def prime_number(limit):
    for i in range(1, limit+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


limit = int(input("Enter the limit:"))
prime_number(limit)
