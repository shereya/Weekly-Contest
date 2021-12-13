n=int(input())
l=[]
L=[]
for i in range(0,n+1):
    x=int(input())
    l.append(x)
a=l.pop(-1)
for i in range(0,len(l)):
    for j in range (i+1,len(l)):
        for k in range(i+2,len(l)):
            if l[i]+l[j]+l[k]==a and l[i]!=l[j]!=l[k]:
                L.append(1)
if len(L)>0:
    print(True)
else:
    print(False)
