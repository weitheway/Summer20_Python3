#Auto-generate a spot to order takeout from 

from random import randint
places = [
    "Lo Fatt Chow","Asia", 
    "Qdoba","Rice Shop", "Sri Thai", 
    "Napoli's","Gio's","Honeygrow",
    ]

while True:
    print('''
    What would you like to do?
    1. Pick a place for me.
    2. Let me narrow down to what type of food I want.
    3. Show me complete list of options I have
    4. Quit
    ''')
    ans = input("Please select a number: ")

    if ans == "1":
        #generate a place
        print(places[randint(0,len(places)-1)])
    elif ans == "2":
        #print list of type options1
        #prompt for input type 
        #then generate 
        print("Here are the currently available types")
    elif ans == "3":
        #print entire list of options
        #ask if want to edit list 
        #append/remove as needed 
        print("Here's the full list")
    elif ans == "4":
        print("Good-bye")
        break
    else: 
        print("Invalid input. Please select again")
