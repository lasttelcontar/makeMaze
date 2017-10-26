# Let's build a maze
import math, random, struct

# Global variables
mazesize = 300 # maze is this many tiles wide
outputfile = 'Desktop/pygames/maze.bmp'
hallwidth = 4 # hallways is this many pixels wide
wallwidth = 1 # walls are this many pixels wide
m = hallwidth + wallwidth # width of a tile
blockedcode = 4
wiggliness = 5

def makemaze(n):
    """ makes a mn y mn maze """
    maze = [[0 for y in range(m*n)] for x in range(m*n)]
    pathToLowerRight(maze,n)
    token = 2
    for y in range(n):
        for x in range(n):
            if maze[y*m][x*m] == 0:
                pathToPath(maze,n,y,x,token)
                token += 1
    return maze
    
def pathToLowerRight(maze,n):
    y = 0 # y coordinate of current postion in an n y n grid
    x = 0
    corners = [[y,x]]
    while y!=n-1 or x!=n-1:
        if isDeadEnd(maze,n,y,x,1):
            s = random.randint(0,len(corners)-1)
            coords = corners[s]
            y = coords[0]
            x = coords[1]
        direction = random.randint(0,3)
        length = random.randint(0,math.ceil(n/wiggliness))
        if direction == 0: # if direction is north
            while length > 0 and y != 0:
                if maze[(y-1)*m][x*m] == 0: # our path is not blocked
                    updatemazeSquare(maze,y,x,direction,1)
                    y -= 1
                    length -= 1
                else: 
                    updatemazeSquare(maze,y,x,blockedcode,1)
                    length = 0
        elif direction == 1: # if direction is east
            while length > 0 and x != n-1:
                if maze[y*m][(x+1)*m] == 0: # our path is not blocked
                    updatemazeSquare(maze,y,x,direction,1)
                    x += 1
                    length -= 1
                else: 
                    updatemazeSquare(maze,y,x,blockedcode,1)
                    length = 0
        elif direction == 2: # if direction is south
            while length > 0 and y != n-1:
                if maze[(y+1)*m][x*m] == 0: # our path is not blocked
                    updatemazeSquare(maze,y,x,direction,1)
                    y += 1
                    length -= 1
                else: 
                    updatemazeSquare(maze,y,x,blockedcode,1)
                    length = 0
        else: # if direction is west
            while length > 0 and x != 0:
                if maze[y*m][(x-1)*m] == 0: # our path is not blocked
                    updatemazeSquare(maze,y,x,direction,1)
                    x -= 1
                    length -= 1
                else: 
                    updatemazeSquare(maze,y,x,blockedcode,1)
                    length = 0
        corners.append([y,x])
    updatemazeSquare(maze,y,x,1,1)
            
def isDeadEnd(maze,n,y,x,token):
    if y > 0 and maze[(y-1)*m][x*m]<token:
        return False
    elif x < n-1 and maze[y*m][(x+1)*m]<token:
        return False
    elif y < n-1 and maze[(y+1)*m][x*m]<token:
        return False
    elif x > 0 and maze[y*m][(x-1)*m]<token:
        return False
    else:
        return True

def pathToPath(maze,n,y,x,token):
    corners = [[y,x]]
    hitPath = False
    while hitPath != True:
        direction = random.randint(0,3)
        if isDeadEnd(maze,n,y,x,token):
            s = random.randint(0,len(corners)-1)
            coords = corners[s]
            y = coords[0]
            x = coords[1]
        length = random.randint(0,n/wiggliness)
        if direction == 0: # if direction is north
            while length > 0 and y != 0:
                if maze[(y-1)*m][x*m] == 0: # our path is not blocked
                    updatemazeSquare(maze,y,x,direction,token)
                    y -= 1
                    length -= 1
                elif maze[(y-1)*m][x*m] < token: # we hit the previous path
                    updatemazeSquare(maze,y,x,direction,token)
                    y -= 1
                    length =0
                    hitPath = True
                else: 
                    updatemazeSquare(maze,y,x,blockedcode,token)
                    length = 0
        elif direction == 1: # if direction is east
            while length > 0 and x != n-1:
                if maze[y*m][(x+1)*m] == 0: # our path is not blocked
                    updatemazeSquare(maze,y,x,direction,token)
                    x += 1
                    length -= 1
                elif maze[y*m][(x+1)*m] < token: # hits path
                    updatemazeSquare(maze,y,x,direction,token)
                    x += 1
                    length = 0
                    hitPath = True
                else: 
                    updatemazeSquare(maze,y,x,blockedcode,token)
                    length = 0
        elif direction == 2: # if direction is south
            while length > 0 and y != n-1:
                if maze[(y+1)*m][x*m] == 0: # our path is not blocked
                    updatemazeSquare(maze,y,x,direction,token)
                    y += 1
                    length -= 1
                elif maze[(y+1)*m][x*m] < token: # hits path
                    updatemazeSquare(maze,y,x,direction,token)
                    y += 1
                    length = 0
                    hitPath = True
                else: 
                    updatemazeSquare(maze,y,x,blockedcode,token)
                    length = 0
        else: # if direction is west
            while length > 0 and x != 0:
                if maze[y*m][(x-1)*m] == 0: # our path is not blocked
                    updatemazeSquare(maze,y,x,direction,token)
                    x -= 1
                    length -= 1
                elif maze[y*m][(x-1)*m] < token: # hits path
                    updatemazeSquare(maze,y,x,direction,token)
                    x -= 1
                    length = 0
                    hitPath = True
                else: 
                    updatemazeSquare(maze,y,x,blockedcode,token)
                    length = 0
        corners.append([y,x])
            
def updatemazeSquare(maze,y,x,direction,token):
    for i in range(hallwidth):
        for j in range(hallwidth):
            maze[y*m+i][x*m+j] = token
    if direction == 0:
        for i in range(wallwidth+1):
            for j in range(hallwidth):
                maze[y*m-i][x*m+j] = token
    elif direction == 1:
        for i in range(hallwidth):
            for j in range(wallwidth):
                maze[y*m+i][x*m+hallwidth+j] = token
    elif direction == 2:
        for i in range(wallwidth):
            for j in range(hallwidth):
                maze[y*m+hallwidth+i][x*m+j] = token
    elif direction == 3:
        for i in range(hallwidth):
            for j in range(wallwidth+1):
                maze[y*m+i][x*m-j] = token

def printMaze(maze):
    for row in maze:
        currentrow = ''
        for y in row:
            if y  == 0: 
                currentrow += '0'
            else:
                currentrow += ' '
        print(currentrow)

""" puts the maze in a format that can be made into a bitmap """        
def mazetobmp(maze,n):
    pad = 8-(n*m+wallwidth)%8
    rowstrings = ['1'*(n*m+wallwidth)+'0'*pad]
    for row in maze:
        currentrow = '1'*wallwidth
        for y in row:
            if y  == 0: 
                currentrow += '1'
            else:
                currentrow += '0'
        currentrow += '0'*pad
        rowstrings.append(currentrow)
    width = int((n*m+wallwidth+pad)/8)
    rows = [[int(rowstring[8*i:8*(i+1)],2) for i in range(width)]
    for rowstring in rowstrings]
    return rows, width

    
""" Building the bitmap image """
      
mult4 = lambda n: int(math.ceil(n/4))*4
mult8 = lambda n: int(math.ceil(n/8))*8
lh = lambda n: struct.pack("<h", n)
li = lambda n: struct.pack("<i", n)

def bmp(rows, w):
    h, wB = len(rows), int(mult8(w)/8)
    s, pad = li(mult4(wB)*h+0x20), [0]*(mult4(wB)-wB)
    s = li(mult4(w)*h+0x20)
    reserved = b"\x00\x00\x00\x00"
    dataoffset = b"\x20\x00\x00\x00"
    infosize = b"\x0C\x00\x00\x00"
    planes = bytes([1,0])
    bitcount = bytes([1,0])
    return (b"BM" + s + reserved + dataoffset + infosize +
            lh(w) + lh(h) + planes + bitcount + b"\xff\xff\xff\x00\x00\x00" +
            b"".join([bytes(row+pad) for row in reversed(rows)]))
            
""" What we actually run """

mymaze = makemaze(mazesize)
#printMaze(mymaze)

rows, width = mazetobmp(mymaze,mazesize)
image = bmp(rows, width*8)
saveimage = open(outputfile,'wb')
saveimage.write(image)
saveimage.close()