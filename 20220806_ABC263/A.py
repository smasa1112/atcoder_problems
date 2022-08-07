from collections import defaultdict

ans_dic=defaultdict(int)

A=list(map(int,input().split()))

for num in A:
    ans_dic[num]+=1
    
values = list(ans_dic.values())

if 3 in values and 2 in values:
    print("Yes")
else:
    print("No")