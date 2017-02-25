n=int(input())
boys_s=[]
girls_s=[]
for i in range(0,n):
    boys_s.append(int(input()))
for i in range(0,n):
    girls_s.append(int(input()))  
m=int(input())
rep=0
k=len(boys_s)
for i in range(0,k):
    rep=rep+(boys_s[i]*girls_s[i])
print rep
prod=[]
for i in range(0,k):
    prod.append((boys_s[i]*girls_s[i]))
mx=max(prod)

def duplicates(prod, item):
    
    return [i for i, x in enumerate(prod) if x == item] 
q= duplicates(prod, mx)
diff=[]
for i in q:
    diff.append(boys_s[i]-girls_s[i])
mx1=max(diff)
i1=diff.index(mx1)


x=q[i1]
x=prod.index(mx)

if(boys_s[x]<0 and girls_s[x]<0):
    
    m1=(boys_s[x]-n)*girls_s[x]
    m2=boys_s[x]*(girls_s[x]-n)
    print(m1,m2,x)
    if(m1>m2):
        boys_s[x]=(boys_s[x]-n)
        
    print boys_s[x]
    print boys_s

    if(m2>m1):
        girls_s[x]=(girls_s[x]-n)
    print girls_s[x]



else:
    
    m1=(boys_s[x]+n)*girls_s[x]
    m2=boys_s[x]*(girls_s[x]+n)
    print(m1,m2,x)
    if(m1>m2):
        boys_s[x]=(boys_s[x]+n)
        
    print boys_s[x]
    print boys_s

    if(m2>m1):
        girls_s[x]=(girls_s[x]+n)
    print girls_s[x]
rep=0   
for i in range(0,k):
    rep=rep+(boys_s[i]*girls_s[i])
print rep




    
    
    
