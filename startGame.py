from helperFunctions import *
import time
def startGame():
    
    board = ['_']* 10
    printBoard(board)
    player_symbol, bot_symbol = chooseSymbol()
    print("PROGRAM RANDOMLY PICKS FIRST TURN ....\n")
    time.sleep(2)
    # current_turn = randomizeFirstTurn()
    current_turn = 'BOT' #TODO: remove after testing
    print("%s GOES FIRST\n"%(current_turn))
    print("----- SPACES ARE MARKED AS SHOWN -----")
    printBoard(['0','1','2','3','4','5','6','7','8','9'])
    print("--------------------------------------\n")
    gameNotOver = True
    
    while gameNotOver:
        if current_turn == 'PLAYER':
            printBoard(board)
            position = chooseSpot(board)
            board[position] = player_symbol
            if checkWin(board,player_symbol):
                printBoard(board)
                print('*** PLAYER WINS!!! GREAT WORK!!! ***')
                gameNotOver = False
            else:
                if boardIsFull(board):
                    printBoard(board)
                    print('*** UH-OH! BOARD IS FULL AND THERE IS NO WINNER ***')
                    break
                else: current_turn = 'BOT'
        else:
            printBoard(board)
            position = randomSpot(board)
            board[position] = bot_symbol
            if checkWin(board,bot_symbol):
                printBoard(board)
                print('*** BOT WINS... BETTER LUCK NEXT TIME ***')
                gameNotOver = False
            else:
                if boardIsFull(board):
                    printBoard(board)
                    print('*** UH-OH! BOARD IS FULL AND THERE IS NO WINNER ***')
                    break
                else: current_turn = 'PLAYER'
            
        # gameNotOver = False #TODO: remove after testing
startGame()
