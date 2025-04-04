# Neo Holgado
# 03/03/2025
# CS325-400
from collections import deque


def solve_puzzle(Board, Source, Destination):
    """
    Given a board, source coordinates (a, b), and destination coordinates (x, y),
    finds a path on the board from the source to the destination
    """
    # Determine the rows and columns of the board
    rows = len(Board)
    columns = len(Board[0])

    # If the source is the destination, return the source
    if Source == Destination:
        return [Source]

    # Store the current row, column, and path in the queue
    queue = deque([(Source[0], Source[1], [Source])])

    # Track visited cells
    visited = set()
    visited.add(Source)

    # Initialize directions
    directions = [
        (-1, 0),    # Left
        (1, 0),     # Right
        (0, -1),    # Down
        (0, 1)      # Up
    ]

    while queue:
        # Store the values for row, column, and path taken
        row, column, path = queue.popleft()

        # Check if we reached the destination
        if (row, column) == Destination:
            return path

        for d_row, d_column in directions:
            # Store the neighboring cell's row and column coordinates and set that as the next cell
            neighbor_row, neighbor_column = row + d_row, column + d_column
            next_cell = (neighbor_row, neighbor_column)

            # Check if the neighboring cells are in bounds
            if neighbor_row < 0 or neighbor_row >= rows:
                continue
            if neighbor_column < 0 or neighbor_column >= columns:
                continue

            # Ignore cells that have been visited or have a barrier
            if next_cell in visited or Board[neighbor_row][neighbor_column] == '#':
                continue

            # Add the cell to the path
            queue.append((neighbor_row, neighbor_column, path + [next_cell]))
            visited.add(next_cell)

    # If the destination can't be reached
    return None


def main():
    # Board for the puzzle
    puzzle_board = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
    ]

    # Test 1
    print(f"Path from (0, 2) to (2, 2): {solve_puzzle(puzzle_board, (0, 2), (2, 2))}")

    # Test 2
    print(f"Path from (0, 0) to (4, 4): {solve_puzzle(puzzle_board, (0, 0), (4, 4))}")

    # Test 3
    print(f"Path from (0, 0) to (4, 0): {solve_puzzle(puzzle_board, (0, 0), (4, 0))}")

    # Test 4
    print(f"Path from (0, 0) to (0, 0): {solve_puzzle(puzzle_board, (0, 0), (0, 0))}")


if __name__ == '__main__':
    main()