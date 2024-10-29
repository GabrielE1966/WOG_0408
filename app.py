from guess_game import play as play_guess
from currency_roulette_game import  play as play_currency_roulette
def welcome():
    username = input('Please, enter your name: ')
    print(f'Hi {username}, and welcome to the World of Games: The Epic Journey')


MAX_GAME_NUMBER = 3
MAX_DIFFICULTY_LEVEL = 5
gameInfo = {
  1: "Memory Game",
  2: "Guess game",
  3: "Currency Roulette"
}


def start_play():
    user_choice = 0
    wrong_input = True
    print('Please, choose a game to play')
    while wrong_input:
        print('''
        1. Memory game - a sequence of numbers will appear for 1 second and you have to guess it back'
        2. Guess Game - guess a number and see if you chose like the computer.'
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS'
        ''')
        choice_str = input('your choice:')
        try:
            user_choice = int(choice_str)
        except ValueError:
            print('ERROR: The valUe you entered is not an  integer number')
            user_choice = 0

        if user_choice > MAX_GAME_NUMBER or user_choice < 1:
            print('please, enter number from 1 to 3')
        else:
            wrong_input = False

    print(f'You chose Game Number: {gameInfo[user_choice]}')
    wrong_input = True
    while wrong_input:
        diff_level_str = input('Please, Enter difficulty level (1-5): ')
        try:
            diff_level = int(diff_level_str)
        except ValueError:
            print('ERROR: The valUe you entered is not an  integer number')

        if diff_level > MAX_DIFFICULTY_LEVEL or diff_level < 1:
            print('Wrong Input!')
        else:
            wrong_input = False

# play the selected game
    if user_choice == 1:
        pass
    elif user_choice == 2:
        play_currency_roulette(diff_level)
    elif user_choice == 3:
        play_guess(diff_level)