def exist(board, word):

    rows = len(board)
    cols = len(board[0])

    def dfs(board, word, r, c, wordIdx):
        # base cases
        if wordIdx == len(word):
            return True
        if r<0 or r>=rows or c<0 or c>=cols:
            return False
        if board[r][c] != word[wordIdx]:
            return False
        
        temp = board[r][c]
        board[r][c] = "#"
        
        # check neighbours
        found = (dfs(board, word, r-1, c, wordIdx+1) or 
                dfs(board, word, r, c+1, wordIdx+1) or
                dfs(board, word, r+1, c, wordIdx+1) or 
                dfs(board, word, r, c-1, wordIdx+1))
        
        board[r][c] = temp

        return found

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if dfs(board, word, r, c, 0):
                    return True
    
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(exist(board, word))