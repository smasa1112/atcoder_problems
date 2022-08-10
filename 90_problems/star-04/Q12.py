H,W = map(int,input().split())
Q=int(input())

m= [[False]*W for _ in range(H)]

# 毎回BFSするの時間がかかりそう→辺からいけるかチェックする
# つながっているものを判定するにはUnion Findを用いる
# bfsだと時間がかかるし、つながっている判定ができるだけでOKなので

# 点数がH*W点なのでH*W点のUFを作成
# H*r+cで点を一列にまとめる

from collections import defaultdict

class UnionFind():
    
    def __init__(self,n) -> None:
        self.n = n
        self.parents = [-1]*n
        return 
    
    def find(self, x):
        # xの大本(ルート)を探す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
    def union(self,x,y):
        # xとyの所属グループを併合
        # 基本数が小さい方に統合される
        x = self.find(x)
        y = self.find(y)
        
        if x==y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
            
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        # xのグループの要素数を返す
        return -self.parents[self.find(x)]
    
    def members(self, x):
        # xが属するグループ内の要素を返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def same(self,x,y):
        return self.find(x) == self.find(y)
    
    def roots(self):
        # 根となる要素を返す
        return [i for i,x in enumerate(self.parents) if x < 0 ]
    
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r,m in self.all_group_members().items())

# どうやら下の部分で間違えていた部分があった様子→rrとccの範囲が別だった。
# 構造の部分と比較してみたら上手くいった

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
        if m[ra][ca] and m[rb][cb] and uf.same(x, y):
            print("Yes")
        else:
            print("No")