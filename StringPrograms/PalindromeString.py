# Program to check if a string is Palindrome or not
# What is Palindrome - If string reads same from backwards and forwards Example - Dad, Kanak
# Input - Accept String as Input from User
# Output - Print if it is Palindrome or not
# Example - Input - str1='kanak'
# Output - kanak is Palindrome String

def reverseString(str1):
    reversedStr=''
    for index in range(-1,-len(str1)-1,-1):
        reversedStr+=str1[index]
    return reversedStr.lower()
   

inputStr=input("Enter any string - ")
if inputStr.lower()==reverseString(inputStr):
    print(inputStr,"is a Palindrome String")
else:
    print(inputStr,"is not a Palindrome String")

