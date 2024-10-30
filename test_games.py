from guess_game import play as play_guess
from currency_roulette_game import play as play_currency_roulette
from memory_game import play as play_memory


def test_guess():
    guess_result = play_guess(7)
    if guess_result:
        print('you win!')
    else:
        print('you loose!')

    guess_result = play_guess(1)
    if guess_result:
        print('you win!')
    else:
        print('you loose!')


    guess_result = play_guess(4)
    if guess_result:
        print('you win!')
    else:
        print('you loose!')


def test_currency():
    result = play_currency_roulette(3)
    if result:
        print('you win!')
    else:
        print('you loose!')

    result = play_currency_roulette(5)
    if result:
        print('you win!')
    else:
        print('you loose!')

def test_memory():
    result = play_memory(3)
    if result:
        print('you win!')
    else:
        print('you loose!')

    input('Please press enter to conintue')

    result = play_memory(5)
    if result:
        print('you win!')
    else:
        print('you loose!')

# test_guess()
# test_currency()
test_memory()
