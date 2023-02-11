N,M = map(int,input().split())

a = list(map(int,input().split()))

ans = []
partial = []
for i in range(1,N+1):
    if i in a:
        partial.append(i)
    else:
        partial.append(i)
        ans+=reversed(partial)
        partial =[]
print(*ans)