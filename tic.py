"""Console Tic-Tac-Toe
Incremental game built for git-bisect practice."""

def play_once():
    board=[' ']*9
    WIN=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

    def show():
        for i in range(0,9,3):
            print('|'.join(board[i:i+3])); print('-'*5)

    def winner(m):
        return any(all(board[i]==m for i in line) for line in WIN)

    player='X'
    while True:
        show()
        try:
            idx=int(input(f'{player} choose (1-9): '))-1
            if not 0<=idx<9 or board[idx] != ' ':
                raise ValueError
        except ValueError:
            print('Invalid move. Try again.')
            continue
        board[idx]=player
        if winner(player):
            show(); print(f'{player} wins!'); break
        if ' ' not in board:
            show(); print('Draw!'); break
        player='O' if player=='X' else 'X'

if __name__ == '__main__':
    while True:
        play_once()
        if input('Play again (y/n)? ').lower()!='y':
            break
