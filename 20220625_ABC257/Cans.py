n=int(input())
S=list(map(int,list(input())))
W=list(map(int,input().split()))

ca_l=list(zip(S,W))
ca_l.sort(key=lambda s: s[1])
c_or_a=[data[0] for data in ca_l]
ans=c_or_a.count(1)

#左から線を動かして超えたかどうかで判定
#一個前の値と同じだったらパス
x=ans
for i in range(n):
    if ca_l[i][0]:
        x-=1
    else:
        x+=1
    if i < n-1:
        if ca_l[i][1] != ca_l[i+1][1]:
            ans=max(ans,x)
    else:
        ans = max(ans,x)

print(ans)