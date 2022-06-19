H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

B = [[0]*(W) for _ in range(H)]
# print(sum(A[2]))
rows=[sum(row) for row in A]
cols=[0]*W
for i in range(W):
  nums=[A[j][i] for j in range(H)]
  cols[i]=sum(nums)
  
for i in range(H):
    for j in range(W):
        B[i][j] = rows[i]+cols[j]-A[i][j]

for i in range(H):
    print(*B[i])
