a = [[1, 4, 5],
     [-3, 5, 9],
     [5, -2, 0],
     [1, 8, -5]]

w = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

b = [[1, 4, -3],[-3, 5, 9]]

print(a)
print(w)
print(b)
print(a[1][2])
print(a[0][2])
print(a[3][2])

column =  []
for row in a:
  column.append(row[2])
  print("halo ", column )
else:
  print("exit")

# matrix multiplication
print('matrix multiplication')
columns, rows = len(a), len(w[0])
print(columns, rows )