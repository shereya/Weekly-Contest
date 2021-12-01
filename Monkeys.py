#Monkeys REC Weekly Coding Question
n=int(input())
L=[]
for i in range(n):
    l1=[]
    s=str(input())
    for j in s.split():
        l1.append(int(j))
    L.append(l1)
for i in L:
    t=()
    c=0
    l2=[]
    l3=[]
    for j in i:
        t=t+(j,)
    for j in t:
        l2.append(j)
    l3.append(l2)
    f=True
    while f==True:
        c=c+1
        l4=[]
        for j in range(len(i)):
            l4.append(0)
        for j in range(len(i)):
            l4.pop(i[j]-1)
            l4.insert(i[j]-1,l3[-1][j])
        if l4==i:
            f=False
        else:
            l3.append(l4)
    print(c)
    
        
        
        

        
    
        
    
