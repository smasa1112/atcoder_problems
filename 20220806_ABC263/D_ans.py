N,L,R=map(int,input().split())
A=list(map(int,input().split()))

l_dp=[0]*(N+1)
r_dp=[0]*(N+1)

for i in range(1,N+1):
    l_dp[i]=min(L*i,l_dp[i-1]+A[i-1])
    
for i in range(N-1,-1,-1):
    r_dp[i]=min(R*(N-i),r_dp[i+1]+A[i])

ans=[l+r for l,r in zip(l_dp,r_dp)]

print(min(ans))