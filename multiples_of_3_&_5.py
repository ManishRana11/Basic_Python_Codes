def multiple(limit):
    a = []
    for i in range(0, limit+1):
        if i % 3 == 0 or i % 5 == 0:
            a.append(i)
    print(a)
    print(sum(a))


limit = int(input("Set limit:"))
multiple(limit)
