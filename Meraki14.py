# Write a program to sort a dictionary in ascending or descending 
# according to its values .



f={"bijendar":45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for key,value in (sorted(f.items())):
#     print(f)

a=[]
d={}
for value in f.values():
    a.append(value)
    a.sort()
print(a)
i=0
while i<len(a):
    for key,value in f.items():
        if value==a[i]:
            d.update({key:value})
    i+=1
print("Ascending",d)
e={}
i=-1
while i>=-len(a):
    for key,value in f.items():
        if value==a[i]:
            e.update({key:value})
    i-=1
print("Descending",e)
    
