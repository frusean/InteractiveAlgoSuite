
import tkinter as tk
from tkinter import messagebox, scrolledtext

class SubsetSumApp:
    def __init__(self, root):
        """
        Initialize the GUI application for solving the Subset Sum problem.
        Sets up the window layout, input fields, and the solve button.
        """
        self.root = root
        self.root.title("Subset Sum Problem Solver")  # Set the window title

        # Set up the window dimensions and background color
        self.root.geometry("600x500")
        self.root.config(bg="#f4f4f9")

        # Label and input field for entering numbers
        self.label_nums = tk.Label(root, text="Enter numbers (comma-separated):", bg="#f4f4f9", font=("Arial", 12))
        self.label_nums.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_nums = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry_nums.grid(row=0, column=1, padx=10, pady=10)

        # Label and input field for entering the target sum
        self.label_target = tk.Label(root, text="Enter target sum:", bg="#f4f4f9", font=("Arial", 12))
        self.label_target.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_target = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry_target.grid(row=1, column=1, padx=10, pady=10)

        # Label for displaying the algorithm's step-by-step output
        self.output_label = tk.Label(root, text="Step-by-Step Output:", bg="#f4f4f9", font=("Arial", 12))
        self.output_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # ScrolledText widget to show detailed output of the algorithm
        self.output_text = scrolledtext.ScrolledText(root, height=15, width=60, font=("Courier", 10), bg="#1e1e1e", fg="white")
        self.output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.output_text.config(state=tk.DISABLED)  # Initially make it read-only

        # Button to trigger the Subset Sum algorithm
        self.solve_button = tk.Button(root, text="Solve", command=self.solve_subset_sum, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.solve_button.grid(row=4, column=0, columnspan=2, pady=20)

    def solve_subset_sum(self):
        """
        Handles the input validation, runs the backtracking algorithm, and updates the output text area with the result.
        """
        # Retrieve user inputs
        nums_str = self.entry_nums.get()
        target_str = self.entry_target.get()

        try:
            # Convert the comma-separated input into a list of integers
            nums = list(map(int, nums_str.split(',')))
            target = int(target_str)  # Parse the target sum
        except ValueError:
            # Show an error message if input is invalid
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")
            return

        # Clear the output area to display fresh results
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)

        # Use the backtracking algorithm to solve the problem
        steps = []  # Keep track of the steps taken during the algorithm
        found = self.backtrack(nums, target, 0, 0, [], steps)

        # Display the result in the output area
        if found:
            result_message = f"Subset found: {steps[-1]}"
        else:
            result_message = "No subset found."

        self.output_text.insert(tk.END, result_message + "\n\n")  # Write the final message
        self.output_text.config(state=tk.DISABLED)  # Make the output area read-only again

    def backtrack(self, nums, target, index, current_sum, current_subset, steps):
        """
        Recursive backtracking function to determine if a subset of numbers sums to the target value.
        Logs intermediate steps to the output area.
        """
        # Base case: If the target is reached, save the subset and return True
        if current_sum == target:
            steps.append(f"Subset: {current_subset}")
            return True

        # Base case: If we've exhausted the numbers or exceeded the target, return False
        if index >= len(nums) or current_sum > target:
            return False

        # Log the attempt to include the current number
        self.output_text.insert(tk.END, f"Trying: {current_subset + [nums[index]]} | Sum: {current_sum + nums[index]}\n")
        self.output_text.yview(tk.END)  # Auto-scroll to display the latest step

        # Recursive case: Include the current number
        if self.backtrack(nums, target, index + 1, current_sum + nums[index], current_subset + [nums[index]], steps):
            return True

        # Log the decision to exclude the current number
        self.output_text.insert(tk.END, f"Skipping: {current_subset} | Sum: {current_sum}\n")
        self.output_text.yview(tk.END)

        # Recursive case: Exclude the current number
        if self.backtrack(nums, target, index + 1, current_sum, current_subset, steps):
            return True

        return False  # If no solution is found, return False


# --- Main Function to Run the GUI Application ---
if __name__ == "__main__":
    # Create the main Tkinter window and launch the application
    root = tk.Tk()
    app = SubsetSumApp(root)
    root.mainloop()


# --- Time Complexity and Performance Discussion ---


# ### Time Complexity Analysis:
# The backtracking algorithm systematically explores all subsets of the input numbers to find a solution.
# For a list of size `n`, there are 2^n possible subsets.
#
# - Worst-case time complexity**: O(2^n)
#   - At each step, the algorithm branches into two possibilities: include or exclude the current number.
#   - Each subset exploration takes constant time, so the total complexity is dominated by the number of subsets.
#
# ### Factors Affecting Performance:
# 1. Input Size:
#    - Larger input sizes increase the number of subsets exponentially, leading to longer runtimes.
# 2. Target Value**:
#    - If the target is too small or too large relative to the sum of the numbers, the algorithm can terminate early, reducing computation time.
# 3. Number Distribution**:
#    - If numbers are spread out and diverse, fewer valid subsets exist, which can improve efficiency.
#    - Closely packed numbers create more possible subsets, increasing runtime.
# 4. Early Termination:
#    - The algorithm stops as soon as a valid subset is found, which can significantly save time for feasible targets.
# 5. Pruning (Not Implemented Here)**:
#    - Skipping numbers that are too large to contribute to the target or caching results (memoization) could improve runtime.
#
# ### Optimizations (Not Implemented):
# - Sorting:
#   - Sorting the numbers in descending order can improve the likelihood of finding a solution earlier.
# - Pruning:
#   - Stop recursion when adding the current number exceeds the target.
# - Memoization:
#   - Cache results for overlapping subproblems to avoid redundant calculations.
#
