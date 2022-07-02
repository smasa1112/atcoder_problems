#一番クリアコストの引くところを繰り返す
import sys
sys.setrecursionlimit(10**9)

N,X=map(int,input().split())

AL = []
BL = []
 
for _ in range(N):
    a, b = map(int, input().split())
    AL.append(a)
    BL.append(b)
 
mae_total = 0
ato_total = 0
ans = float('inf')
 
for i in range(N):
    mae_total += AL[i]
    nokori = X - i
    if nokori < 0:
        break
    jikan = mae_total + ato_total + nokori * BL[i]
    
    ato_total += BL[i]
    
    if jikan  < ans:
        ans = jikan
 
print(ans)