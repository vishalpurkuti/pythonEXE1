item = [1, 2, 3, 3, 1]
for i in range(0, len(item)):
    print(item[i], end=':=> ')
    if(item[i] != 0):
        print(i)
        for j in range(i+1, len(item)):
            if(item[i] != 0):
                if item[i] == item[j]:
                    item[j] = 0
                    print(j)
        print("_____________")
