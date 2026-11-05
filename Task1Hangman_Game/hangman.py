import random
words=list()
  
with open("englishwordlist.txt","r") as file:
  for i in file:
    i=i.strip()
    words.append(i)
    
if not words:
  print("Word is empty!")
  exit()

word=random.choice(words).lower()

guessed_letters=set()
wrong_guesses=set()
max_attemps=6
remaining_attempts=6

hangman_stages=[
  """
      +---+
      |   |
          |
          |
          |
      =========
    """,
  """
      +---+
      |   |
      O   |
          |
          |
      =========
  """,
  r"""
    +---+
    |   |
    O   |
    |   |
        |
    ========= """,
  r""" 
      +---+
      |   |
      O   |
     /|   |
          |
    ========= """,
  r"""
    +---+
    |   |
    O   |
   /|\  |
        |
  ========= """,
  r""" 
    +---+
    |   |
    O   |
   /|\  |
   /    |
  ========= """,
  r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
=========
"""
]

while remaining_attempts > 0:
  print(hangman_stages[len(wrong_guesses)])
    
  display_word=""
  for letter in word:
    if letter in guessed_letters:
      display_word += letter
      
    else:
      display_word += "_"
    
  print("Word:"," ".join(display_word))
  
  print("Remaining attempts:",remaining_attempts)
  
      
  guess=input("Enter guess letter: ").lower()
    
  if not guess.isalpha() or len(guess) !=1:
    print("Invalid input")
  elif guess in guessed_letters or guess in wrong_guesses:
    print("Already guessed letter")
    
  elif guess in word:
    guessed_letters.add(guess)
    
  else:
    wrong_guesses.add(guess)
    remaining_attempts -=1
    
  print("Correct guesses:", sorted(guessed_letters))
  print("Wrong guesses:",sorted(wrong_guesses))
    
  
  if all(letter in guessed_letters for letter in word):
    print("You won the game")
    print("The word was:",word)
    break
    
if(remaining_attempts == 0):
    print(hangman_stages[6])
    print("Game Over!! You lost")
    print("The correct word was:",word)
    
  
    
      
