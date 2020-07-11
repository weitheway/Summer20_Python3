from random import randint
def dice_roll(s):
    x = randint(1,s)
    print(x)
    
    while True:
        ans = input('Do you want to roll again? Y/N: ')
    
        if ans == 'Y':
            x = randint(1,s)
            print(x)
        else: 
            print('Good Bye')
            exit ()
            
#any number sided dice
dice_roll(4)