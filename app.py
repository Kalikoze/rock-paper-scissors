winning_combinations = {
  "rock": "scissors",
  "scissors": "paper",
  "paper": "rock",
}

scores = {
  "player": 0,
  "computer": 0,
}

def random_choice():
  import random
  return random.choice(list(winning_combinations.keys()))

def get_winner(name, player, computer):
  if player == computer:
    return "It's a tie!"
  if winning_combinations[player] == computer:
    scores["player"] += 1
    return f"{name} wins! The score is {scores['player']} - {scores['computer']}"
  scores["computer"] += 1
  return f"Computer wins!  The score is {scores['player']} - {scores['computer']}"

def invalid_input(input, type="choice"):
  if type == "name":
    return input == "" or input.isspace() or input.isdigit()
  return input not in winning_combinations.keys()

def get_input(type):
  data = input(f"Enter your {type}: ")
  if invalid_input(data, type):
    print("Invalid input. Try again.")
    return get_input(type)
  return data

def start_game():
  print("Welcome to Rock, Paper, Scissors!")
  print("You will be playing against the computer.")
  print("Feel free to play for as many rounds as you'd like.")
  print("Good luck!")
  player_name = get_input("name")
  play_game(player_name)


def play_game(player_name):
  computer_input = random_choice()
  player_input = get_input("choice").lower()
  print(get_winner(player_name, player_input, computer_input))
  print(determineNextGame(player_name))

def determineNextGame(player_name):
  play_again = input(f"Do you want to play again {player_name}? (Y/N): ")
  if play_again.upper() == "Y":
    return play_game(player_name)
  if play_again.upper() == "N":
    return "Thanks for playing!"
  print("Invalid input. Try again.")
  determineNextGame(player_name)

start_game()

