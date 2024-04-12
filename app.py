winning_combinations = {
  "rock": "scissors",
  "scissors": "paper",
  "paper": "rock",
}

def get_winner(name, player, computer):
  if player == computer:
      return "It's a tie!"
  if winning_combinations[player] == computer:
      return f"{name} wins!"
  return "Computer wins!"

def random_choice():
  import random
  return random.choice(list(winning_combinations.keys()))

computer_input = random_choice()
player_name = input("Enter your name: ")
player_input = input("Enter your choice: ")
print(get_winner(player_name, player_input, computer_input))