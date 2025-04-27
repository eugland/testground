board = [' ']*9


def print_board():
    rows = [board[i:i+3] for i in range(0, 9, 3)]
    for r in rows:
        print('|'.join(r))
        print('-'*5)

current = 'X'
while True:
    print_board()
    move = int(input(f'{current} choose 1-9: ')) - 1
    if board[move] == ' ':
        board[move] = current
        current = 'O' if current == 'X' else 'X'
    else:
        print('Spot taken!')
