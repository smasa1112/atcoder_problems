N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()

ans=[]

def minimize_stress(score):
    l = 0
    r = N-1
    m=0
    #スコアの初期化
    while abs(r - l) > 1:
        m = (r+l)//2
        if score>=A[m]:
            l=m
        else:
            r=m
    return min(abs(A[r]-score),abs(score - A[l]))


for _ in range(Q):
    B = int(input())
    ans.append(minimize_stress(B))

print( *ans, sep="\n")
