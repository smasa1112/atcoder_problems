from functools import partial


from collections import deque

N, K = map(int, input().split())
S = input()

# # Kを満たすまで辞書順最小を順番に入れていく
# ans = []
# start = -1
# for i in range(K, 0, -1):
#     partial_S = S[start+1:-i+1]
#     if i == 1:
#         partial_S = S[start+1:]
#     ch = min(partial_S)
#     ans.append(ch)
#     start = S.index(ch)
# print("".join(ans))

ans = ''
que = deque()

# queで文字を管理
for i, c in enumerate(S):
    # queに文字があって残っている文字が今入れた文字より後ろだと文字削除
    while que and que[-1] > c:
        que.pop()
    que.append(c)
    # 文字のindexがKを超えたら一文字ずつ取り出す
    if N - K <= i:
        ans += que.popleft()
print(ans)
