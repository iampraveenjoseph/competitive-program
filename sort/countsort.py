def count_sort(arr,place):
    n=len(arr)
    count=[0]*10
    output=[0]*n

    for i in range(0,n):
        index=arr[i]//place
        count[index%10]+=1
    for i in range(1,n):
        count[i]+=count[i-1] 

    i=n-1
    while i>=0:
        index=arr[i]//place 
        output[count[index]-1]=arr[i]
        count[index]-=1
        i-=1
    for i in range(0,n):
        arr[i]=output[i]
    return arr


arr=[0,2,1,3,2,1]
place=1
print(count_sort(arr,place))