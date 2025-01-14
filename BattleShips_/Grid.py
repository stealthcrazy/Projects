def Grid(x,y):
    grid = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(' ')
        grid.append(row)
    #print(grid)
    return grid