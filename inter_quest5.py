# Sum list of dictionaries with the same key
x={'a':1,'b':2,'c':4}
y={'d':3,'b':9,'e':7}
a={}
for i in (x):
    if i in y:
        y[i]=x[i]+y[i]
x.update(y)
print(x)


