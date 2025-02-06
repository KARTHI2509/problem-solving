d={}
n=int(input("enter a number:"))
for i in range(1,n+1):
    key=i
    value=i*i
    d.update({key:value})
print(d)
    
