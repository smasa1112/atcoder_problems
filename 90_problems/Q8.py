N=int(input())
S=input()
dp=[[0]*8 for _ in range(N)]
ans_s="atcoder"
dp[0][0]=1

for ind,ch in enumerate(S):
    if ind!=0:
        dp[ind][0]+=dp[ind-1][0]
    for target_ind,target_ch in enumerate(ans_s):
        if ind!=0:
            dp[ind][target_ind+1]+=dp[ind-1][target_ind+1]

        if ch==target_ch:
            dp[ind][target_ind+1]+=dp[ind][target_ind]

print(dp[-1][-1]%(10**9+7))

