a = [[1, 4, 5],
     [-3, 5, 9],
     [5, -2, 0],
     [1, 8, -5]]

w = [[1, 4, 5, 12, 0], 
    [-5, 8, 9, -3, 0],
    [-6, 7, 11, 19, 0]]

# matrix multiplication
print('basic contruct matrix multiplication')
rows = len(a)
columns = len(w[0])

print(f"generating matrix with {rows} rows and {columns} columns")

Matrix = [[0 for x in range(columns)] for y in range(rows)]

for i in range(len(a)):
  for j in range(len(w[0])):
    for k in range(len(w)):
      Matrix[i][j] += a[i][k] * w[k][j]     
  print(Matrix[i])
