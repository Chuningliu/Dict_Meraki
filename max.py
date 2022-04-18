# SORT WITHOUT METHOD

def nummbers(num):
    b=len(num)
    for i in range(b):
        for j in range(i+1,b):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
    print(num)
nummbers([3,5,7,34,2,2,5])
            
        
        