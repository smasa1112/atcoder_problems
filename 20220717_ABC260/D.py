from collections import defaultdict
from heapq import heapify

N,K=map(int,input().split())
P=list(map(int,input().split()))

#1~Nまでの消失ターンデフォルトは0
turns=[-1 for _ in range(N)]


#とりあえずdictで作ってみる
ans_dic=defaultdict(list)
for turn,num in enumerate(P,start=1):
    keys=list(ans_dic.keys())
    keys.sort()
    flag=False
    if K==1:
        turns[num-1]=turn
    for i in range(len(keys)):
        if keys[i]>num:
            flag=True
            ans_dic[num]=ans_dic.pop(keys[i])
            ans_dic[num].append(num)
            if len(ans_dic[num])==K:
                indexes=ans_dic.pop(num)
                for ind in indexes:
                    turns[ind-1]=turn
            break
    if not flag:
        ans_dic[num].append(num)
            
print(*turns,sep="\n")