import pygame
from pygame.locals import *
import CheckWin
import User
pygame.init()

#how to start a new game w/empty board
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

#user interface definitions
LEFT = 1 # left button
(width, height) = (600, 750)
backgroundColor = (255,255,255)
bg = pygame.image.load('/home/phillip/projects/TetraTicTacToe/gameboard.png')
screen = pygame.display.set_mode((width, height))
pygame.display.flip()# screen modifications must be done before flip()

#game definitions
player = 1
move = 0
board = createEmptyBoard()


while not CheckWin.checkWin(move):
    #update move stuff
    move+=1
    player *= -1

    #update screen
    screen.blit(bg, (0, 0))
    pygame.display.flip()

    #wait for a click, quit when X clicked
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
        print ("You pressed the left mouse button at (%d, %d)" % event.pos)
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        print ("You released the left mouse button at (%d, %d)" % event.pos)


    #now that user input has been detected, play the game
    cube = User.getUserInput(move)
    board[cube[0]][cube[1]][cube[2]] = player
    print(board)


print("Player " + str(player)  + " won!")
