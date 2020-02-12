square = []


def squre(n1, n2):
    for i in range(n1+1, n2):
        square.append(i*i)
    print(square)


squre(int(input("Enter first integer:")), int(input("Enter second integer:")))
