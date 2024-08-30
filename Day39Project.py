import random

words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
word = random.choice(words)

guessed = set()
lives = 6

while lives > 0:
    print(' '.join([letter if letter in guessed else '_' for letter in word]))
    guess = input('Guess a letter: ').lower()
    if guess in guessed:
        print('You already guessed that!')
    elif guess in word:
        guessed.add(guess)
        if len(guessed) == len(set(word)):
            print('Congratulations, you guessed the word!')
            break
    else:
        lives -= 1
        print('That letter is not in the word. You have', lives, 'lives left.')

if lives == 0:
    print('Game over! The word was', word)