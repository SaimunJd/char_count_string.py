s=input("word=")
p=input("char=")
k=0
for i in range(len(s)):
	if(s[i]==p):
		k+=1
print(k)
