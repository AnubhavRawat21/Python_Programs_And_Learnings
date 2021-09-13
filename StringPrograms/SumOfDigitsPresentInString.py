# Program which take some string as input, that string should have some digits in it.
# Means Input String should be Alphanumeric String like 'Hello123545'
# Input - Accept Alphanumeric String as Input from User
# Output - Print Sum of all the digits present in string
# Example - Input - str1='Hello123545'
# Output - Sum of digits present in String is - 25

def sumOfDigitsInStr(string):
    sum=0
    for digit in string:
        if digit in ("0123456789"):
            sum+=int(digit)
    return sum

string=input("Enter any string:- ")
print("Sum of digits in",string,"is",sumOfDigitsInStr(string))
print("BYE")
