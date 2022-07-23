N,M= map(int,input().split())
X=list(map(int,input().split()))
bonuses={}
for i in range(M):
    c,b=map(int,input().split())
    bonuses[c]=b
#N回降った時をDPでやるのがよさそう(N<5000)なのでN乗しても高々25000000



#カウンタの値とその時のコイントスの値が大事になるのでそれらの値でDPを持つ
#とりあえず全部上手くいった時を計算する
X_sum=[sum(X[:i]) for i in range(1,N+1)]
#i回目のコイントスでカウンタの数がj
dp=[[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    #カウンタの値はiより大きくならない
    for j in range(1,i+1):
        #カウンタの値がjだったらi回表に出たか判断
        if j in bonuses:
            dp[i][j]=dp[i-1][j-1]+X[i-1]+bonuses[j]
        else:
            dp[i][j]=dp[i-1][j-1]+X[i-1]
    #カウンタが0になったときの値を初期化
    dp[i][0]=0
    for j in range(i):
        #前の状態で一番大きいものが初期化されたとする
        dp[i][0]=max(dp[i][0],dp[i-1][j])
print(max(dp[-1]))

    
    


