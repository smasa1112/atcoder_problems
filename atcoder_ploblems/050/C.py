from collections import defaultdict
N=int(input())
A=list(map(int,input().split()))
ans_dic=defaultdict(int)
mod=10**9+7
#数を格納       
for num in A:
     ans_dic[num]+=1

keys=list(ans_dic.keys())
keys.sort()
flag=True
if N%2==0:
    i=1
    for key in keys:
        if key!=i or ans_dic[key]!=2:
            flag=False
            break
        else:
            i+=2
       
else:
    i=0
    for key in keys:
        if i==0:
            if key!=0 or ans_dic[key]!=1:
                flag=False
                break
            i+=2
        else:
            if key!=i or ans_dic[key]!=2:
                flag=False
                break
            i+=2
if flag:
    ans=2**(N//2)
    ans%=mod
    print(ans)
else:
    print(0)
       
       
       		
       	