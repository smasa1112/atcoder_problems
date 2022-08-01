N,M= map(int,input().split())
graph=[[] for _ in range(N)]

for i in range(M):
    u,v=map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

cnt=0
for i in range(N):
    path_1=graph[i]
    for j in path_1:
        if i<j:
            path_2=graph[j]
            for k in path_2:
                if j<k:
                    path_3=graph[k]
                    if i in graph[k]:
                        cnt+=1
print(cnt)       