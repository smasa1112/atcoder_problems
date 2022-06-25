import bisect
n=int(input())
S=list(map(int,list(input())))
W=list(map(int,input().split()))

cl=[]
al=[]

for i in range(n):
    if S[i]==0:
        cl.append(W[i])
    else:
        al.append(W[i])
        
cl.sort()
al.sort()
ans=max(len(cl),len(al))

#2分探索？→狭義単調増加でないため使えなさそう
#狭義単調増加にできるなら使用可能？
#子供か大人の回答人数を固定して２分探索すると
#nlog_nの計算量で住む

for i in range(len(al)):
    f_x=len(al)-i
    f_x+=bisect.bisect_left(cl,al[i])
    ans=max(ans,f_x)
    

print(ans)

