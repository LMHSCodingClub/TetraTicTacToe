#import checkWin


player = 1
move = 0

def checkWin(move):
    if move < 3:
        return False
    else:
        return True

def createEmptyBoard():
    print("ok")
    board = []
    for i in range(4):
        empty = []
        board.append(empty)
        for j in range(4):
            emptyDim2 = []
            board[i].append(emptyDim2)
            for k in range(4):
                board[i][j].append(0)

    return board

def getUserInput(move):
    return [move,move,move]

board = createEmptyBoard()

while not checkWin(move):
    move+=1
    player *= -1
    cube = getUserInput(move)
    board[cube[0]][cube[1]][cube[2]] = player
    print(board)

print("Player " + str(player)  + " won!")
