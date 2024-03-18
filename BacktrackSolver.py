from Sudoku.Generator import *
def backtrack(board: Board):
    numOpenVals = len(board.get_unused_cells())
    nodesVisited = [0]
    def solve():
        openCells = board.get_unused_cells()
        if len(openCells) == 0:
            return True
        cell = openCells[0]
        for number in range(1, 10):
            if valid(board, cell, number):
                nodesVisited[0] += 1
                cell.value = number
                if solve():
                    return True
                cell.value = 0
        return False
    solve()  
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