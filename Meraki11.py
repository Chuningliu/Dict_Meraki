# Write a program to print the top 3 highest values of a given dictionary.
# Output :-
# [58,56,100]

a= {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}

    
n=[]
for i in a:
    if a[i]>50:
        b=a[i]
        n.append(b) 
print(n)














# for value in a:
#     b=a.values()
#     c=sorted(b,reverse=True)[:3]
# print(c)
