h1,h2,h3,w1,w2,w3=map(int,input().split())

#プログラムによって総和を求める            
cnt=0

def get_3_num(num):
    data=[]
    for i in range(1,num-1):
        for j in range(1,num-i):
            data.append([i,j,num-i-j])
    return data

def get_3_num_fix(s_num,f_num):
    target=s_num-f_num
    data=[]
    for i in range(1,target):
        data.append([f_num,i,target-i])
    return data

h1_nums=get_3_num(h1)
for h1_num in h1_nums:
    w1_nums=get_3_num_fix(w1,h1_num[0])
    for w1_num in w1_nums:
        h2_nums=get_3_num_fix(h2,w1_num[1])
        for h2_num in h2_nums:
            a=[h1_num,h2_num,[w1_num[2],0,0]]
            a[2][1]=w2-a[1][1]-a[0][1]
            a[2][2]=w3-a[1][2]-a[0][2]
            if sum(a[2])==h3 and min(a[2])>=1:
                cnt+=1
print(cnt)
    
            
                

    
