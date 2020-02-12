def calledremove_duplicate(num):
    rum = []
    for i in num:
        if i not in rum:
            rum.append(i)
    print(rum)


num = [11, 1, 1, 7, 6, 6, 1, 11, 1]
calledremove_duplicate(num)
