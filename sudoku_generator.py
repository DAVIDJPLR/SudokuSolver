# !/usr/bin/python
import sys
from Sudoku.Generator import *
from ExactCoverSolver import DLX

def matrix_to_board(lst: list[list[int]]):
    b = Board()
    for row in range(0, len(lst)):
        for col in range(0, len(lst[0])):
            b.rows[row][col].value = lst[row][col]
    return b

# setting difficulties and their cutoffs for each solve method
difficulties = {
    'easy': (35, 0), 
    'medium': (81, 5), 
    'hard': (81, 10), 
    'extreme': (81, 15)
}

# getting desired difficulty from command line
difficulty = difficulties[sys.argv[2]]

# constructing generator object from puzzle file (space delimited columns, line delimited rows)
gen = Generator(sys.argv[1])

# applying 100 random transformations to puzzle
gen.randomize(100)

# getting a copy before slots are removed
initial = gen.board.copy()

# applying logical reduction with corresponding difficulty cutoff
gen.reduce_via_logical(difficulty[0])

# catching zero case
if difficulty[1] != 0:
    # applying random reduction with corresponding difficulty cutoff
    gen.reduce_via_random(difficulty[1])


# getting copy after reductions are completed
final = gen.board.copy()

# printing out complete board (solution)
# print("The initial board before removals was: \r\n\r\n{0}\n\n".format(initial))

# printing out board after reduction
print("Unsolved board: \r\n\r{0}\n\n".format(final))

sol = matrix_to_board(DLX(final.get_list()).search())

print("Solution: \r\n\r\n{0}\n\n".format(sol))