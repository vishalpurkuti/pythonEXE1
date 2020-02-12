def isPalindrome(str):

    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


if(isPalindrome(input("Enter a string:"))):
    print("Palindrome")
else:
    print("Not a palindrome")
