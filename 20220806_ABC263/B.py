N=int(input())

P=list(map(int,input().split()))

cnt=1

num=P[-1]
while num!=1:
    num =P[num-2]
    cnt+=1
print(cnt)