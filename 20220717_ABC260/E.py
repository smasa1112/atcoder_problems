N,M=map(int,input().split())

# Aが何の時Bがどの値になるか
pairs = [[] for _ in range(M+1)]
r=0
minB=M

#A,Bは狭義単調増加なので尺取り法が使える
for _ in range(N):
    a,b=map(int,input().split())
    pairs[a].append(b)
    r=max(r,a)
    minB=min(minB,b)

f = [0]* (M+10)
for l in range(1,minB+1):
    #全a,bが存在しうる区間に+1をする
    #rは最初区間始まりの最大値
    f[r-l+1]+=1
    f[M-l+1 + 1]-=1
    if len(pairs[l])!=0:
        #区間終わりが出てきたら最大値を更新
        r = max(r, max(pairs[l]))
    
for i in range(1,M+1):
    #累積和で足す
    f[i] += f[i-1]
    
print(*f[1:M+1])


    