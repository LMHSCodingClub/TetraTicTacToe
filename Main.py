import CheckWin
import User


player = 1
move = 0

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

board = createEmptyBoard()

while not CheckWin.checkWin(move):
    move+=1
    player *= -1
    cube = User.getUserInput(move)
    board[cube[0]][cube[1]][cube[2]] = player
    print(board)

print("Player " + str(player)  + " won!")
