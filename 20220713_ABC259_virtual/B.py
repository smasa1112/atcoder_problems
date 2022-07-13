import numpy as np

a,b,d=map(int,input().split())

def rotation_o(u, t, deg=False):

    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)

    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])

    return  np.dot(R, u)

# 単位ベクトル
rotate=rotation_o((a,b),d,True)

print(*rotate)
