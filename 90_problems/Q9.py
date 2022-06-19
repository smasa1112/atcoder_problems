import math

N=int(input())
pos=[list(map(int,input().split())) for _ in range(N)]

#O(N^2logN)なのでN=2000だと通る
ans=-1
for i in range(N):
    x_,y_=pos[i]
    angles=[]
    for j in range(N):
        xj,yj=pos[j]
        if i==j:
            continue
        else:
            angles.append(math.degrees(math.atan2(yj-y_,xj-x_)))
    #各点でのなす角の保存
    angles.sort()
    now=0
    for j in range(len(angles)-1):
        now=max(j+1,now)
        while now<len(angles)-1:
            now_v=min(angles[now]-angles[j],360-angles[now]+angles[j])
            next_v=min(angles[now+1]-angles[j],360-angles[now+1]+angles[j])
            if now_v < next_v:
                now+=1
            else:
                break
        now_v = min(angles[now]-angles[j],360-angles[now]+angles[j])
        ans = max(ans,now_v)

print(ans)
