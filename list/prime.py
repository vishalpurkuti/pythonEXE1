def isPrime(num):
    k = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                k += 1

        if k > 0:
            print("No Prime")
        else:
            print("prime")
    else:
        print("invalid no.")


isPrime(int(input("Enter an integer:")))
