N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
X = int(input())
ng_stair = [0] * (X+1)
dp = [0]*(X+1)
dp[0]=1
is_climb = True
for b in B:
    ng_stair[b] = 1
# print(ng_stair)  
for i in range(X):
    for a in A:
        if i+a > X:
            continue
        if dp[i] == 1 and ng_stair[i+a] == 0:
            dp[i+a]=1
#dpはX<=10^5のためできない
#登れる段数などで判定する方がよさそう。

if dp[-1]==1:
    print("Yes")
else:
    print("No")