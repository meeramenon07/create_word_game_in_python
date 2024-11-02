import random
name = input("your name? : ")
print("Hey", name, " Welcome to word guesding game!")
words = ["cat", "dog", "elephant", "bull", "rat", "mouse", "snake", "rabbit", "cow", "horse"]
word = random.choice(words)
print("guess the characters in the word")
guesses = ""
attempts = 10
while attempts > 0:
  wrong = 0
  for char in word:
    if char in guesses:
      print(char, end="")
    else:
      print("_")
      wrong += 1
  if wrong == 0:
    print("You won!")
    print("The word is", word)
    break
  print()
  guess = input("guess a character in the word: ")
  guesses += guess
  if guess not in word:
    attempts -= 1
    print("wrong")
    print("You have", attempts, "more guesses" )
    if attempts == 0:
      print("You lose!")



