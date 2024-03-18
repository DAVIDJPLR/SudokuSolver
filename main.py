import sys
from GenerateSudoku import *
from BacktrackSolver import *

try:
    algo = sys.argv[1]
    difficulty = sys.argv[2]
    verbosity = int(sys.argv[3])

    if (algo == "backtrack"):
        runBacktrack(difficulty, verbosity)
    elif (algo == "exactcover"):
        print("exactcover")
    else:
        print("Incorrect arguments, usage example: py main.py algorithm difficulty verbosity")
        print("algorithm usages: backtrack, exactcover")
        print("difficulty usages: easy, medium, hard, extreme")
        print("verbosity usages: 1, 2, 3")
except:
    print("Incorrect arguments, usage example: py main.py algorithm difficulty verbosity")
    print("algorithm usages: backtrack, exactcover")
    print("difficulty usages: easy, medium, hard, extreme")
    print("verbosity usages: 1, 2, 3")

# print("easy -- results")
# totalNodesExplored = 0
# totalNodes_Opens = 0

# for i in range(8):
#     unsolved: Board = generateSudoku('easy')

#     results = backtrack(unsolved)
#     solved = results[0]
#     visitedNodes = results[1]
#     openVals = results[2]

#     totalNodesExplored += results[1]
#     ratio = results[1]/results[2]
#     totalNodes_Opens += ratio

# avgNodesVisited = totalNodesExplored/7
# avgRatio = totalNodes_Opens/7

# print(str(avgNodesVisited) + " nodes visited on average")
# print(str(avgRatio) + " nodes visited/open nodes on average")
# print("=====================================")


# print("medium -- results")
# totalNodesExplored = 0
# totalNodes_Opens = 0

# for i in range(8):
#     unsolved: Board = generateSudoku('medium')

#     results = backtrack(unsolved)
#     solved = results[0]
#     visitedNodes = results[1]
#     openVals = results[2]

#     totalNodesExplored += results[1]
#     ratio = results[1]/results[2]
#     totalNodes_Opens += ratio

# avgNodesVisited = totalNodesExplored/7
# avgRatio = totalNodes_Opens/7

# print(str(avgNodesVisited) + " nodes visited on average")
# print(str(avgRatio) + " nodes visited/open nodes on average")
# print("=====================================")


# print("hard -- results")
# totalNodesExplored = 0
# totalNodes_Opens = 0

# for i in range(8):
#     unsolved: Board = generateSudoku('hard')

#     results = backtrack(unsolved)
#     solved = results[0]
#     visitedNodes = results[1]
#     openVals = results[2]

#     totalNodesExplored += results[1]
#     ratio = results[1]/results[2]
#     totalNodes_Opens += ratio

# avgNodesVisited = totalNodesExplored/7
# avgRatio = totalNodes_Opens/7

# print(str(avgNodesVisited) + " nodes visited on average")
# print(str(avgRatio) + " nodes visited/open nodes on average")
# print("=====================================")


# print("extreme -- results")
# totalNodesExplored = 0
# totalNodes_Opens = 0

# for i in range(8):
#     unsolved: Board = generateSudoku('extreme')

#     results = backtrack(unsolved)
#     solved = results[0]
#     visitedNodes = results[1]
#     openVals = results[2]

#     totalNodesExplored += results[1]
#     ratio = results[1]/results[2]
#     totalNodes_Opens += ratio

# avgNodesVisited = totalNodesExplored/7
# avgRatio = totalNodes_Opens/7

# print(str(avgNodesVisited) + " nodes visited on average")
# print(str(avgRatio) + " nodes visited/open nodes on average")
# print("=====================================")

