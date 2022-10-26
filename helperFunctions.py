import random
def printBoard(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    
def chooseSymbol():
    symbol = ''
    while not (symbol == 'X' or symbol == 'O'):
        symbol = input('Welcome Tic-Tac-Toe Player.\nDo you want to be (X) or (O) ?')
    if symbol == 'X':
        return 'X','O'
    else: return 'O', 'X'
    
def randomizeFirstTurn():
    if random.randint(0, 1) == 0:
        return 'PLAYER'
    else:
        return 'BOT'
        
def chooseSpot(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] and spotIsEmpty(position,board):
        position = int(input("Choose an available position from 1-9: "))
    return position

def spotIsEmpty(position,board):
    if board[position] == '_':
        return True
    else: return False
    
def checkWin(board,symbol):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right 
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
def boardIsFull(board):
    for i in range(1,10):
        if spotIsEmpty(i,board):
            return False
    return True
