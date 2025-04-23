import os
import time
from git import Repo

# Initialize the Repo object for the current directory
repo = Repo(os.getcwd())

# Define the game file path
game_file = os.path.join(repo.working_tree_dir, "game.py")

# Define the content for each commit
commits = [
    ("Initial commit: Create game.py with a simple print statement",
     "print('Welcome to the Adventure Game!')\n"),
    ("Add main function",
     "def main():\n    print('Starting the game...')\n\nmain()\n"),
    ("Add player input for name",
     "def main():\n    name = input('Enter your name: ')\n    print(f'Welcome, {name}!')\n\nmain()\n"),
    ("Add simple decision point",
     "def main():\n    name = input('Enter your name: ')\n    choice = input('Do you go left or right? ')\n    print(f'{name} chose to go {choice}.')\n\nmain()\n"),
    ("Add outcome for left choice",
     "def main():\n    name = input('Enter your name: ')\n    choice = input('Do you go left or right? ')\n    if choice == 'left':\n        print('You encounter a friendly dragon!')\n    else:\n        print('You fall into a trap!')\n\nmain()\n"),
    ("Add health points",
     "def main():\n    name = input('Enter your name: ')\n    health = 100\n    choice = input('Do you go left or right? ')\n    if choice == 'left':\n        print('You encounter a friendly dragon!')\n    else:\n        print('You fall into a trap!')\n        health -= 50\n    print(f'{name} has {health} health points.')\n\nmain()\n"),
    ("Add loop for multiple decisions",
     "def main():\n    name = input('Enter your name: ')\n    health = 100\n    while health > 0:\n        choice = input('Do you go left or right? ')\n        if choice == 'left':\n            print('You encounter a friendly dragon!')\n        else:\n            print('You fall into a trap!')\n            health -= 50\n        print(f'{name} has {health} health points.')\n    print('Game over!')\n\nmain()\n"),
    ("Add win condition",
     "def main():\n    name = input('Enter your name: ')\n    health = 100\n    treasure_found = False\n    while health > 0 and not treasure_found:\n        choice = input('Do you go left or right? ')\n        if choice == 'left':\n            print('You find a treasure chest!')\n            treasure_found = True\n        else:\n            print('You fall into a trap!')\n            health -= 50\n        print(f'{name} has {health} health points.')\n    if treasure_found:\n        print('Congratulations, you win!')\n    else:\n        print('Game over!')\n\nmain()\n"),
    ("Refactor code into functions",
     "def get_player_name():\n    return input('Enter your name: ')\n\ndef make_choice():\n    return input('Do you go left or right? ')\n\ndef main():\n    name = get_player_name()\n    health = 100\n    treasure_found = False\n    while health > 0 and not treasure_found:\n        choice = make_choice()\n        if choice == 'left':\n            print('You find a treasure chest!')\n            treasure_found = True\n        else:\n            print('You fall into a trap!')\n            health -= 50\n        print(f'{name} has {health} health points.')\n    if treasure_found:\n        print('Congratulations, you win!')\n    else:\n        print('Game over!')\n\nmain()\n"),
    ("Add comments and improve readability",
     "# Adventure Game\n\ndef get_player_name():\n    # Get the player's name\n    return input('Enter your name: ')\n\ndef make_choice():\n    # Get the player's choice\n    return input('Do you go left or right? ')\n\ndef main():\n    name = get_player_name()\n    health = 100\n    treasure_found = False\n    while health > 0 and not treasure_found:\n        choice = make_choice()\n        if choice == 'left':\n            print('You find a treasure chest!')\n            treasure_found = True\n        else:\n            print('You fall into a trap!')\n            health -= 50\n        print(f'{name} has {health} health points.')\n    if treasure_found:\n        print('Congratulations, you win!')\n    else:\n        print('Game over!')\n\nif __name__ == '__main__':\n    main()\n"),
]

# Function to write content and commit
def write_and_commit(message, content):
    with open(game_file, "w") as f:
        f.write(content)
    repo.index.add([game_file])
    repo.index.commit(message)
    print(f"Committed: {message}")

# Iterate over the commits
for msg, code in commits:
    write_and_commit(msg, code)
    time.sleep(1)  # Optional: pause between commits
