def grid_traveler(n, m):
    if n == 0 or m == 0: 
        return 0 #[[]]

    grid = [[0 for _ in range(m)] for _ in range(n)]
    grid[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0: continue
            grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

    return grid[n-1][m-1]

print(grid_traveler(0, 1)) # 0
print(grid_traveler(1, 0)) # 0
print(grid_traveler(1, 1)) # 1
print(grid_traveler(1, 2)) # 2
print(grid_traveler(2, 2)) # 0
print(grid_traveler(3, 2)) # 3
print(grid_traveler(4, 4)) # 10
print(grid_traveler(18, 18)) # 0
