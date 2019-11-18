def checkWin(move, board): # move: [x, y, z] AKA the address
    """
    * move[0] = x,
    """
    x = move[0]
    y = move[1]
    z = move[2]
    global player

    # y-check
    if board[x][y] == [player, player, player, player]:
        "Player " + str(player) + " wins!"

    # x-check
    for i in range(4):
    if board[i][0] == player

    # z-check
    elif board[x
 "Player " + str(player) + " wins!"
