n,x=map(int,input().split())
array=[]
for i in range(26):
    array+=[chr(ord("A")+i) for _ in range(n)]
print(array[x-1])