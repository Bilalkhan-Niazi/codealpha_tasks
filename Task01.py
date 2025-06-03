import random

# List of words to choose from
word_list = ["python", "programming", "computer", "algorithm", "database", "network", "developer"]

def get_word():
    """Select a random word from the word list."""
    return random.choice(word_list).upper()

def display_hangman(tries):
    """Return the ASCII art for the hangman based on remaining tries."""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           --------
        """,  # 0 tries left
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           --------
        """,  # 1 try left
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           --------
        """,  # 2 tries left
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           --------
        """,  # 3 tries left
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           --------
        """,  # 4 tries left
        """
           --------
           |      |
           |      O
           |
           |
           |
           --------
        """,  # 5 tries left
        """
           --------
           |      |
           |
           |
           |
           |
           --------
        """   # 6 tries left
    ]
    return stages[tries]

def play_hangman():
    """Main function to play the Hangman game."""
    word = get_word()
    word_letters = set(word)  # Letters in the word
    guessed_letters = set()   # Letters guessed by the player
    tries = 6                 # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print(f"You have {tries} incorrect guesses allowed.")

    while tries > 0 and word_letters:
        # Display current state of the word
        print("\nWord:", " ".join(letter if letter in guessed_letters else "_" for letter in word))
        print(display_hangman(tries))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Get player input
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)
        if guess in word_letters:
            word_letters.remove(guess)
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess! {tries} tries left.")

    # Game outcome
    if not word_letters:
        print("\nWord:", word)
        print("Congratulations! You guessed the word!")
    else:
        print("\nWord was:", word)
        print(display_hangman(tries))
        print("Game Over! You ran out of tries.")

if __name__ == "__main__":
    play_hangman()
    while input("\nPlay again? (y/n): ").lower().startswith("y"):
        print("\n" * 50)  # Clear screen for new game
        play_hangman()