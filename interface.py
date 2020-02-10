import pygame
from pygame.locals import *
import CheckWin
import User
import math
pygame.init()

# user interface definitions
LEFT = 1 # left button
(width, height) = (600, 750)
backgroundColor = (255,255,255)
bg = pygame.image.load('gameboard.png')
screen = pygame.display.set_mode((width, height))
pygame.display.flip()# screen modifications must be done before flip()

def updateBoard():
    print("----------------------------------")
    print("Move Number: " + str(moveNumber))
    print("Current Board: " + str(board))

#how to start a new game w/empty board
def createEmptyBoard():
    print("creating Empty Board")
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

#game definitions
player = 1
moveNumber = 0
cube = [0,0,0]
board = createEmptyBoard()
pieces = []
font = pygame.font.Font('freesansbold.ttf', 32)

while not CheckWin.checkWin(cube, board, player):
    #update moveNumber stuff
    moveNumber+=1 #moveNumber count
    player *= -1 #changes player

    #update screen
    screen.blit(bg, (0, 0))
    for i in pieces:
        if i[1] == 1:
            text = font.render('O', True, (0,255,0), (0,0,255))
        else:
            text = font.render('X', True, (0,255,0), (0,0,255))

        coord = i[0]
        updatedCoord = (coord[0] - 5, coord[1] - 5)
        screen.blit(text, updatedCoord)

    pygame.display.flip()

    moveMade = False
    while(moveMade == False):
        #wait for a click
        event = pygame.event.poll()
        #print("Event registered. Type: " + str(event.type))

        #if the red x is clicked
        if event.type == pygame.QUIT:
            pygame.quit()

        #if you left click
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            print("event: " + str(event))
            #now that user input has been detected, play the game
            cube = User.getUserInput(event.pos)
            if cube == None:
                print("Invalid Move")
            elif board[cube[0]][cube[1]][cube[2]] == 0:
                print("Valid Move")
                pieces.append((event.pos, player))
                board[cube[0]][cube[1]][cube[2]] = player
                updateBoard()
                moveMade = True
            else:
                print("Invalid Move")





print("player: " + str(player) + " won!")
