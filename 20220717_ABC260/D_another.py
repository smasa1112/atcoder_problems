import bisect
from collections import defaultdict

N,K=map(int,input().split())
P=list(map(int,input().split()))

#1~Nまでの消失ターンデフォルトは-1
turns=[-1 for _ in range(N)]


#とりあえずdictで作ってみる
ans_dic=defaultdict(list)

keys=[]
for turn,num in enumerate(P,start=1):
    #ここの処理がsortが重いからしないようにしたい
    #keys.sort()
    if K==1:
        turns[num-1]=turn
    else:
        #検索を2部探索で省略
        i=bisect.bisect(keys,num)
        if i!=len(keys):
            ans_dic[num]=ans_dic[keys[i]]
            ans_dic[num].append(num)
            del ans_dic[keys[i]]
            #ここをappend,removeにすると大小関係が崩れるのでNG
            #処理的には自動的に後ろに行くほど大きくなるように要素が追加されるため
            keys[i]=num
            if len(ans_dic[num])==K:
                for ind in ans_dic[num]:
                    turns[ind-1]=turn
                keys.remove(num)
                del ans_dic[num]
        else:
            ans_dic[num].append(num)
            keys.append(num)

print(*turns,sep="\n")