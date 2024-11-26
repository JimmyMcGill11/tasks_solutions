import random

def scramble_word(word):
  word_list = list(word)
  random.shuffle(word_list)
  return ''.join(word_list)

def word_scramble_game():
  words = ["dog", "cow", "cat", "horse", "donkey", "tiger", "lion", "Panther"]
  
  original_word = random.choice(words)
  
  scrambled_word = scramble_word(original_word)
  
  print("Welcome to the Word Scramble Game!")
  print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
  print("You have 5 attempts.")
  
  attempts = 5
  
  while attempts > 0:
    guess = input("Enter your guess: ").strip()
    
    if not guess:
      print("Invalid input! Please enter a valid word.")
      continue
    
    if guess.lower() == original_word:
      print("Congratulations! You guessed the correct word!")
      return
    
    attempts -= 1
    if attempts > 0:
      print(f"Incorrect! Try again. You have {attempts} attempts left.")
    else:
      print(f"You're out of attempts! The correct word was: {original_word}")
      return


word_scramble_game()
