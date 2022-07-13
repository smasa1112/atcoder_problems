N,M,X,T,D=map(int,input().split())

first_height=T-D*X

if M<X:
    print(first_height+D*M)
else:
    print(T)