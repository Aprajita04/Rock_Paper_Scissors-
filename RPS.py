
import random

print('Welcome to the RPS game\n')
print('-----Winning rules-----')
print('Rock vs Paper = Paper wins \n' +
      'Rock vs Scissor = Rock wins \n' +
      'Paper vs Scissor = Scissor wins')
print('----------------------------------\n')

# counter value
i = 1
you = 0
com = 0
draw = 0

# continue the game if user wants
while True:    # random generated value for computer rurn
    com_choice = random.randint(1, 3)  # random number between 1 to 3
    your_choice = int(input('Enter 1 for rock, 2 for paper and 3 for scissor: \n'))

    # user input range validation
    while your_choice not in [1, 2, 3]:
        print('\ninvalid input!')
        your_choice = int(input('Enter 1 for rock, 2 for paper and 3 for scissor: \n'))

    # mapping between input and game value
    gm_dist = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSOR'}
    winner = ''

    print('\nYou selected: ' + gm_dist[your_choice])
    print('Computer selected: ' + gm_dist[com_choice])

    # condition for entire game
    if com_choice == your_choice:
        print('Game is DRAW')
        winner = 'NON'
    elif com_choice == 1:
        if your_choice == 2:
            winner = 'YOU'
        else:
            winner = 'COMPUTER'
    elif com_choice == 2:
        if your_choice == 1:
            winner = 'COMPUTER'
        else:
            winner = 'YOU'
    elif com_choice == 3:
        if your_choice == 1:
            winner = 'YOU'
        else:
            winner = 'COMPUTER'
    else:
        print('Something went wrong')

    # announcement of the winner
    if winner != '' and winner != 'NON':
        print('THE WINNER IS ' + winner)

    # counter value for whole game
    if winner == 'YOU':
        you += 1
    elif winner == 'COMPUTER':
        com += 1
    elif winner == 'NON':
        draw += 1

    # next round?
    again = input('\nDo you want to play again? Y/N: ')
    if again.upper() == 'N':
        print('thanks for playing')
        print('\n-----game summary-----')
        print('Total game: ' + str(i) + ' rounds')
        print('Computer won: ' + str(com) + ' times')
        print('You won: ' + str(you) + ' times')
        print('Draw: ' + str(draw) + ' times')
        break
    else:
        i += 1
        print('\n' + str(i) + 'nd round started!')


