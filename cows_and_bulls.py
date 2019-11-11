import random
from random import randint
num = randint(1000,9999)
c = 0
guess_count = 0
while(c != 1):
    guess = input('Guess a 4-digit num : ')
    guess_count = guess_count + 1
    cow_count = 0
    bull_count = 0
    list_rand = [i for i in str(num)]
    list_guess = [i for i in guess]
    print(list_guess)
    if(list_rand == list_guess):
        print("4 cows!! That's awesome")
        print("You guessed it in %d guesses"%guess_count)
        break
    for a in range(0,4):
        if(list_guess[a] == list_rand[a]):
            cow_count = cow_count + 1
            continue
        else:
            for b in range(0,4):
                if(a == b and list_guess[a] == list_rand[b]):
                    cow_count = cow_count + 1
                    break
                elif(list_guess[a] == list_rand[b] and a != b):
                    bull_count = bull_count + 1
                    break
            
    print('Cows : %d, Bulls : %d'%(cow_count,bull_count))
                


