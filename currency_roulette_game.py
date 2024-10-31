from currency_converter import CurrencyConverter
import random
MAX_DOLLARS = 100


def generate_dollar_val():
    dollar_value = random.randint(1, MAX_DOLLARS)
    return dollar_value


def get_money_interval(usd_value, difficulty):
    c = CurrencyConverter()
    nis_value = c.convert(usd_value, 'USD', 'ILS')
    interval_len = 10 - difficulty
    min_interval = nis_value - interval_len
    max_interval = nis_value + interval_len
    interval = [min_interval, max_interval]
    print(f'currency rate usd to nis:{nis_value:.2f}, min: {interval[0]:.2f}, max: {interval[1]:.2f}')
    return interval


def get_guess_from_user(usd_value):
    usr_guess = -1
    while usr_guess < 0:
        guess_str = input(f'What is your guess for {usd_value:} USD in N.I.S ? ')
        try:
            usr_guess = int(guess_str)
            if usr_guess < 0:
                print('Please, Enter a positive number')
        except ValueError:
            print('Please enter an integer  value')
    return usr_guess


def compare_result(usd_value, difficulty):
    usr_guess = get_guess_from_user(usd_value)
    interval = get_money_interval(usd_value, difficulty)

    if interval[0] <= usr_guess <= interval[1]:
        return True
    else:
        return False


def play(difficulty):
    print('Welcome to the currency roulette game!')
    dollar_value = generate_dollar_val()
    result = compare_result(dollar_value, difficulty)
    return result


