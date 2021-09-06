
num=int(input('Enter number-'))
flag=0
if num<=1:
    print("please enter number greater than 1")
else:    
    #for (i=2;i<num;i++):
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    if flag==0:
        print("It is a prime number")
    else:
        print("It is not a prime number")



 