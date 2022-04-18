# Store the unique letters and their frequency of the letters 
# from the word "MISSISSIPPI" to a dictionary, were the letters 
# are the keys and their frequencies are the values.
# Output :-
# {'M':1,'I':4,'S':4,'P':2}

 
count = {"M":0,"I":0,"S":0,"P":0}
a= "MISSISSIPPI"
for i in a:
	if i=="M":
		count['M']=count['M']+1
	elif i=="I":
		count['I']=count['I']+1
	elif i == "S":
		count['S']=count['S']+1
	elif i == "P":
		count['P']=count['P']+1
print (count)