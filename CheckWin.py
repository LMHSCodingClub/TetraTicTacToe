def checkWin(move, board, player): # move: [x, y, z] AKA the address
   def check(xFunc, yFunc, zFunc):
      sumd = 0
      for i in range(4):
         sumd += board[xFunc(i)][yFunc(i)][zFunc(i)]
      return sumd == player * 4
   xs = [lamda i:move[0], lamda i: i, lamda i:3-i]
   ys = [lamda i:move[1], lamda i: i, lamda i:3-i]
   zs = [lamda i:move[2], lamda i:i, lamda i:3-i]
   for (a in range(3)):
      for (b in range(3)):
         for (c in range(3)):
            if check(xs[a], ys[b], zs[c]):
             return True
