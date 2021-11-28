#prime counter - REC Weekly Contest - Non- CSE/IT
s=str(input())
L=[]
for i in range(int(s)):
    s1=str(input())
    l=[]
    for j in s1.split():
        l.append(int(j))
    L.append(l)
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return 'prime'
    else:
        return 'composite'
L3=[]
for i in L:
    a=i[0]
    b=i[1]
    L1=[]
    L2=[]
    for j in range(a,b+1):
        L1.append(j)
    for j in L1:
        c=0
        for k in range(1,j+1):
            ans=prime(k)
            if ans=='prime':
                c=c+1
        L2.append(c)
    L3.append(L2)
for i in L3:
    C=0
    for j in i:
        if prime(j)=='prime':
            C=C+1
    print(C)












