def game():
    board=[' ']*9
    WIN=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    def print_board():
        for i in range(0,9,3):
            print('|'.join(board[i:i+3])); print('-'*5)
    def win(m): return any(all(board[i]==m for i in l) for l in WIN)
    cur='X'
    while True:
        print_board()
        try:
            idx=int(input(f'{cur} 1-9: '))-1
            if board[idx]!=' ': raise ValueError
        except: print('Try again'); continue
        board[idx]=cur
        if win(cur): print_board(); print(f'{cur} wins'); break
        if ' ' not in board: print_board(); print('Draw'); break
        cur='O' if cur=='X' else 'X'

while True:
    game()
    if input('Play again (y/n)? ').lower()!='y':
        break
