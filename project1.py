#--------------------------------------------------------------------------|
#         |    In this game which is played by 2 players anyone of them    |
#         |  can determine whether he wants to determine the pile of coins |
# Purpose |  on which he wants to play, or allow the computer to do so.    |
#         |     the players must exchange roles in playing and each of them|
#         | must ensure that the number is non-zero square and each time   |
#         | this input will be subtracted until one of them win at the game|    
#--------------------------------------------------------------------------|               
#  Author |                 Walid Adel Mord                                |
#--------------------------------------------------------------------------|
import random
#take users`names 
player1=input('Player (1) Please, Enter your name: ').title()
player2=input('Player (2) Please, Enter your name: ').title()

#Take the pile of coins from the user .
choice=input('''\ndo you want to insert the pile of coins or you want the coputer do this
Enter (a) to insert a number or (b) to let the computer do this: ''').lower()
chars=['a','b']
while choice not in chars:
    print('Invalid Input!')
    choice=input('''\ndo you want to insert the pile of coins or you want the coputer do this
Enter (a) to insert a number or (b) to let the computer do this: ''').lower()
if choice=='a':
    while True:
        try:
            pile_coin=int(input('\nPlease, Enter the pile of coins that you want to play on it: '))
            break
        except ValueError:
            print('\nInvalid input! Please, Follow the instructions.')
    while pile_coin<=0:
        print('The pile of coins has to be greater than zero.')
        while True:
            try:
                pile_coin=int(input(f'\n{player1} insert your number: '))
                break
            except ValueError:
                print('''\nInvalid Input! Please, Follow the instructions.''')
# make the computer choose a random number and check if it is not square or not
elif choice=='b':
    pile_coin=random.randint(10,1000)
    num=pile_coin**0.5
    while num==int(num):
        pile_coin=random.randint(10,1000)
        num=pile_coin**0.5
    print(f'\nthe pile of coins is {pile_coin}')

# start the game
while True:
#let user (1) to play and then check the validety of the input 
    while True:
        try:
            play1=int(input(f'\n{player1} insert your number: '))
            break
        except ValueError:
            print('''\nInvalid Input! Please, Follow the instructions.''')
# check if the input a non-zero square number
    while  play1 <=0 :
        print(f'{player1} your number has to be greater than zero.')
        while True:
            try:
                play1=int(input(f'\n{player1} insert your number: '))
                break
            except ValueError:
                print('''\nInvalid Input! Please, Follow the instructions.''')
#the root of the number to check if it is square number or not
    num1=play1**0.5
    while play1>pile_coin or num1!=int(num1) :
        print(f'\n{player1} your number has to be less than or equal and a non-zero square number.')
        while True:
            try:
                play1=int(input(f'\n{player1} insert your number: '))
                break
            except ValueError:
                print('''\nInvalid Input! Please, Follow the instructions.''')
#check if the input is greater than zero 
        while  play1 <=0 :
            print(f'{player1} your number has to be greater than zero.')
            while True:
                try:
                    play1=int(input(f'\n{player1} insert your number: '))
                    break
                except ValueError:
                    print('''\nInvalid Input! Please, Follow the instructions.''')
        num1=play1**0.5
#the new pile of coins
    pile_coin-=play1
    print(f'\n{pile_coin} remaining')
    if pile_coin==0:
        print(f'\nCongratulation {player1}! you are winner. ')
        break
# let user (2) to play and then check the validety of the input  
    while True:
        try:
            play2=int(input(f'\n{player2} insert your number: '))
            break
        except ValueError:
            print('''\nInvalid Input! Please, Follow the instructions.''')
#check if the input is greater than zero
    while  play2 <=0 :
        print(f'{player2} your number has to be greater than zero.')
        while True:
            try:
                play2=int(input(f'\n{player2} insert your number: '))
                break
            except ValueError:
                print('''\nInvalid Input! Please, Follow the instructions.''')
#the root of the number.
    num2=play2**0.5
# check if the input is a non-zero square number
    while play2>pile_coin or num2!=int(num2) :
        print(f'\n{player2} your number has to be less than or equal and a non-zero square number.')
#handling the errors
        while True:
            try:
                play2=int(input(f'\n{player2} insert your number: '))
                break
            except ValueError:
                print('''\nInvalid Input! Please, Follow the instructions.''')
        while  play2 <=0 :
            print(f'{player2} your number has to be greater than zero.')
            while True:
                try:
                    play2=int(input(f'\n{player2} insert your number: '))
                    break
                except ValueError:
                    print('''\nInvalid Input! Please, Follow the instructions.''')
# the root of the input
        num2=play2**0.5
# create a new pile of coins    
    pile_coin-=play2
    print(f'{pile_coin} remainig.')
    if pile_coin==0:
        print(f'\ncongratulation {player2}! you are winner. ')
        break





