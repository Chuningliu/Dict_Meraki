# Take a list having dictionary elements as shown below (Sample Data) 
# and then store all the unique values into a list and print.

a=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"six":"9"},{"seven":"7"}]
b=[]
i=0
while i<len(a):
    for j in a[i]:
        if a[i][j] not in b:
            b.append(a[i][j])                                                   
    i+=1
print(b)
    
        