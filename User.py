from PIL import Image

'''
def getUserInput(move):
    return [move,move,move]
'''

colorMap = Image.open('gameboardColor.png') # This is the colormap, we never want the user to see it
pix = colorMap.load()
value = pix[300,300][:3] # returns color value at x,y
print(value)

colorMap.close()
