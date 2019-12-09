def checkWin(move, board, player): # move: [x, y, z] AKA the address

   x = move[0]
   y = move[1]
   z = move[2]

   # z-check
   if board[x][y] == [player, player, player, player]:
       print("Player " + str(player) + " wins!")
       return True

   # x-check
   sumx = 0
   for i in range(4):
      sumx += board[i][y][z]
      if sum == player*4:
         print("Player " + str(player) + " wins!")
         return True

   # y-check
   sumy = 0
   for i in range(4):
           sumy += board[x][i][z]
           if sum == player*4:
               print("Player " + str(player) + " wins!")
               return True



   #diagonal check 1
   sumd1 = 0
   for i in range(4):
           sumd1 += board[i][i][z]
           if sumd1 == player*4:
               print("Player " + str(player) + " wins!")
               return True

   #diagonal check 2
   sumd2 = 0
   for i in range(4):
           sumd1 += board[i][3-i][z]
           if sumd1 == player*4:
               print("Player " + str(player) + " wins!")
               return True

   #diagonal check 3
   sumd3 = 0
   for i in range(4):
           sumd3 += board[x][i][i]
           if sumd3 == player*4:
               print("Player " + str(player) + " wins!")
               return True

   #diagonal check 4
   sumd4 = 0
   for i in range(4):
           sumd4 += board[x][3-i][i]
           if sumd4 == player*4:
               print("Player " + str(player) + " wins!")
               return True


   #diagonal check 5
   sumd5 = 0
   for i in range(4):
           sumd5 += board[i][y][i]
           if sumd5 == player*4:
               print("Player " + str(player) + " wins!")
               return True

   #diagonal check 6
   sumd6 = 0
   for i in range(4):
           sumd6 += board[3-i][y][i]
           if sumd6 == player*4:
               print("Player " + str(player) + " wins!")
               return True



   #Grand Diagonal Checks (4)


   #GD check 1
   sumgd1 = 0
   for i in range(4):
           sumdgd1 += board[i][i][i]
           if sumgd1 == player*4:
               print("Player " + str(player) + " wins!")
               return True

   #GD check 2
   sumgd2 = 0
   for i in range(4):
           sumdgd2 += board[3-i][i][i]
           if sumgd2 == player*4:
               print("Player " + str(player) + " wins!")
               return True

   #GD check 3
   sumgd3 = 0
   for i in range(4):
           sumdgd3 += board[i][3-i][i]
           if sumgd3 == player*4:
               print("Player " + str(player) + " wins!")
               return True

   #GD check 4
   sumgd4 = 0
   for i in range(4):
           sumdgd4 += board[i][i][3-i]
           if sumgd4 == player*4:
               print("Player " + str(player) + " wins!")
               return True



   return False


   '''
  def check_diagonals(a,b,c):
   sumd = 0
   for i in range(4):
           sumd1= board[i][i][z]
           if sumd1= player*4:
               print("Player " + str(player) + " wins!")
               return True
            else
               return False

  sum = 0
  for i in range(4)
   sum = check_axes(i,y,z)
   if sum = player * 4:
           print ("Player" + str(player) + " wins!")
           return True


  def check_axes (x, y, z, sum):
      return sum + board[x][y][z]



   '''
