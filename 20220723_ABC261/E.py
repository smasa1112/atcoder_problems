N,C=map(int,input().split())
commands=[list(map(int,input().split())) for _ in range(N)]
#いちいち比較するのが面倒
#or と xor と andは可換
#なのでとりあえず各項目の処理をまとめてどんどん掛け合わせていく配列を作成する
#and or xorで縮減配列を作成してまとめてどんどんやっていくのがよさそう？
#各桁でやりましょう

ans=[0]*N
for i in range(30):
    #bitシフトと1との論理積でi桁目(2)が0,1か判断
    each_keta=(C>>i) & 1
    #最初0,1だったらどっちになっているか保存するやつ
    f=[0,1]
    for j in range(N):
        command=commands[j]
        ope_keta= (command[1] >> i) & 1
        if command[0]==1:
            each_ope=[0&ope_keta,1&ope_keta]
        elif command[0]==2:
            each_ope=[0|ope_keta,1|ope_keta]            
        elif command[0]==3:
            each_ope=[0^ope_keta,1^ope_keta]
        #今の状態からどんどん更新していく
        f=[each_ope[f[0]],each_ope[f[1]]]
        #はじめ0,1の最終段階がfに保存されているので桁から探せる
        ans_keta=f[each_keta]
        #bitの桁をついあkするイメージ
        ans[j] = ans[j]|(ans_keta<<i)
        
for i in range(N):
    print(ans[i])
#上手くいかない

