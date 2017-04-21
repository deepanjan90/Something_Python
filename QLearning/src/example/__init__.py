import  GridDraw
import time
import numpy as np

dataGrid = []
for row in range(225):
    dataGrid.append([])
    for column in range(4):
        dataGrid[row].append(0)

actionGrid = []
for row in range(225):
    actionGrid.append([])
    cRow = int(row/15)
    cCol = row%15
    
    #State Up
    if(cRow-1<0):
        actionGrid[row].append("Row:"+str(cRow)+"#Col:"+str(cCol)) 
    else:
        actionGrid[row].append("Row:"+str(cRow-1)+"#Col:"+str(cCol))
        
    #State Down
    if(cRow+1>14):
        actionGrid[row].append("Row:"+str(cRow)+"#Col:"+str(cCol)) 
    else:
        actionGrid[row].append("Row:"+str(cRow+1)+"#Col:"+str(cCol)) 
        
    #State Left
    if(cCol-1<0):
        actionGrid[row].append("Row:"+str(cRow)+"#Col:"+str(cCol)) 
    else:
        actionGrid[row].append("Row:"+str(cRow)+"#Col:"+str(cCol-1))
        
    #State Right
    if(cCol+1>14):
        actionGrid[row].append("Row:"+str(cRow)+"#Col:"+str(cCol)) 
    else:
        actionGrid[row].append("Row:"+str(cRow)+"#Col:"+str(cCol+1))

a='Row:14#Col:0'
#print(np.matrix(actionGrid))


def getRowCol(rowColString):
    row=int(rowColString.split(sep="#", maxsplit=1)[0].split(sep=":", maxsplit=1)[1])
    col=int(rowColString.split(sep="#", maxsplit=1)[1].split(sep=":", maxsplit=1)[1])
    return (row,col)

print(np.random.choice(4, 1))

grid = []
for row in range(15):
    grid.append([])
    for column in range(15):
        grid[row].append(0)        

def resetDisplayGrid():
    for row in range(15):
        for column in range(15):
            grid[row][column]=0
        
def modifyDisplayGrid(prevIndexRow, prevIndexCol, currentRow, currentCol):
    grid[prevIndexRow][prevIndexCol] = 2
    grid[currentRow][currentCol] = 1
    prevIndexRow = currentRow
    prevIndexCol = currentCol

for row  in range(1):
    i = 0
    j = 0
    ii = 0
    jj = 0
    for row  in range(15):
        for event in GridDraw.pygame.event.get():
            if event.type == GridDraw.pygame.QUIT:
                GridDraw.pygame.quit()
                break;
        modifyDisplayGrid(ii, jj, i, j)
        GridDraw.DrawGrid(grid)
        time.sleep(.1)
        ii = i
        jj = j
        i += 1
        j += 1
    resetDisplayGrid()