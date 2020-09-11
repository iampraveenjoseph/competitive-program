def heapify(lis,n,i):
    large=i
    l=2 * i + 1 
    r=2 * i + 2 
    
    if l < n and lis[l] > lis[i]:
        #print(lis[l])
        large = l
   
    if r < n and lis[r] > lis[large]:
        large = r
    if large != i:
        lis[i],lis[large] = lis[large],lis[i]
        heapify(lis,n,large)

def build_heap(lis):
    n=len(lis)
    for i in range(n//2-1,-1,-1):
       #print(lis)
        #print(i)
        heapify(lis,n,i)
    print(lis)
    for i in range(n-1,0,-1):
        lis[i],lis[0]=lis[0],lis[i]
        #print(lis)
        heapify(lis,i,0)
    
    



lis= [11,6,5,0,8,2,7]
build_heap(lis)
print(lis)
