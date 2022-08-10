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