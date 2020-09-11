def insertion_sort(lis):
    length=range(1,len(lis)) # since first element is considered as sorted so negelect 0
    for i in length:
        while lis[i-1]>lis[i] and i>0:
            lis[i-1],lis[i]=lis[i],lis[i-1]
            i-=1
    return lis
lis=[12,3,2,123,77,9]
print(insertion_sort(lis))