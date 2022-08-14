# Automate the boring stuff with python
"""
• Artificial intelligence

• List references

• Short-circuit evaluation

• The None value
"""

import random

def drawBoard(board):
    """
    This function prints the board that passes through it
    :param: list of 10 strings representing the board (ignore index 0)
    :return: N.A
    """
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def inputPlayerLetter():
        """
        This function gets the letter X or O that the human wants to be
        :param: nothing much
        :return: dictionary of human and computer letter
        """
        ask = True
        while ask:
            try:
                letter = str(input("Do you wish to be letter 'X' or 'O': "))
                letter = letter.upper()
                if letter == 'X' or letter == 'O':
                    ask = False
            except Exception as e:
                print(f"Because of error {e}, please input a letter")

        if letter == "X":
            return ["X", "O"]
        else:
            return ["O", "X"]

def whoGoesFirst(opponent):
    """
    Randomly chooses which player goes first
    :param: -
    :return: whether it is the humans of the computers turn
    """
    if opponent == 'Computer':
        turn = random.randint(0, 1)
        if turn == 0:
            return "Computer"
        else:
            return "Human"
    if opponent == "Player":
        turn = random.randint(0, 1)
        if turn == 0:
            return "Player1"
        else:
            return "Player2"


def makeMove(board, letter, move):
    """
    helps make the move
    :param: board=10 strings, letter, move
    :return: -
    """
    board[int(move)] = letter

def isWinner(bo, le):
    """
    Determines whether the goal state has been reached
    To check whether either the computer of the human has won
    :param: board=10 strings, move, letter
    :return: -
    # 'bo'=> board
    # 'le'=> letter
    """
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right
    (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def getBoardCopy(board):
    """
    Makes copy of the board. When testing moves we don't want to change the actual board
    :param: board
    :return: copy of board as a list
    """
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def isSpaceFree(board, move):
    """
    Determines whether space on the board is free
    :param: board, move
    :return: True or False
    """
    return board[move] == ' '


def getPlayerMove(board):
    # Allows the player to enter their move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What is your next move?")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, ComputerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == "X":
        playerLetter = "O"
    if computerLetter == "O":
        playerLetter = "X"

    # AI for tic tac toe algorithm

    # Check if computer can win in next move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Check if player could win on the next move and block them
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Try to take one of the corners if they are free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center if it is free
    if isSpaceFree(board, 5):
        return 5

    # Try to take one of the sides if they are free
    move = chooseRandomMoveFromList(board, [2, 4, 6, 8])
    if move != None:
        return move

def isBoardFull(board):
    # Return True if every space on board is taken
    # Return False if there is a space left on the board
    for i in range(1, len(board)):
        if isSpaceFree(board, i):
            return False

    return True

def opponentSelect():
    # Asks players whether they want to play two-player or against a computer
    print("\033[1m" + "Opponent select" + "\033[0m") # "\033[1m" => to make the string bold
    opponents = ['Player vs player', 'Player vs Computer']
    print(opponents[0] + ' or ' + opponents[1])
    selectedOption = input("Computer (c)\nPlayer (p)\n")
    if selectedOption.lower().startswith('c'):
        return "Computer"
    if selectedOption.lower().startswith('p'):
        return "Player"

def twoPlayerGamePlay():
    # Player one chooses a letter first
    print("Player 1 choose your letter (X or O): ")
    player1Letter, player2Letter = inputPlayerLetter() # Whatever player 1 chooses player 2 is the opposite letter
    # After letters are decided it is randomly chosen who goes first
    turn = whoGoesFirst(opponent) # Who goes first Player1 or Player2
    print(f"{turn} is going first")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "Player1":
            # Player 1 turn
            drawBoard(theBoard)
            print("Player 1:", end=' ')
            move = getPlayerMove(theBoard)
            makeMove(theBoard, player1Letter, move)

            if isWinner(theBoard, player1Letter):
                drawBoard(theBoard)
                print("Hooray Player 1 has won the game")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game's a tie")
                    break
                else:
                    turn = 'Player2'

        # Player 2 turn
        drawBoard(theBoard)
        print("Player 2", end='')
        move = getPlayerMove(theBoard)
        makeMove(theBoard, player2Letter, move)

        if isWinner(theBoard, player2Letter):
            drawBoard(theBoard)
            print("Hooray Player 2 has won the game")
            gameIsPlaying = False
        else:
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print("The game's a tie")
                break

        turn = 'Player1'


print("Welcome to Tic-Tac-Toe")
# Game loop
while True:
    # Reset the board
    theBoard = [" "] * 10
    opponent = opponentSelect()
    if opponent == "Computer":
        playerLetter, computerLetter = inputPlayerLetter()
        print("players and computers letters are: ", playerLetter, computerLetter)
        turn = whoGoesFirst(opponent)
        print(f"{turn} will go first")
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == "Human":
                # Humans turn
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print("Hooray you have won the game")
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print("The game's a tie")
                        break
                    else:
                        turn == 'Computer'

            # Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Human'

    elif opponent == "Player":
        twoPlayerGamePlay()

    wish = input("Do you wish to play again (y or n): ")
    if not wish.lower().startswith('y'):
        break
