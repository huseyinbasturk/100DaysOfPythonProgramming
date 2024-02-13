from replit import clear
import random
from hangman_words import word_list
import hangman_art

chosen_word = random.choice(word_list)

lives = 6
print(hangman_art.logo)

display =[]
length = len(chosen_word)
for _ in range(length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(0, length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word, you lose a life")
        lives -= 1

    if lives == 0:
        end_of_game = True
        print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(hangman_art.stages[lives])
