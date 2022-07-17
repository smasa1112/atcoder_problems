from collections import defaultdict
s=input()

ans_dic=defaultdict(int)
for char in s:
    ans_dic[char]+=1

for key,value in ans_dic.items():
    if value==1:
        print(key)
        exit()

print(-1)
    