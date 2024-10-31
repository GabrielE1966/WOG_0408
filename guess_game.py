import random

def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    guess_no = -1
    while guess_no < 0:
        guess_str = input(f"Please, enter your guess number 0-{difficulty}: ")
        try:
            guess_no = int(guess_str)
            if guess_no < 0 or guess_no > difficulty:
                print(f'Please, enter a number between 0 to {difficulty}')
                guess_no = -1
        except ValueError:
            print('Error, not a  valid integer number')
            guess_no = -1
    return guess_no


def compare_result(user_guess, secret_no):
    win_value = user_guess == secret_no
    return win_value

# play the guessing game. get a choice from the  user, generate randon number and compare the two!
def play(difficulty):
    assert difficulty > 0
    print('the Guessing game!')

    secret_number = generate_number(difficulty)

    user_choice = get_guess_from_user(difficulty)

    result = compare_result(user_choice, secret_number)
    print(f'The secret number was: {secret_number}')
    return result

