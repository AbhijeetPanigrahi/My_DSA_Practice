# Brute Force Approach  - TC: O(m*n), SC: O(m*n)
def gameOfLife_bruteforce(board):
    if not board:
        return
    
    rows, cols = len(board), len(board[0])
    
    # Copy of the original board
    copy_board = [[board[r][c] for c in range(cols)] for r in range(rows)]
    
    # Directions of 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    # Iterate through every cell
    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            
            # Count live neighbors
            for dr, dc in directions:   # dr and dc are the row and column offsets (like -1, 0, or 1).
                nr, nc = r + dr, c + dc     # (nr, nc) gives us the neighbor’s coordinates.
                if 0 <= nr < rows and 0 <= nc < cols and copy_board[nr][nc] == 1:
                    live_neighbors += 1
                # This checks if the neighbor’s row index (nr) is inside the grid boundaries.
                # If nr is negative (like -1) or >= rows, it means the neighbor would be outside the board — so we skip it.
                # Same idea for columns
                # If the neighbor cell at (nr, nc) is alive (value 1), then we count it as a live neighbor.

            # Apply the Game of Life rules
            if copy_board[r][c] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = 0  # Dies
            else:
                if live_neighbors == 3:
                    board[r][c] = 1  # Becomes alive


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
board_2 = [[1,1],[1,0]]
# gameOfLife_bruteforce(board_2)
# print(board_2)



# Optimized Approach  - TC: O(m*n), SC: O(1) since in-place

def gameOfLife_optimized(board):
    rows, cols = len(board), len(board[0])
    directions = [
        (-1, -1),   (-1,0),     (-1,1),
        (0, -1),                (0,1),
        (1,-1),     (1,0),      (1,1)   
    ]

    def count_neighbours(r, c):
        live_neighbour = 0

        for dr, dc in directions:
            nr = r+dr
            nc = c+dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if board[nr][nc] == 1 or board[nr][nc] == -1:
                    live_neighbour += 1
        
        return live_neighbour

    # 1st pass
    for r in range(rows):
        for c in range(cols):
            live_neighbours = count_neighbours(r,c)
            if board[r][c] == 1:
                # die for 2 reasons (over-population or under-population)
                if live_neighbours < 2 or live_neighbours > 3:
                    board[r][c] = -1
            else:
                if live_neighbours == 3:
                    board[r][c] = 2

    # 2nd pass
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == -1:
                board[r][c] = 0
            elif board[r][c] == 2:
                board[r][c] = 1


gameOfLife_optimized(board)
print(board)