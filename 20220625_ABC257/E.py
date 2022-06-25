N=int(input())
C=list(map(int,input().split()))
x=0

#桁数を最大化できるようにまず最大桁を求める
min_num=min(C)
keta=N//min_num

ans=""
for i in range(keta):
    for j in reversed(range(len(C))):
        if (min_num * (keta-1-i) + C[j]) <= N:
            N-=C[j]
            ans+=str(j+1)
            break
print(ans)

