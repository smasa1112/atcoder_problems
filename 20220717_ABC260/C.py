N,X,Y=map(int,input().split())

#逆にレベルNが最初レベル1が最後になる2次元配列を持つ
rb=[[0]*2 for _ in range(N)]

rb[0][0]=1

if N==1:
    print(0)
    exit()
    
for i in range(N-1):
    if rb[i][0]>0:
        rb[i+1][0]+=rb[i][0]
        rb[i][1]+=X*rb[i][0]
    if rb[i][1]>0:
        rb[i+1][0]+=rb[i][1]
        rb[i+1][1]+=Y*rb[i][1]

print(rb[-1][1])   