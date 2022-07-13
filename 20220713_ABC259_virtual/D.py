import math
import sys
sys.setrecursionlimit(10**6)

N=int(int(input()))
sx, sy, tx, ty=map(int,input().split())

circles=[]
visited=[False]*N
s_ind=[]
t_ind=[]

G=[[] for _ in range(N)]

#入力の受け取りとどの円にいるか判定
for i in range(N):
    x,y,r=map(int,input().split())
    circles.append([x,y,r])
    if (sx-x)**2+(sy-y)**2==r**2:
        visited[i]==False
        s_ind.append(i)
    if (tx-x)**2+(ty-y)**2==r**2:
        t_ind.append(i)
    
# 円の交差関係をグラフで受け取り
for i in range(N):
    x_i,y_i,r_i=circles[i]
    for j in range(N):
        x_j,y_j,r_j=circles[j]
        if (r_i-r_j)**2<=(x_i-x_j)**2+(y_i-y_j)**2<=(r_i+r_j)**2:
            G[i].append(j)
            G[j].append(i)
            
for i in range(N):
    G[i]=list(set(G[i]))
            
#頂点vを始点とした深さ優先探索
def rec(v,G,visited):
    visited[v]=True
    for v2 in G[v]:
        if visited[v2]:continue
        rec(v2,G,visited)
    return

for v in s_ind:
    rec(v,G,visited)

flag=False
for v in t_ind:
    if visited[v]==True:
        flag=True
        break 
    
if flag:
    print("Yes")
else:
    print("No")       

    