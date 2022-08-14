#行列が短縮できる<=>Bの数字が同じ行に存在　かつ　Bの列が同じ行に存在

H1,W1 = map(int,input().split())
A= [list(map(int,input().split())) for _ in range(H1)]

H2,W2 = map(int,input().split())
B= [list(map(int,input().split())) for _ in range(H2)]

#Bの要素がAのどこにあったかを格納する変数
indexes = [list([] for _ in range(W2))  for _ in range(H2)]


flag=False
B_row=0
for i in range(H1):
    #要素がある場合のみindexを追加できるか探索
    if B[B_row][0] in A[i]:
        B_col=0
        for j in range(W1):
            if A[i][j] == B[B_row][B_col]:
                indexes[B_row][B_col]=[i,j]
                B_col+=1
            if B_col==W2:
                B_row+=1
                break
    if B_row==H2:
        break

if B_row == H2:
    #各行は一致しているので各列のindexが一致しているか確認
    for col in range(W2):
        cols=[indexes[i][col][1] for i in range(H2)]
        if len(set(cols))==1:
            flag=True
        else:
            flag=False

if flag:
    print("Yes")
else:
    print("No")
             
