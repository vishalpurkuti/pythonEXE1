
def isint(a):
    for i in range(len(a)):
        if a[i].isdigit() == True:
            return False
        else:
            return True


if(isint(input("Enter anything:"))):
    print("String")
else:
    print("integer")
