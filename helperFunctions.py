import random

""" MINIMAX FUNCTION (source: http://goo.gl/sJgv68)
PURPOSE: backtracking algorithm used in game theory to find optimal move for player
PARAMETERS: game board, level of current backtracking stage, whether to maximize optimal move
RETURN: best optimal score found
"""
def minimax(board,depth,isMax,player_symbol,bot_symbol):
    if checkWin(board,player_symbol):
        return -10
    if checkWin(board,bot_symbol):
        return 10
    if boardIsFull(board):
        return 0
    if (isMax): #maximizer's move
        best = -1000
        for i in range(1,10):
            if board[i] == '_':
                board[i] = bot_symbol
                #call minimax recursively + choose max value
                best = max(best, minimax(board,depth+1,not isMax,player_symbol,bot_symbol))
                #undo the move
                board[i] = '_'
        return best
    else: #minimizer's move
        best = 1000
        for i in range(1,10):
            if board[i] == '_':
                board[i] = player_symbol
                best = min(best, minimax(board,depth+1,not isMax,player_symbol,bot_symbol))
                board[i] = '_'
        return best

def findBestMove(board,symbol,player_symbol,bot_symbol):
    bestVal = -1000
    bestMove = 0
    
    for i in range(1,10):
        if board[i] == '_':
            #make the move 
            board[i] = symbol
            #evaluate minimax for move
            moveVal = minimax(board,0,False,player_symbol,bot_symbol) #TODO: check needs True
            board[i] = '_'
            #if value of current move greater than best value, update best
            if (moveVal > bestVal):
                bestMove = i
                bestVal = moveVal
    # print("The value of the best Move is :", bestVal)
    # print()
    return bestMove
    
    #go through each cell, calculate minimax function for empty cells
    

def printBoard(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print()
    
def chooseSymbol():
    symbol = ''
    while not (symbol == 'X' or symbol == 'O'):
        symbol = input('~ Welcome Tic-Tac-Toe Player ~ \nDo you want to be (X) or (O) ?')
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
        print("CHOSEN POSITION: ",position)
        while board[position] != '_':
            print("space %s is NOT EMPTY, try again\n"%(position))
            position = int(input("Choose an AVAILABLE position from 1-9: "))
            # return position
    return position
    
def randomSpot(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] and spotIsEmpty(position,board):
        position = random.choice([1,2,3,4,5,6,7,8,9])
        while board[position] != '_':
            position = random.choice([1,2,3,4,5,6,7,8,9])
    return position

def spotIsEmpty(position,board):
    if board[position] == '_':
        return True
    else: return False
    
def checkWin(board,symbol):
    return ((board[7] == symbol and board[8] == symbol and board[9] == symbol) or # across the top
    (board[4] == symbol and board[5] == symbol and board[6] == symbol) or # across the middle
    (board[1] == symbol and board[2] == symbol and board[3] == symbol) or # across the bottom
    (board[7] == symbol and board[4] == symbol and board[1] == symbol) or # down the middle
    (board[8] == symbol and board[5] == symbol and board[2] == symbol) or # down the middle
    (board[9] == symbol and board[6] == symbol and board[3] == symbol) or # down the right 
    (board[7] == symbol and board[5] == symbol and board[3] == symbol) or # diagonal
    (board[9] == symbol and board[5] == symbol and board[1] == symbol)) # diagonal
    
def boardIsFull(board):
    for i in range(1,10):
        if spotIsEmpty(i,board):
            return False
    return True
