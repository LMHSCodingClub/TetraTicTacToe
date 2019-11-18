def checkWin(move, board): # move: [x, y, z] AKA the address
   """
   * move[0] = x,
   """
 
   x = move[0]
   y = move[1]
   z = move[2]
   global player
  
   # z-check
   if board[x][y] == [player, player, player, player]:
       "Player " + str(player) + " wins!"
       return True
  
   # x-check
   for i in range(4):
      sumx = 0
      sumx += board[i][y][z]
      if sum == player*4:
         "Player " + str(player) + " wins!"
         return True
     
   # y-check
   for i in range(4):
           sumy = 0
           sumy += board[x][i][z]
           if sum == player*4:
               "Player " + str(player) + " wins!"
               return True
 
   #diagonal check 1
   return False
  
   
