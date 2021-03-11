
# import ../../data_structures/avl_tree as trees 

def grid_traveler(m, n):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)

# Memoization recipe
def grid_traveler_memoized(m, n):
    memo = [[0 for _ in range (n)] for _ in range (m)]
    _grid_traveler_recursive(m, n, memo)

def _grid_traveler_recursive(m, n, memo):
    if memo[m -1][n -1] != 0: return memo[m -1][n -1]
    if memo[n -1][m -1] != 0: return memo[m -1][n -1]
    
    #  ALT
    # use a dictoraty with key formant = 'm, n'
    # 'simpler' and smaller structure than a matrix

    if m == 1 and n == 1: 
        memo[0][0] = 1
        return 1
    if m == 0 or n == 0: 
        return 0
    
    memo[m - 2][n - 1] = _grid_traveler_recursive(m - 1, n, memo)
    memo[m - 1][n - 2] = _grid_traveler_recursive(m, n - 1, memo)

    # may want to do the same the other way around the matrix.

    return memo[m -1][n] + memo[m][n -1]


