from collections import deque

N = int(input())

#最長距離を求めたいので各点からの探索に長けるBFSを使用
def bfs(s):
    dist = [None]*N
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in vec[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + 1
            que.append(w)
    d = max(dist)
    return dist.index(d), d


# 閉路の最大値は最大パス+1→最大パスを求める
vec = [[] for _ in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    vec[A-1].append(B-1)
    vec[B-1].append(A-1)
u, _ = bfs(0)
v, d = bfs(u)

print(d+1)
