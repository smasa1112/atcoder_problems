import sys
sys.setrecursionlimit(10**9)

N,X=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(N)]
INF=10**18
dp=[[INF]*N for i in range(X)]
dp[0][0]=ab[0][0]+ab[0][1]

for i in range(0,X-1):
    for j in range(0,N-1):
        if dp[i][j]!=INF:
            dp[i+1][j]=dp[i][j]+ab[j][1]
            dp[i+1][j+1]=min(dp[i][j]+ab[j+1][0]+ab[j+1][1],dp[i+1][j+1])
        
        
        
print(min(dp[-1]))
