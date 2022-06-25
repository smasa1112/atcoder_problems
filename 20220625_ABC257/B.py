n,x,q=map(int,input().split())
A=list(map(int,input().split()))
L=list(map(int,input().split()))

masu=[0]*(n+1)
for a in A:
    masu[a]=1

for l in L:
    if A[l-1]!=n and masu[A[l-1]]==1:
        if masu[A[l-1]+1]==0:
            masu[A[l-1]+1]+=1
            masu[A[l-1]]-=1
            A[l-1]+=1
print(*A)