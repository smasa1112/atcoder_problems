N=int(input())

A=[list(input()) for _ in range(N)]

ans="correct"

for i in range(N):
    for j in range(N):
        if A[i][j]=="W" and A[j][i]!="L":
            ans="incorrect"
        if A[i][j]=="D" and A[j][i]!="D":
            ans="incorrect"
        if A[i][j]=="L" and A[j][i]!="W":
            ans="incorrect"
            
print(ans)