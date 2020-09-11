def merge_sort(lis):
    if len(lis)<=1:
        return lis
    
    middle=len(lis)//2
    left=merge_sort(lis[:middle])
    #print(left)
    right=merge_sort(lis[middle:])
    #print(right)
    print(left)
    return merge(left,right)

    
def merge(left,right):
    i,j=0,0,
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            #print(result)
            i+=1
        else:
            result.append(right[j])
            j+=1
        
    #print(left[i:])
    result.extend(left[i:])
    
    result.extend(right[j:])
    #return list(set(lis))
    return result

lis=[11, 8, 7, 0, 6, 2, 5]
print(merge_sort(lis))




