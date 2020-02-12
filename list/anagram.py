def anagram(a, b):

    if sorted(a) == sorted(b):
        return True

    else:
        return False


if anagram(input("Enter str 1:"), input("Enter str2:")) == True:
    print("anagram")
else:
    print("Not anagram")
