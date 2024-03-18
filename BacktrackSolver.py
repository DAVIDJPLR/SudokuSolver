import sys
from GenerateSudoku import *
from BacktrackSolver import *
from Sudoku.Generator import *

def runBacktrack(difficultylevel, verbosity: int):
    unsolved: Board = generateSudoku(difficultylevel)

    results = backtrack(unsolved, verbosity)
    solved = results[0]
    visitedNodes = results[1]
    openVals = results[2]

    totalNodesExplored = results[1]
    ratio = totalNodesExplored/openVals
    totalNodes_Opens = ratio

    if verbosity == 2:
        print("=====================================")
        print(str(totalNodesExplored) + " nodes were visited")
        print(str(openVals) + " open squares in the starting state")
        print(str(totalNodes_Opens) + " = (# nodes visited)/(# of open squares in starting state)")
        print("=====================================")

def backtrack(board: Board, verbosity: int):
    numOpenVals = len(board.get_unused_cells())
    nodesVisited = [0]

    print("The original unsolved sudoku puzzle is: \r\r\n{0}".format(board) + "\n")

    def solve():
        openCells = board.get_unused_cells()
        if len(openCells) == 0:
            return True
        cell = openCells[0]
        for number in range(1, 10):
            if valid(board, cell, number):
                nodesVisited[0] += 1
                cell.value = number
                
                if verbosity == 3:
                    print("Changing value of (" + str(cell.row) + "," + str(cell.col) + ") to " + str(number) + ": \r\r\n{0}".format(board) + "\n")

                if solve():
                    return True
                cell.value = 0

                if verbosity == 3:
                    print("Backtracking and changing value of (" + str(cell.row) + "," + str(cell.col) + ") back to " + str(0) + ": \r\r\n{0}".format(board) + "\n")
        return False
    solve() 

    print("The solved sudoku puzzule is: \r\r\n{0}".format(board) + "\n")

    return [board, nodesVisited[0], numOpenVals]

def valid(board: Board, cell: Cell, number: int):
    rowValues = board.rows[cell.row]
    for value in rowValues:
        if value.value == number:
            return False
            
    colValues = board.columns[cell.col]
    for value in colValues:
        if value.value == number:
            return False
            
    boxValues = board.boxes[cell.box]
    for value in boxValues:
        if value.value == number:
            return False
            
    return True