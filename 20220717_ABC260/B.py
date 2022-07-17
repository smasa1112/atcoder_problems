N,X,Y,Z=map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
students=list(zip(range(1,N+1),A,B))

math_higher=sorted(students,reverse=True,key=lambda s:s[1])
english_higher=sorted(students,reverse=True,key=lambda s: s[2])
sum_higher=sorted(students,reverse=True,key=lambda s: s[1]+s[2])

ans=[]

ans+=[data[0] for data in math_higher[:X]]

y_cnt=0
i=0
while y_cnt<Y:
    data=english_higher[i]
    if data[0] not in ans: 
        ans.append(data[0])
        y_cnt+=1
    i+=1


z_cnt=0
i=0
while z_cnt<Z:
    data=sum_higher[i]
    if data[0] not in ans: 
        ans.append(data[0])
        z_cnt+=1
    i+=1
    
ans.sort()

print(*ans,sep="\n")
