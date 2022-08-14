R,C= map(int,input().split())
R=R-8
C=C-8
if R==0 and C==0:
    flag=False
else:
    R=abs(R)
    C=abs(C)
    
    if R%2==1 and C==0:
        flag=True
    elif C%2==1 and R==0:
        flag=True
    elif C%2==0 and R%2==0 and C==R:
        flag=False
    elif C%2==1 and C%2==1 and C==R:
        flag=True
    else:
        # 大小関係で入れ替え
        if R>C:
            # Rの方が必ず大きい　→　対称性を用いる
            X,Y=C,R
        else:
            X,Y=R,C
        
        if Y%2==0:
            flag=False
        else:
            flag=True
            
            


if flag:
    print("black")
else:
    print("white")    
