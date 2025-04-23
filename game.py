# Adventure Game

def get_player_name():
    # Get the player's name
    return input('Enter your name: ')

def make_choice():
    # Get the player's choice
    return input('Do you go left or right? ')

def main():
    name = get_player_name()
    health = 100
    treasure_found = False
    while health > 0 and not treasure_found:
        choice = make_choice()
        if choice == 'left':
            print('You find a treasure chest!')
            treasure_found = True
        else:
            print('You fall into a trap!')
            health -= 50
        print(f'{name} has {health} health points.')
    if treasure_found:
        print('Congratulations, you win!')
    else:
        print('Game over!')

if __name__ == '__main__':
    main()
