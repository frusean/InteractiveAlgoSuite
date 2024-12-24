#Name:Rusean Francis
#ID:2101012160

import pygame
import sys

# --- Interactive N-Queens (Drag and Drop) ---

# Check if placing a queen at a given row and column is safe
# This ensures no two queens threaten each other
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
                abs(board[i] - col) == abs(i - row):  # Check for diagonal conflicts
            return False
    return True

# Solve the N-Queens problem for a given board size (n)
# This function uses backtracking to find a valid solution
def solve_n_queens(n):
    def backtrack(board, row):
        if row == n:  # If all queens are placed, return success
            return True
        for col in range(n):  # Try placing a queen in each column
            if is_safe(board, row, col):  # Check if it's safe
                board[row] = col  # Place the queen
                if backtrack(board, row + 1):  # Recurse to place the next queen
                    return True
                board[row] = -1  # Backtrack and remove the queen
        return False

    board = [-1] * n  # Initialize an empty board with no queens
    backtrack(board, 0)  # Start solving from the first row
    return board

# Solve a partial N-Queens problem, starting from a given row
# This is used for dynamic adjustments during interactions
def solve_n_queens_partial(n, board, start_row):
    def backtrack(board, row):
        if row == n:  # If all rows are processed, return success
            return True
        for col in range(n):  # Try placing a queen in each column
            if is_safe(board, row, col):  # Check if it's safe
                board[row] = col  # Place the queen
                if backtrack(board, row + 1):  # Recurse to the next row
                    return True
                board[row] = -1  # Backtrack
        return False

    # Reset all rows below the starting row to allow new placements
    for row in range(start_row, n):
        board[row] = -1
    backtrack(board, start_row)  # Solve starting from start_row

# Visualization of the N-Queens problem with drag-and-drop functionality
def visualize_n_queens_interactive(n):
    pygame.init()
    size = 60  # Size of each square on the chessboard
    screen = pygame.display.set_mode((n * size, n * size))
    pygame.display.set_caption("Interactive N-Queens Visualization")
    clock = pygame.time.Clock()

    colors = [(255, 255, 255), (0, 0, 0)]  # Alternating colors for the chessboard
    queen_image = pygame.image.load("queen.png")  # Load the queen image
    queen_image = pygame.transform.scale(queen_image, (size, size))

    # Get the initial solution to the problem
    board = solve_n_queens(n)

    dragging = False  # Track whether the user is dragging a queen
    drag_row, drag_col = -1, -1  # Coordinates of the dragged queen

    def reset_board():
        nonlocal board
        board = solve_n_queens(n)  # Reset the board to a new solution

    while True:
        screen.fill((0, 0, 0))  # Clear the screen for redraw

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit the game
                pygame.quit()
                sys.exit()

            # Handle mouse events for dragging queens
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col, row = x // size, y // size
                if 0 <= row < n and board[row] == col:  # Check if a queen is clicked
                    dragging = True
                    drag_row, drag_col = row, col
                    board[row] = -1  # Temporarily remove the queen

            if event.type == pygame.MOUSEBUTTONUP and dragging:
                x, y = pygame.mouse.get_pos()
                col, row = x // size, y // size
                if 0 <= row < n and 0 <= col < n and is_safe(board, row, col):
                    backup_board = board[:]
                    board[row] = col  # Place the queen at the new position
                    solve_n_queens_partial(n, board, row + 1)  # Adjust solution dynamically
                    if board != backup_board:
                        dragging = False
                    else:  # Restore the original position if no solution
                        board[drag_row] = drag_col
                        dragging = False
                else:
                    board[drag_row] = drag_col  # Restore the original position
                    dragging = False

            # Reset the board if 'R' is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_board()

        # Draw the chessboard and queens
        for row in range(n):
            for col in range(n):
                color = colors[(row + col) % 2]  # Alternate colors for each square
                pygame.draw.rect(screen, color, (col * size, row * size, size, size))
                if board[row] == col:  # Draw a queen if present
                    screen.blit(queen_image, (col * size, row * size))

        # If a queen is being dragged, draw it under the mouse cursor
        if dragging:
            x, y = pygame.mouse.get_pos()
            screen.blit(queen_image, (x - size // 2, y - size // 2))

        # Display reset instructions
        font = pygame.font.SysFont("Arial", 24)
        reset_text = font.render("Press 'R' to reset", True, (255, 255, 255))
        text_rect = reset_text.get_rect(center=(n * size // 2, n * size - 30))
        pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(20, 10))
        screen.blit(reset_text, text_rect)

        pygame.display.flip()  # Refresh the display

        clock.tick(30)  # Cap the frame rate at 30 FPS

# --- Backtracking N-Queens Solver (Static) ---

# Solve N-Queens using backtracking and store all solutions
def solve_n_queens_backtracking(n):
    def is_safe(board, row, col):
        for i in range(row):  # Check for conflicts in columns and diagonals
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row, solutions):
        if row == n:  # A complete solution is found
            solutions.append(board[:])  # Add it to the list of solutions
            return
        for col in range(n):  # Try placing a queen in each column
            if is_safe(board, row, col):
                board[row] = col  # Place the queen
                backtrack(board, row + 1, solutions)  # Recurse to the next row
                board[row] = -1  # Backtrack

    board = [-1] * n  # Initialize the board
    solutions = []  # List to store all solutions
    backtrack(board, 0, solutions)
    return solutions

# Visualize the static N-Queens solutions one by one
def visualize_n_queens_backtracking(n, solutions):
    pygame.init()
    size = 60  # Size of each square
    screen = pygame.display.set_mode((n * size, n * size))
    pygame.display.set_caption("N-Queens Visualization")
    clock = pygame.time.Clock()

    colors = [(255, 255, 255), (0, 0, 0)]  # Board colors
    queen_image = pygame.image.load("queen.png")
    queen_image = pygame.transform.scale(queen_image, (size, size))

    for solution in solutions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for row in range(n):
            for col in range(n):
                color = colors[(row + col) % 2]
                pygame.draw.rect(screen, color, (col * size, row * size, size, size))
                if solution[row] == col:
                    screen.blit(queen_image, (col * size, row * size))

        pygame.display.flip()
        clock.tick(1)  # Show each solution for 1 second

# --- Main Menu for Selection ---

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Select Algorithm")
    font = pygame.font.SysFont("Arial", 30)
    clock = pygame.time.Clock()

    # Render options for the user
    option1_text = font.render("1. Interactive Backtracking N-Queens", True, (255, 255, 255))
    option2_text = font.render("2. Backtracking N-Queens", True, (255, 255, 255))

    option1_rect = option1_text.get_rect(center=(200, 100))
    option2_rect = option2_text.get_rect(center=(200, 200))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(option1_text, option1_rect)
        screen.blit(option2_text, option2_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if option1_rect.collidepoint(event.pos):
                    return 'interactive'
                elif option2_rect.collidepoint(event.pos):
                    return 'backtracking'

        pygame.display.flip()
        clock.tick(30)

# --- Run the Selected Option ---

def run_selected_option():
    n = 8  # Default board size
    user_choice = main_menu()  # Get the user's choice

    if user_choice == 'interactive':
        visualize_n_queens_interactive(n)
    elif user_choice == 'backtracking':
        solutions = solve_n_queens_backtracking(n)
        visualize_n_queens_backtracking(n, solutions)

# Run the program
run_selected_option()

# --- Time Complexity Analysis ---
# The backtracking algorithm for the N-Queens problem has a worst-case time complexity of O(N!),
# where N is the size of the chessboard (or the number of queens). Here's how this complexity is calculated:
#
# 1. Exploring Row and Column Combinations:**
#    - For the first row, there are N possible columns where a queen can be placed.
#    - For the second row, there are at most N-1 valid columns (considering no conflicts with the first queen).
#    - Similarly, the third row will have at most N-2 valid columns, and so on.
#    - This results in a total of N × (N-1) × (N-2) ... × 1 = N! possible configurations.
#
# 2. Pruning Invalid Configurations:**
#    - The `is_safe` function helps prune configurations that have conflicts early, reducing unnecessary exploration.
#    - However, in the worst case, the algorithm may still explore all valid configurations before finding a solution.
#
# 3. Practical Efficiency:**
#    - For small values of N (e.g., N <= 15), this backtracking approach is efficient and feasible.
#    - For larger values of N, the exponential growth makes solving the problem computationally expensive.
#
# --- Optimizations to Improve Efficiency ---
# The following optimizations can make the algorithm significantly faster in practice:
#
# 1. Efficient Conflict Checking:**
#    - Instead of iterating through all previous rows to check for conflicts, use three additional arrays:
#      - `columns`: Tracks which columns are occupied.
#      - `main_diagonal`: Tracks the main diagonals (row - col).
#      - `anti_diagonal`: Tracks the anti-diagonals (row + col).
#    - These arrays allow conflict checks to be performed in O(1) time, instead of O(row).
#
# 2. Symmetry Reduction:**
#    - For boards with symmetrical solutions, solve for one half of the board and mirror the results.
#    - For example, if a solution exists for column placements in the left half, the right half can be mirrored.
#    - This reduces the number of configurations explored by almost half.
#
# 3. Dynamic Column Ordering (Heuristics):**
#    - Use heuristics to decide the order of column exploration. For example, try columns with the fewest conflicts first.
#    - This prioritization can reduce the recursion depth, as promising branches are explored earlier.
#
# 4. Early Stopping with Constraints:**
#    - If a row cannot be solved due to existing conflicts, terminate the search for that branch immediately.
#    - This avoids wasting time exploring impossible configurations.
#
# 5. Parallelization:
#    - Split the work by fixing the queen in the first row for each column and solving the remaining subproblems independently.
#    - These subproblems can be solved in parallel on separate processors, significantly speeding up computation.
#
# 6. Precomputation for Common Cases:
#    - For commonly solved board sizes (e.g., N=8), store the solutions in a database or cache.
#    - This allows these cases to be returned instantly without recomputing them.
#
# --- Practical Impact of Optimizations ---
# While these optimizations do not change the worst-case complexity of O(N!), they significantly reduce the runtime for most practical cases:
# - Efficient conflict checking eliminates unnecessary iterations.
# - Symmetry reduction cuts the search space in half or more.
# - Heuristics and early stopping help the algorithm focus on valid and promising configurations.
# - Parallelization allows larger board sizes to be handled more effectively.
#
# With these optimizations, the backtracking algorithm becomes much faster and more practical for solving larger N-Queens problems.
