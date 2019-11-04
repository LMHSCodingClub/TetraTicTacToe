player = 1
board = createEmptyBoard()

while !checkWin():
    player *= -1
    cube = getUserInput()
    board[cube[0]][cube[1]][cube[2]] = player
    print(board)

def createEmptyBoard():
    print("ok")
    board = []
    for(i in range(4)):
        empty = []
        board.append(empty)
        for(j in range(4)):
            emptyDim2 = []
            board[i].append(emptyDim2)
            for(k in range(4)):
                board[i][j].append(0)

    return board
                
