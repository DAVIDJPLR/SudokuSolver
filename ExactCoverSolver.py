class ExactCoverSolver:
    def __init__(self, sudoku_grid):
        self.sudoku_grid = sudoku_grid
        self.size = 9  # Size of the Sudoku grid
        self.solution = None

    def solve(self):
        self.solution = None
        exact_cover_matrix = self.create_exact_cover_matrix()
        partial_solution = []
        self.algorithm_x(exact_cover_matrix, partial_solution)
        return self.solution

    def create_exact_cover_matrix(self):
        # Create an empty matrix filled with 0s
        matrix = [[0] * (4 * self.size ** 2) for _ in range(9 * self.size ** 2)]

        # Fill in the matrix based on the Sudoku grid
        for i in range(self.size):
            for j in range(self.size):
                value = self.sudoku_grid[i][j]
                if value != 0:
                    self.cover(matrix, i, j, value)

        return matrix

    def cover(self, matrix, row, col, value):
        for i in range(self.size):
            matrix[row * self.size + col][i] = 0
            matrix[self.size ** 2 + row * self.size + value - 1][i] = 0
            matrix[2 * self.size ** 2 + col * self.size + value - 1][i] = 0
            matrix[3 * self.size ** 2 + (row // 3 * 3 + col // 3) * self.size + value - 1][i] = 0

        matrix[row * self.size + col][row * self.size + col] = 1

    def algorithm_x(self, matrix, partial_solution):
        if not matrix:
            self.solution = [row // self.size + 1 for row in partial_solution]
            return

        col = min(range(len(matrix[0])), key=lambda c: sum(matrix[r][c] for r in range(len(matrix))))
        for row in [r for r in range(len(matrix)) if matrix[r][col] == 1]:
            partial_solution.append(row)
            cols = self.cover_columns(matrix, row)
            self.algorithm_x(matrix, partial_solution)
            self.uncover_columns(matrix, row, cols)
            partial_solution.pop()

    def cover_columns(self, matrix, row):
        cols = []
        for c in range(len(matrix[0])):
            if matrix[row][c] == 1:
                for r in range(len(matrix)):
                    if matrix[r][c] == 1:
                        for i in range(len(matrix[0])):
                            matrix[r][i] = 0
                cols.append(c)
        return cols

    def uncover_columns(self, matrix, row, cols):
        for c in cols:
            for r in range(len(matrix)):
                if matrix[r][c] == 1:
                    for i in range(len(matrix[0])):
                        matrix[r][i] = 1

    def print_solution(self):
        if self.solution:
            for i in range(self.size):
                print(self.solution[i*self.size:(i+1)*self.size])
        else:
            print("No solution found.")
