def main():
    name = input('Enter your name: ')
    health = 100
    while health > 0:
        choice = input('Do you go left or right? ')
        if choice == 'left':
            print('You encounter a friendly dragon!')
        else:
            print('You fall into a trap!')
            health -= 50
        print(f'{name} has {health} health points.')
    print('Game over!')

main()
