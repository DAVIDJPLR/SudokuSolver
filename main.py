import sys
from GenerateSudoku import *
from BacktrackSolver import *


print("easy -- results")
totalNodesExplored = 0
totalNodes_Opens = 0

for i in range(8):
    unsolved: Board = generateSudoku('easy')

    results = backtrack(unsolved)
    solved = results[0]
    visitedNodes = results[1]
    openVals = results[2]

    totalNodesExplored += results[1]
    ratio = results[1]/results[2]
    totalNodes_Opens += ratio

avgNodesVisited = totalNodesExplored/7
avgRatio = totalNodes_Opens/7

print(str(avgNodesVisited) + " nodes visited on average")
print(str(avgRatio) + " nodes visited/open nodes on average")
print("=====================================")


print("medium -- results")
totalNodesExplored = 0
totalNodes_Opens = 0

for i in range(8):
    unsolved: Board = generateSudoku('medium')

    results = backtrack(unsolved)
    solved = results[0]
    visitedNodes = results[1]
    openVals = results[2]

    totalNodesExplored += results[1]
    ratio = results[1]/results[2]
    totalNodes_Opens += ratio

avgNodesVisited = totalNodesExplored/7
avgRatio = totalNodes_Opens/7

print(str(avgNodesVisited) + " nodes visited on average")
print(str(avgRatio) + " nodes visited/open nodes on average")
print("=====================================")


print("hard -- results")
totalNodesExplored = 0
totalNodes_Opens = 0

for i in range(8):
    unsolved: Board = generateSudoku('hard')

    results = backtrack(unsolved)
    solved = results[0]
    visitedNodes = results[1]
    openVals = results[2]

    totalNodesExplored += results[1]
    ratio = results[1]/results[2]
    totalNodes_Opens += ratio

avgNodesVisited = totalNodesExplored/7
avgRatio = totalNodes_Opens/7

print(str(avgNodesVisited) + " nodes visited on average")
print(str(avgRatio) + " nodes visited/open nodes on average")
print("=====================================")


print("extreme -- results")
totalNodesExplored = 0
totalNodes_Opens = 0

for i in range(8):
    unsolved: Board = generateSudoku('extreme')

    results = backtrack(unsolved)
    solved = results[0]
    visitedNodes = results[1]
    openVals = results[2]

    totalNodesExplored += results[1]
    ratio = results[1]/results[2]
    totalNodes_Opens += ratio

avgNodesVisited = totalNodesExplored/7
avgRatio = totalNodes_Opens/7

print(str(avgNodesVisited) + " nodes visited on average")
print(str(avgRatio) + " nodes visited/open nodes on average")
print("=====================================")

