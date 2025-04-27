board = [' ']*9


def print_board():
    rows = [board[i:i+3] for i in range(0, 9, 3)]
    for r in rows:
        print('|'.join(r))
        print('-'*5)

print_board()
