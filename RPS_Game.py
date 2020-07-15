#Rock Paper Scissors

from random import randint

options = ['Rock', 'Paper', 'Scissor']

while True:
    computer = options[randint(0,2)]
    player = input("Rock, Paper, or Scissors?")
    if player == computer:
        print("It's a tie!")
    elif player == 'Rock' & computer == 'Scissor':
        print("You win")
    elif player == "Paper" & computer == "Rock":
        print("You win")
    elif player == "Scissor" & computer == "Paper":
        print("You win")
    else:
        print("Game over")

