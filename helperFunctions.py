def printBoard(board):
    
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    
def chooseSymbol():
    
    symbol = ''
    while not (symbol == 'X' or symbol == 'O'):
        symbol = input('Welcome Tic-Tac-Toe Player.\nDo you want to be (X) or (O) ?')
    if symbol == 'X':
        return 'X','O'
    else: return 'O', 'X'
