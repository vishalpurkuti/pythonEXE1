def calledis_sorted(num):
    k = 0
    for x in range(0, len(num)):

        for y in range(x+1, len(num)):
            if num[x] >= num[y]:
                k += 1
    if k < 1:
        return True
    else:
        return False


n = input("Enter array element seperated by space:")
a = n.split()
if calledis_sorted(a) == True:
    print("Sorted list")
else:
    print("Not sorted list")
