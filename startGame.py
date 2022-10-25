from helperFunctions import *
def startGame():
    
    board = ['_']* 9
    printBoard(board)
    player_symbol, bot_symbol = chooseSymbol()
    print("PLAYER:",player_symbol)
    print("BOT:",bot_symbol)
    
startGame()
