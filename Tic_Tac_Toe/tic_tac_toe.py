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

#MY SOLUTION 
def tic_tac_toe_win_check(board):
  # check the board to see if any of the three win type requirements are met
  #check each row
  for row in board:
    #if all three numbers of that row are the same return that number
    if row[0] == row[1] and row[1] == row[2]:
      return row[0]
      
  #check each col 
  for indexCol in range(len(board[0])):
    #get the sum of the col divided by the number of rows in the column
    #if all three of any column are the same 
    if board[0][indexCol] == board[1][indexCol] and board[1][indexCol] == board[2][indexCol]:
      return board[0][indexCol]
      
  #check first diagonal for a win 
  if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    return board[0][0]
  #check second diagonal for a win
  if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
    return board[0][2]

  # if no player won anything return 0
  return 0

# print("Row win: ",tic_tac_toe_win_check(tic_tac_toe_row))
# print("Column win:", tic_tac_toe_win_check(tic_tac_toe_column))
# print("Diag win:", tic_tac_toe_win_check(tic_tac_toe_diag))
