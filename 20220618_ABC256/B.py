n=int(input())
a=list(map(int,input().split()))
tile=[0]*4

p=0
for i in range(n):
    num=a[i]
    tile[0]=1
    for j in range(4)[::-1]:
        if tile[j]:
            if j+num>=4:
                p+=1
            else:
                tile[j+num]=1
            tile[j]=0
print(p)