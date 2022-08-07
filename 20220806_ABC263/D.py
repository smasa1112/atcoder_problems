from numpy import argmin


N,L,R=map(int,input().split())
A=list(map(int,input().split()))

# N<= 2*10**5のためN^2は間に合わない
# O(logN) or O(N)
# 左で置き換えられる地点と右で置き換えられる地点を見る

# [0,i)でLに置き換えた時の総和累積和?

# [i,N)でRに置き換えた時の総和累積和を算出?


#####segfunc#####
def segfunc(x, y):
    return x+y
#################

#####ide_ele#####
ide_ele =0
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

# 区間更新・区間和を求めるもの
seg_L = SegTree(A, segfunc, ide_ele)
seg_R = SegTree(A, segfunc, ide_ele)

#i番目までをNにした場合の区間和
cumsum_L=[0]*(N+1)

cumsum_L[0]=sum(A)
for i in range(N):
    seg_L.update(i,L)
    cumsum_L[i+1]=seg_L.query(0,N)
    
cumsum_R=[0]*(N+1)
cumsum_R[N]=cumsum_L[0]
for i in range(N-1,-1,-1):
    seg_R.update(i,R)
    cumsum_R[i]=seg_R.query(0,N)
    
print(cumsum_L)
print(cumsum_R)

if min(cumsum_L)==cumsum_L[0] and min(cumsum_R)==cumsum_R[-1]:
    print(cumsum_L[0])
else:
    argmin(cumsum_L)
