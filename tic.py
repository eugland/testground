board = [' ']*9

WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),  # rows
    (0,3,6),(1,4,7),(2,5,8),  # cols
    (0,4,8),(2,4,6)           # diags
]

def print_board():
    rows = [board[i:i+3] for i in range(0, 9, 3)]
    for r in rows:
        print('|'.join(r))
        print('-'*5)

def check_winner(mark):
    return any(all(board[i]==mark for i in line) for line in WIN_LINES)

current='X'
while True:
    print_board()
    move=int(input(f'{current} choose 1-9: '))-1
    if board[move]!=' ': continue
    board[move]=current
    if check_winner(current):
        print_board(); print(f'{current} wins!'); break
    if ' ' not in board:
        print_board(); print('Draw!'); break
    current='O' if current=='X' else 'X'
