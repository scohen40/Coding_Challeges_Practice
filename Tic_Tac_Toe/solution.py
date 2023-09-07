## Given a tic-tac-toe board as a two-dimensional array (aka list), determine the winner! There are 0s, representing an empty space, 1 representing the first player, and 2 representing the second player.

## Write a function like so: tic_tac_toe_win_check(board) that returns the winner, 1 or 2, or shows a draw, 0

tic_tac_toe_row = [
  [1, 1, 1], 
  [0, 2, 0], 
  [2, 0, 2]] # row win by player 1

tic_tac_toe_column = [
  [2, 1, 0], 
  [0, 1, 0], 
  [0, 1, 2]] # column win by player 1

tic_tac_toe_diag = [
  [1, 0, 2], 
  [0, 2, 2], 
  [2, 0, 1]] # diagonal win by player 2

def check_row_win(board):
  for row in board:
    if row[0] == row[1] and row[1] == row[2]:
      return row[0]

  return False

def check_column_win(board):
  for column in range(len(board)):
    if board[0][column] == board[1][column] and board[2][column] == board[1][
        column]:
      return board[0][column]
  return False


def check_diag_win(board):
  TOP_ROW = 0
  LEFT_COL = 0
  if board[TOP_ROW][LEFT_COL] == board[TOP_ROW][1] and board[TOP_ROW][1] == board[2][2]:
    return board[1][1]
  if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
    return board[1][1]


def tic_tac_toe_win_check(board):
  the_winner = 0

  row_winner = check_row_win(board)
  if row_winner:
    return row_winner
  column_winner = check_column_win(board)
  if column_winner:
    return column_winner
  diag_winner = check_diag_win(board)
  if diag_winner:
    return diag_winner

    ## check for a row win
    ## check for a column win
    ## check for a diagonal win

  return the_winner
