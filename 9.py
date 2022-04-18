a=[1,2,3,4,5,6,7,8]
n=int(input("Enter the num:"))
i=0
c=0
b=[]
while i<len(a):
    c=n+a[i]
    if c==9:
        b.append(i)
    i+=1
print(b)