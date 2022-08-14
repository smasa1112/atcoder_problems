S=input()

cnt=0

ans_dic={"a":1,"t":2,"c":3,"o":4,"d":5,"e":6, "r":7}

numbered_S=[0]*7
for i in range(7):
    numbered_S[i]=ans_dic[S[i]]

# 反転数を求める

for i in range(7):
    for j in range(i,7):
        if numbered_S[i] > numbered_S[j]:
            cnt+=1
            
print(cnt)