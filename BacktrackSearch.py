def backtrack(unsolvedGame):
    return [[0 for i in range(9)] for x in range(9)]

    def valid(row, column, value):
        for i in range(9):
            if game[row][i] == num:
                return False
            
        for i in range(9):
            if game[i][column] == num:
                return False

        


