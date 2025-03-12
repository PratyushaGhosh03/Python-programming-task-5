def is_valid_sudoku(grid):
    def is_valid_unit(unit):
        unit = [num for num in unit if num != 0]
        return len(unit) == len(set(unit))

    for row in grid:
        if not is_valid_unit(row):
            return False

    for col in zip(*grid):
        if not is_valid_unit(col):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_unit(square):
                return False

    return True

# Example usage
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print(is_valid_sudoku(sudoku_grid))
