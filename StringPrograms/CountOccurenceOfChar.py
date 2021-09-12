# Program to count the number of times a character occurs in a String
# Accept String as Input From User
# Accept Character to count as Input From User
# Print Occurence of that character as Output.

# Function Definition
def charOccurenceCount(stringParameter):
    count=0
    for index in range (0,len(stringParameter)):
        char=stringParameter[index]
        if(char==searchChar):
            count+=1
    return count

# Main
# Input From User
inputString=input('Enter String - ')
searchChar=input("Enter Char To Count - ")

# Method-1 : Char Count Without Function Call
print("Char Count Without Function Call -")
count=0
for index in range (0,len(inputString)):
	char=inputString[index]
	if(char==searchChar):
		count+=1
print("Char", searchChar,"occurs ",count," times in String - '",inputString,"'")
print("Bye")
print("")


# Method-2 : Char Count Without Function Call
print("Char Count Thru Function Call -")
countThruFunction=charOccurenceCount(inputString)
print("Char", searchChar,"occurs ",countThruFunction," times in String - '",inputString,"'")
print("Bye Again")
print("")
