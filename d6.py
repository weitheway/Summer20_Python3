from random import randrange
def d6():
    x = randrange(1,6,1)
    print(x)
    
    while True:
        ans = input('Do you want to roll again? Y/N: ')
    
        if ans == 'Y':
            x = randrange(1,6,1)
            print(x)
        else: 
            print('Good Bye')
            exit ()

d6()