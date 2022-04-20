import random

#Global Variables
Row1 = ['-','-','-']
Row2 = ['-','-','-']
Row3 = ['-','-','-']
Board = [Row3,Row2,Row1]
Coloum = []
DiagonalL = []
DiagonalR = []
Xwin = ['X','X','X']
Owin = ['O','O','O']
occupied = False
win = False
turnnum = 0
AIletter = 'O'
Plrletter = 'X'

#Prints current board state
def printboard():
  for rows in range(len(Board)):
        print(Board[rows])


#Promted player input for human turn
def playerturn():
  global turnnum
  plrinput = input('\"X\" input position (1-9): ')
  intinput = int(plrinput)
  #Checks for valid
  if intinput<1 or intinput>9:
    print('Please enter a valid number.')
    playerturn()
  else:
    freespace(intinput)
    if occupied == False:
      setlocation(intinput, Plrletter)
    else:
      print('Please pick an unoccupied space')
      playerturn()

#Checks for free space
def freespace(index):
  global occupied
  rownum = 0
  numvalid = False
  if index > 6:
    rownum = 7
    row = Row3
  elif index < 4:
    rownum = 1
    row = Row1
  else:
    rownum = 4
    row = Row2

  if row[index-rownum] == '-':
    occupied = False


#Places pieces
def setlocation(index, letter):
  rownum = 0
  if index > 6:
    rownum = 7
    row = Row3
  elif index < 4:
    rownum = 1
    row = Row1
  else:
    rownum = 4
    row = Row2

  row[index-rownum] = letter

#Checks game for win state
def winstate():
  coloum = 0
  global win
  global DiagonalL
  global DiagonalR
  #Checks for horizontal wins
  DiagonalR = [Row3[2],Row2[1], Row1[0]]
  DiagonalL = [Row3[0], Row2[1], Row1[2]]
  for row in Board:
    if row == Xwin:
      win = True
      print('X wins!')
    elif row == Owin:
      win = True
      print('O wins!')
  #Checks for vertical wins
  while coloum<3:
    Coloum.append(Row1[coloum])
    Coloum.append(Row2[coloum])
    Coloum.append(Row3[coloum])
    if Coloum == Xwin:
      win = True
      print('X wins!')
    elif Coloum == Owin:
      win = True
      print('O wins!')
    Coloum.clear()
    coloum = coloum + 1

  #Checks for diagonal wins

  if DiagonalL == Xwin:
    win = True
    print('X wins!')
  elif DiagonalR == Owin:
    win = True
    print('O wins!')
  elif DiagonalR == Xwin:
    win = True
    print('X wins!')
  elif DiagonalR == Owin:
    win = True
    print('O wins!')


#Plays game while not in win state
def boardplaystate():
  global turnnum
  global win
  while win == False:
    if turnnum < 5:
      playerturn()
      winstate()
      if win == False:
        Ply2Turn(Board, AIletter)
        printboard()
        winstate()
      else:
        printboard()




# Jalen's Code =========================================================================

# Does a valid move from the lsit on the past board
#returns None if there are no valid moves
def RandomMove(board, nlist):
  pMoves = []
  for i in nlist:
    freespace(i)
    if occupied == False:
      pMoves.append(i)


#get a random int from that list
#return the random int
  if len(pMoves) > 0:
    randmove = random.choice(pMoves)
  else:
    return None
  return randmove

#determines the AI's Letter either it being X or O based of player 1
# Determines where the computer can move on the board
def Ply2Turn(board, letter):
  playlimit = random.randint(1,3)
  attempt = 0
  played = False
  for row in range(0,9):
    copy = board
    freespace(row)

  if playlimit == 1:
    #AI player corner moves
    while attempt < 4:
      Cmove = RandomMove(board, [1, 3, 7, 9])
      if Cmove != None:
        intcmove = int(Cmove)
        freespace(intcmove)
        if occupied == False:
          setlocation(intcmove,AIletter)
          played = True
          print('O Played a corner')
          attempt = 4
        else:
          attempt = attempt+1

    playlimit = random.randint(1,3)

  elif playlimit == 2:
    #AI player takes middle square if the position is free on the board
    freespace(5)
    if occupied == False:
      setlocation(5, AIletter)
      print('O played a center')
      played = True
    playlimit = random.randint(1,3)

  elif playlimit == 3:
  #AI player side moves
    attempt = 0
    while attempt < 4:
      Smove = RandomMove(board, [2, 4, 6, 8])
      if Smove != None:
        intsmove = int(Smove)
        freespace(intsmove)
        if occupied == False:
          setlocation(intsmove, AIletter)
          attempt = 4
          print('O played a side')
          played = True
      attempt = attempt+1
      playlimit = random.randint(1,3)


  if played == False:
    Ply2Turn(board, AIletter)



printboard()
boardplaystate()
