# display art
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """ format the account data """
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """ use if statement to check the guess """
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return  guess == 'b'


def clear():  # Prints 50 blank lines
    print("\n" * 50)


# display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# make the game repeatable
while game_should_continue:


    # generate a random account from the game data
    # making account at position be become the next account at position a

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    # check if user is correct
    ## get the follower count
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clear the screen
    clear()
    print(logo)
    # give user a feedback
    # score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, That's wrong. Final score: {score}.")








