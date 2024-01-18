# # choosing a random number between 1 and 100
# import random
#
#
# # make a function to set difficulty
# def set_difficulty():
#     chosen_difficulty = input("Choose a difficulty, type 'easy' or 'difficult'")
#     if chosen_difficulty == 'easy':
#         return 10
#     elif chosen_difficulty == 'difficult':
#         return 5
#
#
# # let the user guess a number
# def guess_number():
#     guess = int(input("Please enter your guess: "))
#     return guess
#
#
# # function to check user's guess against actual answer
# def check_guess(target, guess):
#     if target > guess:
#         print("Too low")
#         return False
#     elif target < guess:
#         print("Too high")
#         return False
#     else:
#         print("You got it!")
#         return True
#
#
# def greet_user():
#     print("Welcome the number guessing game!!! Good Luck")
#


#
# def play_game():
#     target_number = random.choice(range(1, 101))
#     greet_user()
#     number_of_guess = set_difficulty()
#     should_continue = True
#     while should_continue is True:
#         user_guess = guess_number()
#         if check_guess(target_number, user_guess) == False:
#             number_of_guess -= 1
#         else:
#             should_continue = False
#
#         if number_of_guess == 0:
#             print("You lost the game!")
#             should_continue = False
#
# play_game()



import random
from art import logo

def set_difficulty():
    while True:
        chosen_difficulty = input("Choose a difficulty, type 'easy' or 'difficult': ").lower()
        if chosen_difficulty == 'easy':
            return 10
        elif chosen_difficulty == 'difficult':
            return 5
        else:
            print("Invalid input. Please type 'easy' or 'difficult'.")

def guess_number():
    while True:
        try:
            guess = int(input("Please enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Out of bounds. Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_guess(target, guess):
    if target > guess:
        print("Too low.")
        return False
    elif target < guess:
        print("Too high.")
        return False
    else:
        print("You got it! The number was", target)
        return True

def play_game():
    target_number = random.randint(1, 100)
    print(logo)
    print("Welcome to the Number Guessing Game! Good luck!")
    attempts = set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        user_guess = guess_number()

        if check_guess(target_number, user_guess):
            break

        attempts -= 1
        if attempts == 0:
            print(f"You've run out of attempts. The number was {target_number}. Better luck next time!")

def main():
    play_again = "yes"
    while play_again.lower() == "yes":
        play_game()
        play_again = input("Would you like to play again? (yes/no): ")
    print("Thank you for playing. Goodbye!")

if __name__ == "__main__":
    main()

