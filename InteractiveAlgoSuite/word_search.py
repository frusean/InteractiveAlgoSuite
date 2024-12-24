#Name:Rusean Francis
#ID:2101012160
import tkinter as tk
from tkinter import messagebox, filedialog


class WordSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Search Solver")  # Set the application title
        self.root.geometry("700x650")  # Define the window size
        self.root.config(bg="#f0f4f8")  # Set the background color of the application

        # Variable to store the last highlighted path on the grid
        self.last_found_path = None

        # Create the main frame for the application's layout
        self.main_frame = tk.Frame(root, bg="#f0f4f8")
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Add a help button with a blue question mark for user instructions
        self.help_button = tk.Button(self.main_frame, text="❓", font=("Arial", 16, "bold"),
                                     bg="#2196F3", fg="white", relief=tk.FLAT, width=2,
                                     command=self.show_instructions)
        self.help_button.pack(side=tk.TOP, anchor='ne', padx=10, pady=5)

        # Section for grid input
        self.grid_frame = tk.Frame(self.main_frame, bg="#f0f4f8")
        self.grid_frame.pack(fill=tk.X, pady=10)

        self.grid_label = tk.Label(self.grid_frame, text="Enter Grid (comma-separated rows):",
                                   bg="#f0f4f8", font=("Arial", 12, "bold"))
        self.grid_label.pack(side=tk.TOP, anchor='w')

        self.grid_entry = tk.Text(self.grid_frame, height=5, width=50,
                                  font=("Courier New", 12), wrap=tk.WORD)
        self.grid_entry.pack(pady=5, fill=tk.X)

        # Add a button to allow users to import the grid from a file
        self.import_grid_button = tk.Button(self.grid_frame, text="Import Grid",
                                            command=self.import_grid_from_file,
                                            font=("Arial", 10), bg="#2196F3", fg="white")
        self.import_grid_button.pack(side=tk.LEFT, padx=(0, 10))

        # Section for word input
        self.word_frame = tk.Frame(self.main_frame, bg="#f0f4f8")
        self.word_frame.pack(fill=tk.X, pady=10)

        self.word_label = tk.Label(self.word_frame, text="Enter Complete Word to Search:",
                                   bg="#f0f4f8", font=("Arial", 12, "bold"),
                                   fg="#FF5722")  # Highlight the label with orange text
        self.word_label.pack(side=tk.TOP, anchor='w')

        self.word_entry = tk.Entry(self.word_frame, width=30,
                                   font=("Arial", 12), justify='center')
        self.word_entry.pack(pady=5, fill=tk.X)

        # Section for action buttons
        self.button_frame = tk.Frame(self.main_frame, bg="#f0f4f8")
        self.button_frame.pack(fill=tk.X, pady=10)

        # Button to start solving the word search
        self.solve_button = tk.Button(self.button_frame, text="Find Entire Word",
                                      command=self.solve_word_search,
                                      font=("Arial", 12, "bold"),
                                      bg="#4CAF50", fg="white",
                                      activebackground="#45a049")
        self.solve_button.pack(side=tk.LEFT, expand=True, padx=10)

        # Button to clear all inputs and reset the grid
        self.clear_button = tk.Button(self.button_frame, text="Clear",
                                      command=self.clear_all,
                                      font=("Arial", 12),
                                      bg="#f44336", fg="white")
        self.clear_button.pack(side=tk.LEFT, expand=True, padx=10)

        # Canvas to visualize the grid and results
        self.canvas = tk.Canvas(self.main_frame, bg="white", height=350, width=350)
        self.canvas.pack(pady=10, fill=tk.BOTH, expand=True)

    def show_instructions(self):
        """
        Display instructions on how to use the application.
        """
        instructions = (
            "Welcome to the Word Search Solver!\n\n"
            "1. Enter your word search grid in the text box. Each row should be separated "
            "by a comma or new line. For example:\n"
            "   A,B,C\n"
            "   D,E,F\n"
            "   G,H,I\n\n"
            "2. Type the complete word you want to find in the provided field.\n\n"
            "3. Click 'Find Entire Word' to locate the word in the grid.\n\n"
            "4. Use the 'Clear' button to reset the grid and inputs.\n\n"
            "5. Optionally, you can import a grid from a text file by clicking 'Import Grid'."
        )
        messagebox.showinfo("How to Use", instructions)

    def import_grid_from_file(self):
        """
        Import the grid from a text file with comma-separated values.
        """
        try:
            # Open a file dialog to select the file
            file_path = filedialog.askopenfilename(
                title="Select Grid File",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if file_path:
                with open(file_path, 'r') as file:
                    grid_content = file.read().strip()
                    # Populate the grid entry field with the file content
                    self.grid_entry.delete('1.0', tk.END)
                    self.grid_entry.insert(tk.END, grid_content)
        except Exception as e:
            # Handle any errors during file import
            messagebox.showerror("File Import Error", f"Could not import file: {e}")

    def clear_all(self):
        """
        Clear all inputs and reset the canvas.
        """
        self.grid_entry.delete('1.0', tk.END)  # Clear the grid input field
        self.word_entry.delete(0, tk.END)  # Clear the word input field
        self.canvas.delete("all")  # Clear the canvas visualization
        self.last_found_path = None  # Reset the last path

    def draw_grid(self, grid, path=None):
        """
        Draw the grid on the canvas with optional path highlighting.
        """
        self.canvas.delete("all")  # Clear any existing drawings
        rows, cols = len(grid), len(grid[0])
        cell_size = min(50, max(350 // rows, 350 // cols))  # Adjust cell size dynamically

        for r in range(rows):
            for c in range(cols):
                x1, y1 = c * cell_size, r * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                # Highlight the path in amber if provided
                color = "#FFD54F" if path and (r, c) in path else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
                self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2,
                                        text=grid[r][c].upper(), font=("Arial", 16))

    def solve_word_search(self):
        """
        Solve the word search puzzle and display the result.
        """
        grid_text = self.grid_entry.get("1.0", tk.END).strip()
        try:
            # Parse the grid and input word
            grid = [row.split(',') for row in grid_text.split('\n') if row]
            word = self.word_entry.get().strip().lower()

            if not grid or not word:
                raise ValueError("Grid and word are required.")

            # Use the backtracking algorithm to find the word
            found, path = self.word_search(grid, word)
            if found:
                messagebox.showinfo("Result", f"The word '{word}' was found!")
                self.draw_grid(grid, path=path)  # Highlight the found path
                self.last_found_path = path
            else:
                messagebox.showinfo("Result", f"The word '{word}' was not found.")
        except Exception as e:
            # Handle any errors during the process
            messagebox.showerror("Error", str(e))

    def word_search(self, grid, word):
        """
        Backtracking algorithm to search for the word in the grid.
        """
        rows, cols = len(grid), len(grid[0])

        def backtrack(r, c, index, path):
            if index == len(word):  # All characters matched
                return path
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in path or grid[r][c].lower() != word[index]:
                return None  # Out of bounds or invalid path

            path.append((r, c))  # Add current cell to path
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Explore all directions
                result = backtrack(r + dr, c + dc, index + 1, path)
                if result:
                    return result
            path.pop()  # Backtrack if no match found
            return None

        for r in range(rows):
            for c in range(cols):
                if grid[r][c].lower() == word[0]:  # Start search from matching character
                    path = backtrack(r, c, 0, [])
                    if path:
                        return True, path
        return False, []


if __name__ == "__main__":
    root = tk.Tk()
    app = WordSearchApp(root)
    root.mainloop()

# --- Time Complexity Analysis ---
#
# Let `m` = number of rows in the grid, `n` = number of columns in the grid,
# and `L` = length of the word to search.
#
# For every cell in the grid (total of m * n cells), the algorithm explores up to 4 possible directions.
# The depth of the recursion is equal to the length of the word (`L`).
#
# Worst-Case Time Complexity:
# O(m * n * 4^L)
#
# - For each starting cell, the algorithm explores all possible paths of length `L` in 4 directions.
# - If the grid is large and the word is long, the number of recursive calls grows exponentially.
#
# --- Example Cases ---
# 1. Small Grid, Short Word:
#    - Example: 3x3 grid, word length = 3
#    - Total calls: O(3 * 3 * 4^3) = O(108)
#    - Efficient due to small recursion depth.
#
# 2. Large Grid, Short Word:
#    - Example: 20x20 grid, word length = 3
#    - Total calls: O(20 * 20 * 4^3) = O(6400)
#    - Still manageable as the word is short.
#
# 3. Large Grid, Long Word:
#    - Example: 20x20 grid, word length = 10
#    - Total calls: O(20 * 20 * 4^10) = O(209,715,200)
#    - Exponentially expensive, making it computationally impractical without optimization.
#
# --- Optimizations ---
# 1. Pruning:
#    - Paths are pruned early if they cannot lead to a valid solution (e.g., mismatched characters or revisited cells).
#
# 2. Memoization:
#    - Caching intermediate results can prevent redundant computations for overlapping subproblems.
#
# 3. Word Length Constraints:
#    - Limit the length of words to be searched based on the grid size to reduce computational overhead.
#
# --- Practical Notes ---
# - The algorithm works well for small grids and short words.
# - For large grids and long words, consider implementing optimizations or using heuristic-based approaches.
