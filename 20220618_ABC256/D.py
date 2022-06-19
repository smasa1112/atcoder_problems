N=int(input())
lr=[list(map(int,input().split())) for _ in range(N)]
ls=[[span[0],0] for span in lr]
rs=[[span[1],1] for span in lr]
query=[*ls,*rs]
query.sort(key=lambda x: x[0])

cnt=0
for time,i in query:
    if i == 0:
        if cnt==0:
            data=[]
            data.append(time)
        cnt+=1
    else:
        cnt-=1
        if cnt==0:
            data.append(time)
            print(*data)
           
        
        