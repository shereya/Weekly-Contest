t=int(input())
L=[]
for j in range(t):
    s=str(input())
    l1=[]
    l2=[]
    L1=[]
    L2=[]
    c1=0
    c2=0
    for i in s:
        l1.append(i)
        l2.append(i)
    for i in range(0,len(l1)):
         c1=c1+1
         a=l1.pop(0)
         l1.append(a)
         if l1==l1[::-1]:
             L1.append(l1)
             break
         else:
             continue
    for i in range(0,len(l2)):
        c2=c2+1
        a=l2.pop()
        l2=[a]+l2
        if l2==l2[::-1]:
            L2.append(l2)
            break
        else:
            continue
    if L1==[] and L2==[]:
       L.append(-1)
    else:
        if c1<c2:
            L.append(c1)
        if c2<c1:
            L.append(c2)
        if c1==c2:
            L.append(c1)
for i in L:
    print(i)
