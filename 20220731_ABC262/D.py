N=int(input())
A=list(map(int,input().split()))

#平均値は整数
#和が平均値で割り切れる
#bitで状態を管理する?=>状態が2^100-1を超えてしまう？
#計算量がオーバーする
#sortしてうまいことやれるかためす？

'''
解法

> あまりを持ってDPして余りによって遷移を変える
なぜか
2^N-1だと計算量のオーバーが見込まれる
N**4だとMAXでも10^8程度なので2sには間に合わないが2.5sには間に合わせることができる
現在の余りの値と個数を持ってdp[j][k][l]にする
dp[j][k][l]= 先頭インデックスj項までからk個の和をiで割った時の余りlの個数をMODで割ったもの
これをi=0からNまで足し合わせる
'''


MOD=998244353
cnt=0
for i in range(1,N+1):
    dp=[[[0]* i for _ in range(i+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for j in range(N):
        for k in range(i+1):
            for l in range(i):
                dp[j+1][k][l] += dp[j][k][l]
                if k!=i:
                    dp[j+1][k+1][(l+A[j])%i] += dp[j][k][l]
    cnt+=dp[-1][i][0]
print(cnt%MOD)