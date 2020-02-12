def divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False


if(divisible(int(input("1st Num:")), int(input("2nd Num:")))) == True:
    print("Divisible")
else:
    print("Not divisible")
