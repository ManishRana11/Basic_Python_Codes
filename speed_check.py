def speed_check(speed):
    if speed <= 70:
        print("OK")
    else:
        speed1 = ((speed-70) // 5)
        if speed1 <= 12:
            print(f"{speed1} demerit points")
        else:
            print("Licence suspended")


speed = int(input("Enter the speed:"))
speed_check(speed)
