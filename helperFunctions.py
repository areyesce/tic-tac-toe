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

""" FIND BEST MOVE FUNCTION 
PURPOSE: iterate over available positions to find optimal move using minimax algorithm
PARAMETERS: game board, bot symbol (only bot uses minimax), player and bot symbols
RETURN: best move to make based on most optimal score found
"""
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
    return bestMove
    
""" PRINT BOARD FUNCTION 
PURPOSE: print current state of the game board
PARAMETERS: game board
RETURN: None
"""
def printBoard(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print()

""" CHOOSE SYMBOL FUNCTION 
PURPOSE: prompt user to input which symbol to use to mark their positions
PARAMETERS: None
RETURN: ordered pair of user's chosen symbol and designated bot symbol
"""
def chooseSymbol():
    symbol = ''
    while not (symbol == 'X' or symbol == 'O'):
        symbol = input('~ Welcome Tic-Tac-Toe Player ~ \nDo you want to be (X) or (O) ?')
    if symbol == 'X':
        return 'X','O'
    else: return 'O', 'X'
    
""" FUNCTION TO RANDOMIZE FIRST TURN
PURPOSE: randomly select which user will go first
PARAMETERS: None
RETURN: string indicating whether PLAYER or BOT goes first
"""
def randomizeFirstTurn():
    if random.randint(0, 1) == 0:
        return 'PLAYER'
    else:
        return 'BOT'
  
""" CHOOSE SPOT FUNCTION 
PURPOSE: prompt user to input which position to place their symbol
PARAMETERS: game board
RETURN: user's chosen position
"""      
def chooseSpot(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] and spotIsEmpty(position,board):
        position = int(input("Choose an available position from 1-9: "))
        print("CHOSEN POSITION: ",position)
        while board[position] != '_':
            print("space %s is NOT EMPTY, try again\n"%(position))
            position = int(input("Choose an AVAILABLE position from 1-9: "))
    return position
 
""" CHECK IF SPOT IS EMPTY FUNCTION 
PURPOSE: check whether given position on the game board is empty
PARAMETERS: position, game board
RETURN: TRUE if position is available, FALSE otherwise
"""    
def spotIsEmpty(position,board):
    if board[position] == '_':
        return True
    else: return False
   
""" CHECK FOR A WIN FUNCTION 
PURPOSE: checks whether given symbol has marked a win on the board
PARAMETERS: symbol to check win for, game board
RETURN: TRUE if symbol has marked a win, FALSE otherwise
"""    
def checkWin(board,symbol):
    return ((board[7] == symbol and board[8] == symbol and board[9] == symbol) or # across the top
    (board[4] == symbol and board[5] == symbol and board[6] == symbol) or # across the middle
    (board[1] == symbol and board[2] == symbol and board[3] == symbol) or # across the bottom
    (board[7] == symbol and board[4] == symbol and board[1] == symbol) or # down the middle
    (board[8] == symbol and board[5] == symbol and board[2] == symbol) or # down the middle
    (board[9] == symbol and board[6] == symbol and board[3] == symbol) or # down the right 
    (board[7] == symbol and board[5] == symbol and board[3] == symbol) or # diagonal
    (board[9] == symbol and board[5] == symbol and board[1] == symbol)) # diagonal

""" CHECK BOARD IS FULL FUNCTION 
PURPOSE: iterate over every space to check if the board is full
PARAMETERS: game board
RETURN: TRUE if game board is full, FALSE otherwise
"""       
def boardIsFull(board):
    for i in range(1,10):
        if spotIsEmpty(i,board):
            return False
    return True
