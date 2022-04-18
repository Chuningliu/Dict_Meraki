#  Get key with maximum value in dictionary?
a= {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
b=[]
max=0
for i in a:
    b.append(a[i])
    b.sort()
    c=b[:-2:-1]
print(c)
i=0
d=[]
while i<len(c):
    for j,k in a.items():
        if k==c[i]:
            d+=j
    i+=1
print(d)
    