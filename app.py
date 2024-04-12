winning_combinations = {
  "rock": "scissors",
  "scissors": "paper",
  "paper": "rock",
}
def random_choice():
  import random
  return random.choice(list(winning_combinations.keys()))

def get_winner(name, player, computer):
  if player == computer:
      return "It's a tie!"
  if winning_combinations[player] == computer:
      return f"{name} wins!"
  return "Computer wins!"

def validate_input(player_input):
  if player_input not in winning_combinations.keys():
    return False
  return True

def validate_player(player_name):
  if player_name == "" or player_name.isspace() or player_name.isdigit():
    return False
  return True

def get_player_name():
  player_name = input("Enter your name: ")
  if not validate_player(player_name):
    print("Invalid name. Try again.")
    return get_player_name()
  return player_name

def get_player_input():
  player_input = input("Enter your choice: ")
  if not validate_input(player_input):
    print("Invalid choice. Try again.")
    return get_player_input()
  return player_input

def play_game():
  computer_input = random_choice()
  player_name = get_player_name()
  player_input = get_player_input()
  return get_winner(player_name, player_input, computer_input)

print(play_game())

# # Path: test_app.py 
# import pytest
# from app import get_winner