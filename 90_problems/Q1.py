import io
import sys
sys.setrecursionlimit(2000)

# _INPUT = """\
# 3 100
# 1
# 28 54 81

# """
# sys.stdin = io.StringIO(_INPUT)


N, L = map(int, input().split())
K = int(input())
As = [0]+list(map(int, input().split()))+[L]

# 2部探索をする
# 任意の値についてK+1個に分けたときに満たせるかを２部探索する


def check(m):
    l = 0
    cut = 0
    for i in range(N+1):
        gap = As[i+1]-As[i]
        l += gap
        if l >= m:
            cut += 1
            l = 0
    return cut >= K+1


def bind(l, r):
    while abs(r-l) > 1:
        m = (l+r)//2
        if check(m):
            l = m
        else:
            r = m
    return l


print(bind(-1, L))
