
import random
# List of words for the game
words = ['python', 'java', 'kotlin', 'javascript', 'flask', 'django', 'hangman', 'algorithm','programmer',]

def get_random_word(words_list):
    """Get a random word from the list."""
    return random.choice(words_list)

def display_word(word, guessed_letters):
    """Return the word with unguessed letters as underscores."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    """Main function to play the Hangman game."""
    print("Welcome to Hangman!")
    
    word = get_random_word(words)
    guessed_letters = set()
    attempts = 6  # You can adjust this number for difficulty
    print(f"\nThe word has {len(word)} letters. Good luck!")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word).issubset(guessed_letters):
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Incorrect guess! You have {attempts} attempts left.")

        if attempts == 0:
            print(f"\nGame over! The word was {word}")



play_hangman()
