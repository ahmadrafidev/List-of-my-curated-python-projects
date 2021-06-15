import random 
from hangman_art import stages, logo
from hangman_words import word_list


print(logo)
lives = len(stages) - 1
gameFinished = False

chosen = random.choice(word_list)
wordLength = len(chosen)

display = []
for _ in range(wordLength):
    display += "_"

while not gameFinished:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(wordLength):
        letter = chosen[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            gameFinished = True
            print("You lose.")
    
    if not "_" in display:
        gameFinished = True
        print("You win.")

    print(stages[lives])

