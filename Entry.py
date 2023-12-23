from Methods import *

myMatrix = [[-1, 1, -1, -1, 8],
            [2,  4,  0,  0, 10],
            [0,  0,  1,  1, 3],
            [2, -3,  0,  -5, 0]]

table = createTable(myMatrix)
print(optimize(table))