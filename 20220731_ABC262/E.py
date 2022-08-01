N,M,K=map(int,input().split())
G=[[] for _ in range(N)]

for _ in range(M):
    u,v=map(int,input().split())
    G[u-1].append(v-1)
print(G)