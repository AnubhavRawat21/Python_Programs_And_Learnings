# Write a Program to replace all the occurence of Vowels in a String with '*'
# Input - Accept String as Input from User
# Output - String with '*' in place of vowels
# Example - Input - 'Hello'
# Output - 'H*ll*'

def newCharString(inputString):
    newString=""
    for char in inputString :
        #if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u":
        if char in "aeiouAEIOU":
            newString+= "*"
        else:
            newString+=char
    return newString

string=input("Enter any string :- ")
print ("New String is ",newCharString(string))
print("BYE")
