#桁の情報をpythonならまとめて持てるので公式解説よりも計算量がすくなくて済む

N,x=map(int,input().split())
m=(2**30)-1
b1=m
b0=0

for _ in range(N):
    t,a=map(int,input().split())
    if t==1:
        b1&=a
        b0&=a
    elif t==2:
        b1|=a
        b0|=a
    elif t==3:
        b1^=a
        b0^=a
    # (x&b1) => xとm(全部１が変化した部分)の共通点→ がどう変化したか
    # (x^m) => 0の部分だけが1として抽出
    # (x^m)&b0 => (x^m)とb0の共通部分最初0の部分がどう変化したか
    x= (x&b1)| (x^m)&b0 
    print(x)