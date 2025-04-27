board=[' ']*9
WIN_LINES=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def print_board():
    rows=[board[i:i+3] for i in range(0,9,3)]
    for r in rows:
        print('|'.join(r)); print('-'*5)

def check_winner(m):
    return any(all(board[i]==m for i in l) for l in WIN_LINES)

def draw():
    return ' ' not in board

current='X'
while True:
    print_board(); move=int(input(f'{current} 1-9: '))-1
    if board[move]!=' ': continue
    board[move]=current
    if check_winner(current):
        print_board(); print(f'{current} wins!'); break
    if draw():
        print_board(); print('Draw!'); break
    current='O' if current=='X' else 'X'
