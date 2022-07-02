N=int(input())

def warp(i,j):
    if i<0:
        i=N-1
    if j<0:
        j=N-1
    if i>=N:
        i=0
    if j>=N:
        j=0
    return (i,j)
               
                

A=[]
max_num=0
max_ind=[]
for i in range(N):
    array=list(map(int,list(input())))
    A.append(array)
    if max(array)>max_num:
        max_num=max(array)
        max_ind=[]
        for j,num in enumerate(array):
            if num==max_num:
                max_ind.append((i,j))   
    elif max(array)==max_num:
        for j,num in enumerate(array):
            if num==max_num:
                max_ind.append((i,j))
     
ans=int("1"*N)
for i,j in max_ind:
    for k in range(-1,2):
        for l in range(-1,2):
            #添字ミスらないようにしましょう
            if k!=0 or l!=0:
                i_tmp=i
                j_tmp=j
                tmp_ans=str(A[i][j])
                for _ in range(N-1):
                    i_tmp,j_tmp=warp(i_tmp+k,j_tmp+l)
                    tmp_ans+=str(A[i_tmp][j_tmp])
                tmp_ans=int(tmp_ans)
                ans=max(ans,tmp_ans)
                
print(ans)




    
       