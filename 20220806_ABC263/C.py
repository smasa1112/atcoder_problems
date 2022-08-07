import itertools


N,M=map(int, input().split())

# Nのほうが大きい時は絶対みたさない

#for文を回していく感じで組み合わせを出す
for v in itertools.combinations(range(1,M+1),N):
    print(*list(v))