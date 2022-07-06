def countPaths(maze,row_number, col_number):  

    if (maze[0][0] == -1):
        return 0

    for i in range(row_number):
        if (maze[i][0] == 0):
            maze[i][0] = 1
   
        else:
            break
 
    
    for i in range(1, col_number, 1):
        if (maze[0][i] == 0):
            maze[0][i] = 1
      
        else:
            break
 
    
    for i in range(1,row_number, 1):
        for j in range(1, col_number, 1):
             
            
            if (maze[i][j] == -1):
                continue
 
            
            
            if (maze[i - 1][j] > 0):
                maze[i][j] = (maze[i][j] +
                              maze[i - 1][j])
 
            
            
            if (maze[i][j - 1] > 0):
                maze[i][j] = (maze[i][j] +
                              maze[i][j - 1])
 
    
    
    if (maze[row_number - 1][col_number - 1] > 0):
        return maze[row_number - 1][col_number - 1]
    else:
        return 0
 

if __name__ == '__main__':
    maze = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            ]
   
    row_number = len(maze)
    col_number = len(maze[0])
    
    result = countPaths(maze, row_number, col_number)-1
    print(result)