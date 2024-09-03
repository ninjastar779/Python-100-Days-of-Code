import random

characters = {
    'Superman': {'Speed': 10, 'Agility': 8, 'Intelligence': 9, 'Strength': 7},
    'Batman': {'Speed': 7, 'Agility': 9, 'Intelligence': 10, 'Strength': 8},
    'Wonder Woman': {'Speed': 8, 'Agility': 10, 'Intelligence': 7, 'Strength': 9},
    'The Flash': {'Speed': 10, 'Agility': 8, 'Intelligence': 7, 'Strength': 9},
    'Green Lantern': {'Speed': 7, 'Agility': 9, 'Intelligence': 10, 'Strength': 8}
}

while True:
    print("Characters:")
    for i, character in enumerate(characters.keys(), start=1):
        print(f"{i}. {character}")
    player_choice = input("Pick a character: ")
    if player_choice not in characters:
        print("Invalid choice")
        continue
    print("Stats:")
    for i, stat in enumerate(characters[player_choice].keys(), start=1):
        print(f"{i}. {stat}")
    player_stat = input("Pick a stat: ")
    if player_stat not in characters[player_choice]:
        print("Invalid stat")
        continue
    computer_choice = random.choice(list(characters.keys()))
    computer_stat = random.choice(list(characters[computer_choice].keys()))
    print(f"Computer chose {computer_choice} and {computer_stat}")
    print(f"Player chose {player_choice} and {player_stat}")
    player_stat_value = characters[player_choice][player_stat]
    computer_stat_value = characters[computer_choice][computer_stat]
    print(f"Player's {player_stat}: {player_stat_value}")
    print(f"Computer's {computer_stat}: {computer_stat_value}")
    print("Result:")
    if player_stat_value == computer_stat_value:
        print("Tie!")
    if player_stat_value > computer_stat_value:
        print("Player wins!")
    else:
        print("Computer wins!")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != 'y':
        break