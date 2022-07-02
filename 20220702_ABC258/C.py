N,Q=map(int,input().split())
S=input()

i=0
for _ in range(Q):
    query=list(map(int,input().split()))
    if query[0] == 1:
        i+=query[1]
    if query[0] == 2:
        i%=N
        print(S[query[1]-1-i])
        