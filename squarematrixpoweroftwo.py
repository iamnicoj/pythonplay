a = [[1, 4, 5, 4],
     [-3, 5, 9, 6 ],
     [5, -2, 0, -5],
     [1, 8, -5, -7]]

# matrix multiplication
print('basic contruct matrix multiplication')
side = len(a)

print(f"generating matrix with {side} rows and {side} columns")

Matrix = [[0 for x in range(side)] for y in range(side)]

for i in range(side):
  for j in range(side):
    for k in range(side):
      Matrix[i][j] += a[i][k] * a[k][j]
  print(Matrix[i])
