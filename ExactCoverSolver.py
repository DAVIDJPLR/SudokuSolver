from __future__ import annotations
from math import sqrt

class Node:
    def __init__(self, row: int, col: int, up: Node=None, down: Node=None, left: Node=None, right: Node=None, count: int=1):
        self.row    = row
        self.col    = col
        self.up     = up
        self.down   = down
        self.left   = left
        self.right  = right
        self.count  = count

    def getCoords(self):
        return (self.row, self.col)
    

def _one_constraint(row: int, dim:int) -> int:
    return row//dim
def _row_constraint(row:int, dim:int) -> int:
    return dim**2 + dim*(row//(dim**2)) + row % dim
def _col_constraint(row:int, dim:int) -> int:
    return 2*(dim**2) + (row % (dim**2))
def _box_constraint(row:int, dim:int) -> int:
    return int(3*(dim**2) + (row//(sqrt(dim)*dim**2))*(dim*sqrt(dim)) + ((row//(sqrt(dim)*dim)) % sqrt(dim))*dim + (row % dim))
constraint_list = [_one_constraint, _row_constraint, _col_constraint, _box_constraint]
    

class DLX:
    def __init__(self, board: list[int], dim: int):
        self.numRows = dim**3
        self.numCols = dim**2 * 4
        self.root = Node(-1, -1)
        self.colHeader: list[Node] = [Node(-1, i) for i in range(self.numCols)]
        self.rowHeader: list[Node] = [Node(i, -1) for i in range(self.numRows)]

        for i, node in enumerate(self.rowHeader):
            node.right = node
            node.left  = node
            node.down  = self.rowHeader[i+1] if i < self.numRows-1 else self.root
            node.up    = self.rowHeader[i-1] if i > 0 else self.root
        for i, node in enumerate(self.colHeader):
            node.up    = node
            node.down  = node
            node.right = self.colHeader[i+1] if i < self.numCols-1 else self.root
            node.left  = self.colHeader[i-1] if i > 0 else self.root

        self.root.right = self.cols[0]
        self.root.left  = self.cols[-1]
        self.root.down  = self.rows[0]
        self.root.up    = self.rows[-1]
                
        #iterate through puzzle
        for i, cell in enumerate(board):
            if cell == 0: # if cell is unassigned
                # populate all rows representing cadidate values for this cell
                for j in range(dim):
                    row = i*dim+j
                    for constraint in constraint_list:
                        self.insert_node(row, constraint(row, dim))
            else: # if cell is assigned
                # populate the row representing the assigned value for this cell
                row = i*dim+cell-1
                for constraint in constraint_list:
                        self.insert_node(row, constraint(row, dim))

    def insert_node(self, row: int, col: int):
        assert(row >=0 and col >= 0 and row < len(self.rows) and col < len(self.cols))
        # create node to insert
        new_node: Node = Node(self, row, col)
        
        # iterate through the row to find correct placement of new_node in row
        n = self.root
        for n in self.rows[row].itr_right(excl=False):
            if n.right.col == -1 or n.right.col > col: break
        if n.col == col: return # if node already exists, leave
        # reassign left and right pointers
        new_node.right      = n.right
        new_node.left       = n
        new_node.right.left = new_node
        n.right             = new_node

        # iterate through the column to find correct placement of new_node in col
        for n in self.cols[col].itr_down(excl=False):
            if n.down.row == -1 or n.down.row > row: break
        # reassign up and down pointers
        new_node.down    = n.down
        new_node.up      = n
        new_node.down.up = new_node
        n.down           = new_node
        self.cols[col].count += 1
