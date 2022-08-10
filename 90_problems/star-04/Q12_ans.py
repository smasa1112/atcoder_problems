from itertools import product

H, W = map(int, input().split())
Q = int(input())

m = [[False] * W for _ in range(H)]


class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(H * W)
for _ in range(Q):
    q = [int(x) - 1 for x in input().split()]
    if q[0] == 0:
        r, c = q[1:]
        m[r][c] = True
        x = r * W + c
        for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            rr = r + i
            cc = c + j
            if 0 <= rr < H and 0 <= cc < W and m[rr][cc]:
                y = rr * W + cc
                uf.union(x, y)
    else:
        ra, ca, rb, cb = q[1:]
        x = ra * W + ca
        y = rb * W + cb
        if m[ra][ca] and m[rb][cb] and uf.is_same(x, y):
            print("Yes")
        else:
            print("No")
