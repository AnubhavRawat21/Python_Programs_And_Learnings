# Program with a function with name deleteChar(), which takes two parameters - 
# One is String and other is a character
# The function should create a new string after deleting all the occurences of the character from the string
# And return a new String
# Input - Accept String as Input from User
# Output - String after deleting all the occurences of the character
# Example - Input - str1='Hello' and str2='o'
# Output - So after deleting 'o' it will be 'Hell'

def deleteChar(inputString, charToDel):
    newString=""
    for char in inputString:
        if(char != charToDel):
            newString+=char
    return newString

# Main
inputString=input("Enter Any String - ")
charToDel=input("Enter Char to Delete from string - ")
print("String after deleting char is ",deleteChar(inputString, charToDel))
print("Bye")


