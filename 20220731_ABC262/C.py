N=int(input())
A=list(map(int,input().split()))
# 面倒なので全部1引いてindexに直す
A=[a-1 for a in A]
# 愚直解
# N^2かかるので足りない
# cnt=0
# for i in range(N-1):
#     ai=A[i]
#     for j in range(i+1,N):
#         aj=A[j]
#         if min(ai,aj)==i+1 and max(ai,aj)==j+1:
#             cnt+=1            
# print(cnt)

cnt=0
is_same_cnt=0
for i in range(N):
    #相方がいる場合
    #indexとvalueが同じやつがある場合はnC2でできる
    if i==A[i]:
        is_same_cnt+=1
    else:
        # 互い違いになっているやつ
        if A[A[i]]==i and A[i]<A[A[i]]:
            # 片方だけでいいから大小関係の比較でOK
            cnt+=1
            
        
if is_same_cnt<=1:        
    print(cnt)
else:
    print(cnt+(is_same_cnt*(is_same_cnt-1)//2))