# Question: Write python code to print addition, subtraction, multiplication and transpose of two 3x3 matrix.

# Define the two 3x3 matrices as lists of lists (nested lists)
# Matrix A
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# Matrix B
B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

ROWS = 3
COLS = 3

def print_matrix(matrix, title):
    """Helper function to print a matrix with a title clearly."""
    print(f"\n--- {title} ---")
    for row in matrix:
        # We use f-strings and list comprehension to neatly print each row
        print([f"{x:3}" for x in row])

# --- 1. MATRIX ADDITION (A + B) ---
def matrix_addition(mat1, mat2):
    """Adds two matrices element by element."""
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    
    for i in range(ROWS):
        for j in range(COLS):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result

# --- 2. MATRIX SUBTRACTION (A - B) ---
def matrix_subtraction(mat1, mat2):
    """Subtracts two matrices element by element."""
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    
    for i in range(ROWS):
        for j in range(COLS):
            result[i][j] = mat1[i][j] - mat2[i][j]
    return result

# --- 3. MATRIX MULTIPLICATION (A * B) ---
def matrix_multiplication(mat1, mat2):
    """Multiplies two matrices."""
    # The result matrix is initialized with zeros
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    
    for i in range(ROWS): # iterate through rows of A
        for j in range(COLS): # iterate through columns of B
            for k in range(COLS): # iterate through rows of B / columns of A
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

# --- 4. MATRIX TRANSPOSE (A^T and B^T) ---
def matrix_transpose(mat):
    """Swaps rows and columns of a matrix."""
    # The result matrix is initialized with zeros
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    
    for i in range(ROWS):
        for j in range(COLS):
            # Swap the indices: element at [i][j] in original goes to [j][i] in transpose
            result[j][i] = mat[i][j]
    return result

# --- EXECUTION ---

print("Original Matrices:")
print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")

# Calculate and print results
print_matrix(matrix_addition(A, B), "Result of A + B (Addition)")
print_matrix(matrix_subtraction(A, B), "Result of A - B (Subtraction)")
print_matrix(matrix_multiplication(A, B), "Result of A * B (Multiplication)")
print_matrix(matrix_transpose(A), "Result of A^T (Transpose of A)")
print_matrix(matrix_transpose(B), "Result of B^T (Transpose of B)")

# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
