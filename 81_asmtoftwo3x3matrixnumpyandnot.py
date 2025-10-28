# Question: Write python code to perform addition, subtraction, multiplication and transpose of two 3x3 matrix:
# · With NumPy

# NumPy makes matrix math incredibly easy and fast!
import numpy as np

# Define the two 3x3 matrices using NumPy's array function
matrix_A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix_B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("--- Original Matrices (NumPy Arrays) ---")
print("Matrix A:\n", matrix_A)
print("Matrix B:\n", matrix_B)

# --- 1. Addition (Simple + operator) ---
addition_result = matrix_A + matrix_B
print("\n--- Result of A + B (Addition) ---")
print(addition_result)

# --- 2. Subtraction (Simple - operator) ---
subtraction_result = matrix_A - matrix_B
print("\n--- Result of A - B (Subtraction) ---")
print(subtraction_result)

# --- 3. Multiplication (Use .dot() or @ for actual Matrix Product) ---
# NOTE: matrix_A * matrix_B performs element-wise multiplication, 
# but matrix_A @ matrix_B or np.dot(A, B) performs true matrix multiplication.
multiplication_result = matrix_A @ matrix_B
print("\n--- Result of A * B (True Matrix Multiplication) ---")
print(multiplication_result)

# --- 4. Transpose (Use .T or np.transpose()) ---
transpose_A = matrix_A.T
transpose_B = matrix_B.T
print("\n--- Result of A^T (Transpose of A) ---")
print(transpose_A)
print("\n--- Result of B^T (Transpose of B) ---")
print(transpose_B)

# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
# Question: Write python code to perform addition, subtraction, multiplication and transpose of two 3x3 matrix:
# · Without NumPy

# Define the two 3x3 matrices (lists of lists)
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

N = 3 # Matrix size (3x3)

def print_matrix(matrix, title):
    """Helper to display the matrix."""
    print(f"\n--- {title} ---")
    for row in matrix:
        print(row)

# --- 1. Addition, Subtraction, and Transpose Logic ---
# These all use simple element-wise operations (or simple swapping for Transpose)
def perform_element_wise_op(mat1, mat2, operation):
    """Performs addition or subtraction."""
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if operation == '+':
                result[i][j] = mat1[i][j] + mat2[i][j]
            elif operation == '-':
                result[i][j] = mat1[i][j] - mat2[i][j]
    return result

def matrix_transpose(mat):
    """Swaps rows and columns."""
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][i] = mat[i][j] # The core swap
    return result

# --- 2. Multiplication Logic (The complicated one) ---
def matrix_multiplication(mat1, mat2):
    """Performs true matrix multiplication."""
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N): # Row of result
        for j in range(N): # Column of result
            for k in range(N): # The intermediate loop for sum of products
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

# --- EXECUTION ---

print("Original Matrices:")
print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")

print_matrix(perform_element_wise_op(A, B, '+'), "A + B (Addition)")
print_matrix(perform_element_wise_op(A, B, '-'), "A - B (Subtraction)")
print_matrix(matrix_multiplication(A, B), "A * B (Multiplication)")
print_matrix(matrix_transpose(A), "A^T (Transpose)")
print_matrix(matrix_transpose(B), "B^T (Transpose)")

# ----------------------------------------------------------------------
# this program was written and executed by Mannan Tayal (0231bca047)
