# Program to check if a string is Palindrome or not
# What is Palindrome - If string reads same from backwards and forwards Example - Dad, Kanak
# Input - Accept String as Input from User
# Output - Print if it is Palindrome or not
# Example - Input - str1='kanak'
# Output - kanak is Palindrome String

def isPalindrome(str1):
        startIndex=0
        endIndex=len(str1) -1
        while startIndex<endIndex:
            if str1[startIndex]==str1[endIndex]:
                startIndex+=1
                endIndex-=1
            else:
                return False
        return True

inputStr=input("Enter any string - ")
if(isPalindrome(inputStr) == True):
    print(inputStr,"is a Palindrome")
else:
    print(inputStr,"is a not Palindrome")


