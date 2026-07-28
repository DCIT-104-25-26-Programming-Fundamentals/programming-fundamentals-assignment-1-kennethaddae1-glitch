# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, label=""):
    print(f"Enter matrix {label} ({rows}x{cols}), each row space-separated:")
    matrix = []
    for r in range(rows):
        row = list(map(float, input(f"Enter row {r + 1}: ").split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(val) for val in row))


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result


def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(a[r][c] + b[r][c])
        result.append(new_row)
    return result


def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = []
    for r in range(rows_a):
        new_row = []
        for c in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[r][k] * b[k][c]
            new_row.append(total)
        result.append(new_row)
    return result


if __name__ == "__main__":
    
    print("=== PART A: Transpose ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix_a = read_matrix(rows, cols)
    print("\nOriginal Matrix:")
    print_matrix(matrix_a)
    print("\nTransposed Matrix:")
    print_matrix(transpose_matrix(matrix_a))

    
    print("\n=== PART B: Addition ===")
    rows_b = int(input("Enter number of rows: "))
    cols_b = int(input("Enter number of columns: "))
    matrix_b1 = read_matrix(rows_b, cols_b, "1")
    matrix_b2 = read_matrix(rows_b, cols_b, "2")
    print("\nSum:")
    print_matrix(add_matrices(matrix_b1, matrix_b2))

    
    print("\n=== PART C: Multiplication ===")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))
    matrix_c1 = read_matrix(m, n, "A")
    matrix_c2 = read_matrix(n, p, "B")
    print("\nProduct A x B:")
    print_matrix(multiply_matrices(matrix_c1, matrix_c2))