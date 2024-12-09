def print_zigzag(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        if i % 2 == 0:  # even row: Moves from Left to Right
            for j in range(cols):
                print(matrix[i][j], end=" ")
        else:  # Odd row: Moves From Right to Left
            for j in range(cols - 1, -1, -1):
                print(matrix[i][j], end=" ")
        print() 


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


print("Zigzag pattern of the matrix:")
print_zigzag(matrix)
