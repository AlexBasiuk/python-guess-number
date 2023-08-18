from random import randint
from art import logo
print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  level = input("Choose your difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
def game():  
  print("Welcme to guessing the NUmber Game!")
  print("I'm thinking about the number between 1 and 100.")
  answer = randint(1, 100)
  print(f"the answer is {answer}")
  
  turns = set_difficulty()
  
  
  game = True
  guess = 0 
  while guess != answer:
    guess = int(input("Make your guess: "))
    turns = check_answer(guess, answer, turns)
    print(f"You have {turns} attemts remaining to guess the number.")
    if turns == 0:
      print("Game over")
      return
    elif guess != answer:
      print("Guess again")
  
game()