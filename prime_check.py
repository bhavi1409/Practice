num = int(input("Enter a number : "))
i = num-1
divisor = 0
while (i > 1) :
    if(num%i == 0):
        divisor = divisor + 1
    i = i-1

if(divisor == 0):
    print('Prime')
else:
    print('Not Prime')
