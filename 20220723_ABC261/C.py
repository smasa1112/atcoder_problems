from collections import defaultdict

N=int(input())

ans_dic=defaultdict(int)
for _ in range(N):
    S=input()
    if S in ans_dic:
        print(f"{S}({ans_dic[S]})")
        ans_dic[S]+=1
    else:
        print(S)
        ans_dic[S]+=1