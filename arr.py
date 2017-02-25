n=input("enter the number of element in array:")
arr=[]
for i in range(1,n+1):
    element=input("element:")
    arr.append(element)
    
def cost(n):
    print arr
    diff=len(arr)
    print diff
    arr2=sorted(arr)
    print arr2
    fiarr=[]
    for i in range(0,diff-1):
        j=abs(arr2[i]-arr2[i+1])
        fiarr.append(j)
    print fiarr
    print min(fiarr)
cost()    
