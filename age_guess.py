a = 0
b = 100
for i in range(0,8):
    print(str(a))
    print(str(b))
    print("Is Your Age "+str(b)+"?")
    print("1. Less")
    print("2. More")
    print("3. Correct")
    choice = int(input("Your Choice :"))
    if(choice == 1):
        if((b-a)%2==0):
            b = a+(b-a)/2
        else:
            b = a+(b-a+1)/2
    elif(choice == 2):
        if((b-a)%2==0):
            a = b+(b-a)/2
            if(a>b):
                (a,b) = (b,a)
        else:
            a = b+(b-a+1)/2
            if(a>b):
                (a,b) = (b,a)
    elif(choice == 3):
        break
