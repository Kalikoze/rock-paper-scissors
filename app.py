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

def play_game():
  computer_input = random_choice()
  player_name = get_input("name")
  player_input = get_input("choice")
  return get_winner(player_name, player_input, computer_input)

print(play_game())