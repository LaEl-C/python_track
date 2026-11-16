"""Game of life."""
def tick(matrix):
    """
    para: matrix
    return: matrix
    """
    if not matrix:
        return matrix
    row = len(matrix)
    col = len(matrix[0])
    
    new_mat = [[0 for _ in range(col)] for _ in range(row)]
    for r in range(row):
        for c in range(col):
            live_n = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr = r + dr
                    nc = c + dc
                    if dr == 0 and dc == 0:
                        continue
                    if 0 <= nr < row and 0 <= nc < col:
                        live_n += matrix[nr][nc]
            if matrix[r][c] == 1:
                if live_n == 2 or live_n == 3:
                    new_mat[r][c] = 1
            elif live_n == 3:
                new_mat[r][c] = 1
    return new_mat
                
            
    
    
        
