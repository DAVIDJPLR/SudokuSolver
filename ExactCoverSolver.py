from __future__ import annotations
from math import sqrt
from typing import Generator

# standard node class which can link 4 directions and can carry a counter
class Node:
    def __init__(self, row: int, col: int, up: Node=None, down: Node=None, left: Node=None, right: Node=None, count: int=1):
        self.row = row
        self.col = col
        self.up = up or self
        self.down = down or self
        self.left = left or self
        self.right = right or self
        self.count = count
    
    # this def yields each of the node above a node
    def loopUp(self, excl: bool=True) -> Generator[Node,None,None]:
        itr = self
        if not excl: yield itr

        # loop until header is reached
        while itr.up != self:
            itr = itr.up
            yield itr

    # this def yields each of the node below a node
    def loopDown(self, excl: bool=True) -> Generator[Node,None,None]:
        itr = self
        if not excl: yield itr

        # loop until header is reached
        while itr.down != self:
            itr = itr.down
            yield itr

    # this def yields each of the nodes to the left of a node
    def loopLeft(self, excl: bool=True) -> Generator[Node,None,None]:
        itr = self
        if not excl: yield itr

        # loop until header is reached
        while itr.left != self:
            itr = itr.left
            yield itr

    # this def yields each of the nodes to the right of a node
    def loopRight(self, excl: bool=True) -> Generator[Node,None,None]:
        itr = self
        if not excl: yield itr

        # loop until header is reached
        while itr.right != self:
            itr = itr.right
            yield itr


# here we define the four sections that correspond to our four constraints in the matrix
# these constraints define the column in which the nodes will go

# this constraint is for the section that checks for exactly one number in each cell
def valConstraint(row: int) -> int: return int(row/9)

# this constraint corresponds to the section that checks that there's a 1-9 in each row
def rowConstraint(row:int) -> int: return 81 + 9*(int(row/81)) + row % 9

# this constraint corresponds to the section that checks that there's a 1-9 in each column
def colConstraint(row:int) -> int: return 2*81 + (row % 81)

# this constraint corresponds to the section that checks that there's a 1-9 in each box
def boxConstraint(row:int) -> int: return int(3*81 + (int(row/(3*81)))*(9*3) + ((int(row/(3*9))) % 3)*9 + (row % 9))

constraint_list = [valConstraint, rowConstraint, colConstraint, boxConstraint]
    

# this is the primary class for the dancing links matrix
class DLX:
    # constructor
    def __init__(self, board: list[int]):
        self.numRows = 9**3
        self.numCols = 9**2 * 4

        # create a frame for the matrix
        self.root = Node(-1, -1)
        self.colHeader: list[Node] = [Node(-1, i) for i in range(self.numCols)]
        self.rowHeader: list[Node] = [Node(i, -1) for i in range(self.numRows)]

        self.solved: bool = False

        # link the nodes in the row header (end nodes link to themselves rather than None)
        for i, node in enumerate(self.rowHeader):
            node.right = node
            node.left = node
            node.down = self.rowHeader[i+1] if i < self.numRows-1 else self.root
            node.up = self.rowHeader[i-1] if i > 0 else self.root

        # link the nodes in the column header (end nodes link to themselves rather than None)
        for i, node in enumerate(self.colHeader):
            node.up = node
            node.down = node
            node.right = self.colHeader[i+1] if i < self.numCols-1 else self.root
            node.left = self.colHeader[i-1] if i > 0 else self.root

        # link column and row readers to root (the corner node on the frame)
        self.root.right = self.colHeader[0]
        self.root.left  = self.colHeader[-1]
        self.root.down  = self.rowHeader[0]
        self.root.up    = self.rowHeader[-1]
                
        # fill in the DLX matrix given a certain sudoku board
        for i, cell in enumerate(board):
            # if the cell is empty add a row for all potential entries
            if cell == 0:
                for j in range(9):
                    # this formula is key for extracting necessary info
                    row = i*9+j
                    for constraint in constraint_list:
                        self.addNode(row, constraint(row))
            # node is full so just add one row defining the proper constraints
            else:
                row = i*9+cell-1
                for constraint in constraint_list:
                        self.addNode(row, constraint(row))


    def addNode(self, row: int, col: int):
        newNode: Node = Node(row, col)
        
        n = self.root
        for n in self.rowHeader[row].loopRight(excl=False):
            if n.right.col == -1 or n.right.col > col: break
        if n.col == col: return
        newNode.right      = n.right
        newNode.left       = n
        newNode.right.left = newNode
        n.right             = newNode

        for n in self.colHeader[col].loopDown(excl=False):
            if n.down.row == -1 or n.down.row > row: break
        newNode.down    = n.down
        newNode.up      = n
        newNode.down.up = newNode
        n.down           = newNode
        self.colHeader[col].count += 1

    def cover(self, node: Node) -> None:
        if node.col == -1: col = self.root
        else: col = self.colHeader[node.col]

        col.right.left = col.left
        col.left.right = col.right
        for col_itr in col.loopDown():
            for row_itr in col_itr.loopRight():
                row_itr.up.down = row_itr.down
                row_itr.down.up = row_itr.up

                if node.col == -1: row = self.root
                else: row = self.colHeader[node.col]
                row.count -= 1

    def uncover(self, node: Node) -> None:
        if node.col == -1: col = self.root
        else: col = self.colHeader[node.col]
        for col_itr in col.loopUp():
            for row_itr in col_itr.loopLeft():
                row_itr.up.down = row_itr
                row_itr.down.up = row_itr

                if node.col == -1: row = self.root
                else: row = self.colHeader[node.col]
                row.count += 1
        col.right.left = col
        col.left.right = col
    
    def search(self) -> list[int]:
        solutions = []
        
        def helper() -> bool:
            if self.is_empty():
                self.solved = True
                return True

            if self.is_empty(): return self.root
            minCol  = self.root.right
            minCount = self.root.right.count
            for col in self.root.loopRight():
                if col.count < minCount:
                    minCol  = col
                    minCount = col.count

            if minCol.count < 1 : return False

            for col_itr in minCol.loopDown():
                solutions.append(col_itr.row)
                for sol_node in col_itr.loopRight(excl=False):
                    if sol_node.col >= 0: self.cover(sol_node)

                if helper(): break

                solutions.pop()
                for sol_node in col_itr.left.loopLeft(excl=False):
                    if sol_node.col >= 0: self.uncover(sol_node)
            return self.solved

        helper()

        solution = [0] * 81
        for row in solutions:
            solution[int(row / 9)] = (row % 9) + 1

        mat: list[list[int]] = [[0 for i in range(9)] for i in range(9)]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                mat[r][c] = solution[9*r + c]
        
        return mat

    def is_empty(self) -> bool:
        return self.root.right == self.root