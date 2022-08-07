#すごろくなら確率遷移でいけるので解けそう！
#期待値は各位置に行く平均回数に
import sys
import numpy as np
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

 

def main(X):
    N = len(X)
    dp = np.zeros(N)
    dp[0] = 1.0
 
    E = 0.0
 
    for n in range(N - 1):
        if X[n] == -1:
            continue
        if X[n] > 0:
            to = min(N - 1, n + X[n])
            dp[to] += dp[n]
            continue
        E += dp[n]
        for d in range(1, 7):
            to = min(N - 1, n + d)
            dp[to] += dp[n] / 6
    return E / dp[-1]
  
if __name__=="__main__":
    N = int(readline())
    A= list(map(int.input().split()))
        
    X = np.array(readline().split(), np.int64)
    print(main(X))