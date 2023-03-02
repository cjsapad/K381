# import for coloured text --> change 1 (see player names)
import colorama
from colorama import Fore

# define the board
board = [["_" for i in range(3)] for j in range(3)]

# title of the game --> change 2
print('''Let`s play Tic Tac Toe!
Player O Starts First''')

# define the player's move
def make_move(board, player, row, col):
  board[row][col] = player

# define the function to check for a winner
def check_winner(board):
  # check rows
  for row in range(3):
    if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
      return board[row][0]

  # check columns
  for col in range(3):
    if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
      return board[0][col]

  # check diagonals
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
    return board[0][0]
  if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
    return board[2][0]

  # if there is no winner, return None
  return None

# define the function to check if the game is a draw
def check_draw(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == "_":
        return False
  return True

# define the function to play the game
def play_game():
  # initialize the game
  player = "X"
  winner = None
  draw = False

  # loop until the game is over
  while not winner and not draw:
    # print the current board
    for row in board:
      print(" ".join(row))

    # get the player's move and label players --> change 3
    if player == 'X':
        print(Fore.RED + 'Player O:')
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        player ="O"
    else:
        player = "X"
        print(Fore.BLUE + 'Player X:')
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

    # make the move
    make_move(board, player, row, col)

    # check for a winner
    winner = check_winner(board)

    # check for a draw
    draw = check_draw(board)

    # switch players --> deleted
#    if player == "X":
#      player = "O"
#    else:
#      player = "X"

  # print the final board
  for row in board:
    print(" ".join(row))

  # print the result of the game
  if winner:
    print(f"Player {winner} wins!")
  else:
    print("The game is a draw.")

# play the game
play_game()