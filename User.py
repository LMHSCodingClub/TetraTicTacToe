from PIL import Image

def getUserInput(move):
    color = getColor(move)
    if color == (0,0,0) or color == (255,255,255):
        return None

    #set the move based on the clicked color, return None if no color match.
    xyzString = ""
    for xyzChoice, colorChoice in colorValues.items():
        if color == colorChoice:
            xyzString = xyzChoice
    if xyzString == "":
        return None

    print("clicked square: " + str([int(xyzString[0]),int(xyzString[1]),int(xyzString[2])]))
    return [int(xyzString[0]),int(xyzString[1]),int(xyzString[2])]

# color to coordinate dict
colorValues = {
    "000":(0, 80, 115),
    "100":(25, 4, 56),
    "200":(140, 102, 53),
    "300":(204, 185, 157),
    "010":(116, 73, 0),
    "110":(122, 119, 0),
    "210":(57, 95, 11),
    "310":(0, 75, 24),
    "020":(153, 0, 80),
    "120":(152, 0, 52),
    "220":(108, 0, 10),
    "320":(113, 45, 8),
    "030":(0, 112, 159),
    "130":(4, 68, 118),
    "230":(29, 42, 99),
    "330":(68, 3, 81),

    "001":(167, 164, 0),
    "101":(81, 132, 19),
    "201":(0, 106, 37),
    "301":(0, 109, 104),
    "011":(225, 0, 82),
    "111":(150, 0, 20),
    "211":(156, 65, 15),
    "311":(161, 103, 0),
    "021":(49, 67, 150),
    "121":(103, 8, 123),
    "221":(145, 0, 123),
    "321":(227, 0, 123),
    "031":(0, 159, 60),
    "131":(0, 164, 157),
    "231":(0, 169, 236),
    "331":(6, 105, 178),

    "002":(239, 156, 0),
    "102":(249, 244, 0),
    "202":(124, 198, 35),
    "302":(0, 176, 52),
    "012":(234, 107, 72),
    "112":(240, 148, 80),
    "212":(245, 184, 87),
    "312":(254, 247, 104),
    "022":(236, 107, 118),
    "122":(237, 108, 158),
    "222":(142, 86, 156),
    "322":(106, 80, 155),
    "032":(140, 205, 202),
    "132":(63, 88, 240),
    "232":(147, 170, 214),
    "332":(103, 110, 176),

    "003":(62, 184, 180),
    "103":(49, 181, 115),
    "203":(136, 202, 157),
    "303":(200, 226, 157),
    "013":(142, 142, 142),
    "113":(61, 61, 61),
    "213":(243, 157, 119),
    "313":(255, 250, 157),
    "023":(206, 206, 206),
    "123":(255, 255, 254),
    "223":(255, 0, 255),
    "323":(0, 0, 255),
    "033":(255, 0, 0),
    "133":(255, 255, 0),
    "233":(0, 255, 0),
    "333":(0, 255, 255),
}

def getColor(pos):
    colorMap = Image.open('gameboardColor.png') # This is the colormap, we never want the user to see it
    pix = colorMap.load()
    value = pix[pos[0],pos[1]][:3] # returns color value at x,y
    return(value)

    colorMap.close()

def getXYZ(color):
    return(colorValues.get(color))
