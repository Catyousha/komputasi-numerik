a = [1.0, 2.0, 3.0]
a.append(4.0)
print(a)  # [1.0, 2.0, 3.0, 4.0]

c = a[:]
c[0] = 5.0
print(c)  # [5.0, 2.0, 3.0, 4.0]

matriks_2d = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

print(matriks_2d)
print(matriks_2d[1])  # [4, 5, 6]
print(matriks_2d[1][2])  # 6
