def bubble_sort(lis):
    sort=False
    while not sort:
        sort=True
        for i in range(0,len(lis)-1):
            if lis[i]>lis[i+1]:
                sort=False
                lis[i],lis[i+1]=lis[i+1],lis[i]
    return(lis)
lis=[12]
print(bubble_sort(lis))           
