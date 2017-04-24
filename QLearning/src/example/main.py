import gridDraw
import numpy as np
import random
import matplotlib.pyplot as plt

global stepCountList
global iterationCountList
global iterationNumber
global prevStepCount
global isDisplayOn

isDisplayOn = False
global gridSize
global epsilonGreedy
global discountFactor
global maxIteration

gridSize = 15
epsilonGreedy = .1
discountFactor = 0.8
maxIteration = 250

def showGridDisplay():
    return True  # Change if you want to display Grid

def minStepsReachedBeforeDisplay():
    return 40  # Change it to the count when reached it would  start displaying

def turnOnDisplay():
    if(isDisplayOn == False):
        gridDraw.start()

# grid for display
displayGrid = []
def setUpDisplayGrid():
    for row in range(gridSize):
        displayGrid.append([])
        for column in range(gridSize):
            displayGrid[row].append(0) 

# Reward for being in a state
rewardGrid = []
def setUpRewardGrid():
    for row in range(gridSize*gridSize):
        rewardGrid.append(1)
        if(row==((gridSize*gridSize)-2)):
            rewardGrid.append(100)

# Reward for choosing an action and getting to that state
dataGrid = []
def setUpDataGrid():
    for row in range(gridSize*gridSize):
        dataGrid.append([])
        for column in range(4):
            dataGrid[row].append(1)

# List of states with corresponding action along with resulting state
actionGrid = []
def setUpActionGrid():
    for row in range(gridSize*gridSize):
        actionGrid.append([])
        cRow = int(row / gridSize)
        cCol = row % gridSize
        
        # State Up
        if(cRow - 1 < 0):
            actionGrid[row].append("Row:" + str(cRow) + "#Col:" + str(cCol) + "#State:" + str(row)) 
        else:
            actionGrid[row].append("Row:" + str(cRow - 1) + "#Col:" + str(cCol) + "#State:" + str(row - gridSize))
            
        # State Down
        if(cRow + 1 > gridSize-1):
            actionGrid[row].append("Row:" + str(cRow) + "#Col:" + str(cCol) + "#State:" + str(row)) 
        else:
            actionGrid[row].append("Row:" + str(cRow + 1) + "#Col:" + str(cCol) + "#State:" + str(row + gridSize)) 
            
        # State Left
        if(cCol - 1 < 0):
            actionGrid[row].append("Row:" + str(cRow) + "#Col:" + str(cCol) + "#State:" + str(row)) 
        else:
            actionGrid[row].append("Row:" + str(cRow) + "#Col:" + str(cCol - 1) + "#State:" + str(row - 1))
            
        # State Right
        if(cCol + 1 > gridSize-1):
            actionGrid[row].append("Row:" + str(cRow) + "#Col:" + str(cCol) + "#State:" + str(row)) 
        else:
            actionGrid[row].append("Row:" + str(cRow) + "#Col:" + str(cCol + 1) + "#State:" + str(row + 1))
            
# Setup all the grids
def setUpGrids():
    setUpDisplayGrid()
    setUpRewardGrid()
    setUpDataGrid()
    setUpActionGrid()

# Get row column and state details from coagulated string
def getRowColState(rowColString):
    row = int(rowColString.split(sep="#", maxsplit=2)[0].split(sep=":", maxsplit=1)[1])
    col = int(rowColString.split(sep="#", maxsplit=2)[1].split(sep=":", maxsplit=1)[1])
    state = int(rowColString.split(sep="#", maxsplit=2)[2].split(sep=":", maxsplit=1)[1])
    return (row, col, state)    

# resetting the display
def resetDisplayGrid():
    for row in range(gridSize):
        for column in range(gridSize):
            displayGrid[row][column] = 0

# Updating display grid with path        
def modifyDisplayGrid(prevIndexRow, prevIndexCol, currentRow, currentCol):
    displayGrid[prevIndexRow][prevIndexCol] = 2
    displayGrid[currentRow][currentCol] = 1
    prevIndexRow = currentRow
    prevIndexCol = currentCol

# updating the display with the updated grid
def updateGridDispay(prevRow, prevCol, currentRow, currentCol):
    for event in gridDraw.pygame.event.get():
        if event.type == gridDraw.pygame.QUIT:
            gridDraw.pygame.quit()
            break
    modifyDisplayGrid(prevRow, prevCol, currentRow, currentCol)
    gridDraw.DrawGrid(displayGrid)

# plot graph for iteration vs steps
def plotGraph(iterationCountList, stepCountList):
    plt.plot(iterationCountList, stepCountList)
    plt.ylabel('Steps')
    plt.xlabel('Iterations')
    plt.show()

# Q learning Algorithm
def qLearn():    
    stepCountList = []
    iterationCountList = []
    prevStepCount = 0
    iterationNumber = 1
    isChanged = True
    while(isChanged):
        isChanged = False
        resetDisplayGrid()
        done = False
        currentRow = 0
        currentCol = 0
        currentStateIndex = 0
        prevRow = 0
        prevCol = 0
        prevStateIndex = 0
        finishStateIndex = (gridSize*gridSize  - 1)
        randomActionIndex = 0
        possibleActionIndex = [0, 1, 2, 3]
        stepCount = 0
        while (done != True):
            stepCount += 1
            if(prevStepCount < minStepsReachedBeforeDisplay() and prevStepCount > 0 and showGridDisplay()):
                turnOnDisplay()
                updateGridDispay(prevRow, prevCol, currentRow, currentCol)
            if(currentStateIndex == finishStateIndex):
                break    
            maxRewardStateIndexList = [i for i, x in enumerate(dataGrid[currentStateIndex]) if x == max(dataGrid[currentStateIndex])]
            otherRewardStateIndexList = list(set(possibleActionIndex) - set(maxRewardStateIndexList))
            if(random.uniform(0, 1) <= epsilonGreedy and otherRewardStateIndexList):
                randomActionIndex = np.random.choice(possibleActionIndex, 1)[0]
            else:
                randomActionIndex = np.random.choice(maxRewardStateIndexList, 1)[0]
            prevRow = currentRow
            prevCol = currentCol
            prevStateIndex = currentStateIndex
            rowColStateString = actionGrid[currentStateIndex][randomActionIndex]
            currentRow, currentCol, currentStateIndex = getRowColState(rowColStateString)
            prevRewardValue = dataGrid[prevStateIndex][randomActionIndex]
            dataGrid[prevStateIndex][randomActionIndex] = rewardGrid[prevStateIndex] + discountFactor * (max(dataGrid[currentStateIndex]) + rewardGrid[currentStateIndex])
            if(prevRewardValue!=dataGrid[prevStateIndex][randomActionIndex]):
                isChanged = True
    
        print("Iteration : " + str(iterationNumber) + ", StepCount : " + str(stepCount))
        iterationCountList.append(iterationNumber)
        stepCountList.append(stepCount)
        iterationNumber += 1
        prevStepCount = stepCount
    
    plotGraph(iterationCountList, stepCountList)
    
setUpGrids()
qLearn()   
