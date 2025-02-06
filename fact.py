n=int(input("enter number:"))
f=1
if(n==0):
    print("1")
else:
    for i in range(1,n+1):
        f=f*i
        print(f,',',end="")
        
