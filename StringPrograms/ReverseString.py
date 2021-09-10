# Program to Reverse a String by creating a new String
# Input - Accept String as Input from User
# Output - Print Reversed String
# Example - Input - str1='Hello'
# Output - str2='olleH'

def reverseString(inputString):
    stringChar=""
    for index in range (-1,-len(inputString)-1,-1):
        stringChar1=inputString[index]
        stringChar+=stringChar1
    string2=stringChar    
    return string2


inputString=input('Enter String That Is To Be Reversed:-')
print('String In Reverse Order Using Function :-')
reversedString=reverseString(inputString)
print('Reverse of ',inputString,'is',reversedString)

