import random
from BacktrackSearch import *

def generateGame(difficulty: int):
    # 4 difficulty levels (1-4)
    numValuesOpen: int

    if (difficulty == 1):
        numValuesOpen = 40
    elif (difficulty == 2):
        numValuesOpen = 48
    elif (difficulty == 3):
        numValuesOpen = 52
    elif (difficulty == 4):
        numValuesOpen = 59
    else:
        print("difficulty level must be betwwen 1 and 4")
        return
    
    print(numValuesOpen)

    # Create an empty grid (9x9)
    emptyGame = [[0 for i in range(9)] for x in range(9)]

    # Fill in the larger diagonals (the top lef 3x3, middle 3x3 and bottom right 3x3)
    # these squares 3x3 squares don't interact with each other on the lines or columns so
    # we can just fill them with random numbers as long as they dont repeat
    for i in range (0, 9, 3):
        possibleValues = list(range(1, 10))
        random.shuffle(possibleValues)
        for x in range(3):
            for y in range(3):
                emptyGame[i+x][i+y] = possibleValues.pop()

    # Print current boad just for testing purposes
    print("============================")
    printGame(emptyGame)
    print("============================")

    solvedGame = backtrack(emptyGame)
    solvableGame = removeValues(solvedGame, numValuesOpen)
    return solvableGame

def removeValues(game, numEmpty):
    for i in range(numEmpty):
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        while (game[row][column] == 0):
            row = random.randint(0, 8)
            column = random.randint(0, 8)
        game[row][column] = 0
    return game

def printGame(game):
    for row in game:
        print(" ".join(map(str, row)))

def main():
    printGame(generateGame(1))

# Example usage: generate a Sudoku with 40 open squares
main()
