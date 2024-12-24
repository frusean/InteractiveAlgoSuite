
# README: Backtracking Algorithms Assignment 4

This ZIP file contains solutions for Assignment #4 of the Analysis of Algorithms (AoA) . The assignment focuses on implementing backtracking algorithms for combinatorial problems.
#Name:Rusean Francis
#ID:2101012160
---

## Assignment Overview

### Objective
To implement backtracking algorithms for:
1. **N-Queens Problem** (Interactive and Static)
2. **Subset Sum Problem**
3. **Word Search Problem**

### Structure
Each solution includes:
- **Implementation**: The algorithm solving the problem.
- **Visualization**: Graphical representation or user interaction where applicable.
- **Time Complexity Analysis**: Included in the source code as comments.

---

## Files in ZIP

| File                  | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `n_queens.py`         | Solves the N-Queens problem and includes interactive and static visualizations using Pygame. |
| `subset_sum.py`       | Solves the Subset Sum problem with a Tkinter-based GUI for user interaction.|
| `word_search.py`      | Solves the Word Search problem with a backtracking algorithm and visualization in Tkinter. |

---

## Problems and Solutions

### 1. N-Queens Problem
**Goal**: Place `N` queens on an `N x N` chessboard such that no two queens threaten each other.

- **Files**: `n_queens.py`
- **Features**:
  - **Interactive Visualization**: Drag-and-drop interface for user interaction.
  - **Static Backtracking**: View all solutions sequentially.
- **Complexity**: Worst-case \(O(N!)\).
- **Optimizations**: 
  - Efficient conflict checking with arrays.
  - Symmetry reduction for faster computations.

---

### 2. Subset Sum Problem
**Goal**: Determine if a subset of numbers in a given set sums to a specified target.

- **Files**: `subset_sum.py`
- **Features**:
  - GUI-based input and output using Tkinter.
  - Step-by-step solution logging.
- **Complexity**: Worst-case \(O(2^N)\).
- **Performance Factors**:
  - Early termination when target is reached.
  - Input size and target value.

---

### 3. Word Search Problem
**Goal**: Find if a given word exists in a 2D grid of letters.

- **Files**: `word_search.py`
- **Features**:
  - GUI for grid input and word search.
  - Highlights the word path if found.
- **Complexity**: Worst-case \(O(M 	imes N 	imes 4^L)\), where \(M\) and \(N\) are grid dimensions, and \(L\) is the word length.
- **Optimizations**:
  - Pruning invalid paths early.
  - Memoization for repeated subproblems.

---

## How to Run

### Prerequisites
- **Python 3.x** installed on your system.
- **Libraries**:
  - `pygame` (for N-Queens visualization)
  - `tkinter` (built-in, for Subset Sum and Word Search GUIs)

### Steps
1. Unzip the file.
2. Navigate to the folder containing the problem solution files.
3. Run the corresponding Python file. For example:
   ```bash
   python n_queens.py
   ```

---

## Time Complexity Analysis
Each algorithm's complexity analysis is included as comments in the respective source code files.

---

 
