from collections import deque
T= int(input())


for _ in range(T):
    N,M = map(int,input().split())
    C = list(map(int,input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v  = map(int,input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    #2人の今いる位置の状態行列を作成
    states = [[-1]*N for _ in range(N)]
    #最初は0,N-1にいる
    states[0][N-1]=0
    
    Q = deque()
    #[pos_takahashi,pos_aoki]
    Q.append([0,N-1])
    while len(Q)>0:
        now = Q.popleft()
        for next_t in G[now[0]]:
            for next_a in G[now[1]]:
                if C[next_t]==C[next_a]:
                    continue
                elif states[next_t][next_a]== -1:
                    states[next_t][next_a]=states[now[0]][now[1]]+1
                    Q.append([next_t,next_a])
    print(states[N-1][0])
    
'''
コメント:

それぞれのいる位置が重要になるので、
それぞれで幅優先探索をするのではなく
全体を状態として管理する。
また今回はそれがそれぞれの点が2000しかなかったため
あっても2000*2000で4000000程度であったことが重要
幅探索O(V+E)なのでそれほど多くはならない
'''