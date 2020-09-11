def quick_sort(lis):
    n=len(lis)
    if n<=1:
        return lis
    else:
        pivot=lis.pop()
    lower=[]
    higher=[]
    for element in lis:
        if element>pivot:
            higher.append(element)
        else:
            lower.append(element)
    return quick_sort(lower)+[pivot]+quick_sort(higher)
lis=[12,3,2,123,77,9]
print(quick_sort(lis))