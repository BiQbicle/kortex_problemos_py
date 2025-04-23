import random

def choose_word():
    words = ['apple', 'quandaledingle', 'skibidi', 'cat', 'orange', 'niggir', 'nigga', 'skullcrusher',]
    return random.choice(words)

def display_word(word, guesses):
    displayed = ''
    for letter in word:
        if letter in guesses:
            displayed += letter
        else:
            displayed += '_'
    return displayed

def check_guess(word, guess, guesses):
    if guess in word:
        guesses.append(guess)
        return True
    else:
        return False

def play_game():
    word = choose_word()
    guesses = []
    wrong_guesses = 0
    max_attempts = 6

    while True:
        print('Word:', display_word(word, guesses))
        guess = input('Guess a letter: ')
        if guess in guesses:
            print('You already guessed it retard')
            continue
        if check_guess(word, guess, guesses):
            print('Correct!')
        else:
            wrong_guesses += 1
            print('LMAO, THAT WAS WRONG! XD Attempts left:', max_attempts - wrong_guesses)
        if all(letter in guesses for letter in word):
            print('You actually won, wow! The word was:', word)
            break
        if wrong_guesses >= max_attempts:
            print('L + RATIO LMAO LOSER! The word was:', word)
            break

play_game()
