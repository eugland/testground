board=[' ']*9
WIN=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def print_board():
    rows=[board[i:i+3] for i in range(0,9,3)]
    for r in rows:
        print('|'.join(r)); print('-'*5)

def winner(m):
    return any(all(board[i]==m for i in l) for l in WIN)

def full():
    return ' ' not in board

def get_move(p):
    while True:
        try:
            idx=int(input(f'{p} (1-9): '))-1
            if board[idx]==' ': return idx
        except: pass
        print('Invalid move.')

def play():
    cur='X'
    while True:
        print_board(); board[get_move(cur)]=cur
        if winner(cur):
            print_board(); print(f'{cur} wins!'); break
        if full():
            print_board(); print('Draw!'); break
        cur='O' if cur=='X' else 'X'

play()
