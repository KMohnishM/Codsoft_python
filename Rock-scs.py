import random

player1c = 0
player2c = 0
player1t=0
player2t=0
inputs = ['Rock', 'Paper', 'Scissor']

while True:
    print('Enter 1 for Rock \nEnter 2 for Paper \nEnter 3 for Scissor')
    player1 = input()

    if player1 not in ['1', '2', '3']:
        print("Invalid input. Please enter 1, 2, or 3.")
        continue

    player2 = random.choice(inputs)

    if player1 == '1':
        if player2 == 'Paper':
            player2c += 1
        elif player2 == 'Scissor':
            player1c += 1
    elif player1 == '2':
        if player2 == 'Rock':
            player1c += 1
        elif player2 == 'Scissor':
            player2c += 1
    else:
        if player2 == 'Paper':
            player1c += 1
        elif player2 == 'Rock':
            player2c += 1

    print("Player 1 input:", inputs[int(player1) - 1])
    print("Player 2 input:", player2)
    print("Player1 score: ", player1c)
    print("Player2 score: ", player2c)

    if player1c == 3 or player2c == 3:
        print('Do You Wanna Play Again\nIf YES press 1 Else press 2')
        userin = input()
        if userin == '1':
            player1c = 0
            player2c = 0
            if player1c== 3:
                player1t+=1
                print("No. of Rounds Won by Player1 :",player1t)
                print("No. of Rounds Won by Player2 :",player2t)
            else:
                player2t+=1
                print("No. of Rounds Won by Player1 :",player1t)
                print("No. of Rounds Won by Player2 :",player2t)    
        else:
            break
