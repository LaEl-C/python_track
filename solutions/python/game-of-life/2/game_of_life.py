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
    for row_idx in range(row):
        for col_idx in range(col):
            live_n = 0
            for diff_r in [-1, 0, 1]:
                for diff_c in [-1, 0, 1]:
                    neir = row_idx + diff_r
                    neic = col_idx + diff_c
                    if diff_r == 0 and diff_c == 0:
                        continue
                    if 0 <= neir < row and 0 <= neic < col:
                        live_n += matrix[neir][neic]
            if matrix[row_idx][col_idx] == 1:
                if live_n in (2, 3):
                    new_mat[row_idx][col_idx] = 1
            elif live_n == 3:
                new_mat[row_idx][col_idx] = 1
    return new_mat
                
            
    
    
        
