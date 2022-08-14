from collections import deque
import sys
sys.setrecursionlimit(10**6)

N,M,E= list(map(int,input().split()))

G = [[]*(N+M)]
V = []

for _ in range(E):
    u,v = map(int,input().split())
    G[u].append()
    G[v].append()
    V.append([u,v])
    
Q = int(input())

# 各回でやれるかどうかなのでBFSはできない
# 超頂点を使って逆側からUFを実行する
for _ in range(Q):
    X = int(input())
    v = V[X]
    G[v[0]].remove(v[1])
    G[v[1]].remove(v[2])  

ans = [0]*Q             
    
    