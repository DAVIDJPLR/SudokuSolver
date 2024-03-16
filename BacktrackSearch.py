def backtrack(game):
    def solve():
        row, column = findOpenBlock(game)
        if row is None:
            return True
        for value in range(1, 10):
            if valid(game, row, column, value):
                game[row][column] = value
                if solve():
                    return True
                game[row][column] = 0
        return False
            

def valid(game, row, column, value):
        for i in range(9):
            if game[row][i] == value:
                return False
            
        for i in range(9):
            if game[i][column] == value:
                return False
            
        startingRow = 3 * (row//3)
        startingColumn = 3 * (column//3)
        for i in range(3):
            for x in range(3):
                if game[startingRow+i][startingColumn+x] == value:
                    return False
        return True

def findOpenBlock(game):
    for row in range(9):
        for column in range(9):
            if game[row][column] == 0:
                return row, column
    return None, None

