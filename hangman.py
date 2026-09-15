import random

def play_hangman():
    # 1. List of 5 predefined words
    words = ["python", "developer", "codealpha", "hangman", "program"]
    
    # Randomly select a word
    secret_word = random.choice(words)
    
    # Tracking variables
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("========================================")
    print("      WELCOME TO HANGMAN GAME           ")
    print("========================================")
    print(f"Try to guess the word! You have {max_incorrect} incorrect tries.\n")

    # Game loop
    while incorrect_guesses < max_incorrect:
        # Display current word progress (e.g., "p _ t h _ n")
        displayed_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        
        print(f"Word: {displayed_word.strip()}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Tries remaining: {max_incorrect - incorrect_guesses}")
        
        # Win Condition: All letters in secret_word have been guessed
        if "_" not in displayed_word:
            print("\n🎉 CONGRATULATIONS! You guessed the word correctly!")
            break
        
        # User input
        guess = input("\nGuess a letter: ").lower().strip()
        
        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single letter.\n")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try another letter.\n")
            continue
            
        # Add guess to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is correct or incorrect
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Sorry, '{guess}' is NOT in the word.\n")

    # Loss Condition
    if incorrect_guesses == max_incorrect:
        print("========================================")
        print(f"💀 GAME OVER! You've run out of guesses.")
        print(f"The secret word was: '{secret_word}'")
        print("========================================")

# Run the game
if __name__ == "__main__":
    play_hangman()