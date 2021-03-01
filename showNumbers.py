def showNumbers(limit):
    for i in range(0, limit+1):
        if i % 2 == 0:
            print(f"{i} EVEN")
            continue
        else:
            print(f"{i} ODD")
            continue


limit = int(input("Set the limit:"))
showNumbers(limit)