S=0
n=int(input())
xyp=[list(map(int,input().split())) for _ in range(n)]
#グラフの最短経路問題っぽい？
#→最短距離問題だった
#ワーシャルフロイド法やDFSを使うとO(N^3)で計算可能
def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]= min(d[i][j],d[i][k]+d[k][j])
    return d

#隣接行列の定義、初期化
d = [[float("inf") for i in range(n)] for i in range(n)]
