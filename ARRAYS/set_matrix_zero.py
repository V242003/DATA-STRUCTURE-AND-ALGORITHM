matrix=[[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
rows=len(matrix)
cols=len(matrix[0])
rows_track=[0 for _ in range(rows)]
cols_track=[0 for _ in range(cols)]

for i in range(0,rows):
    for j in range(0,cols):
        if matrix[i][j]==0:
            rows_track[i]=-1
            cols_track[j]=-1

for i in range(0,rows):
    for j in range(0,cols):
        if rows_track[i]==-1 or cols_track[j]==-1:
            matrix[i][j]=0
print(matrix)
