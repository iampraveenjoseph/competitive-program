
#Given an array of integers, print the array in such a way that the first
# element is first maximum and second element is first minimum and so on.
#Input : arr[] = {7, 1, 2, 3, 4, 5, 6}
#Output : 7 1 6 2 5 3 4
def alternativesort(arr,n):
    arr.sort()
    i=0
    j=n-1
    while(i<j):
        print(arr[j],end=' ')
        j-=1
        print(arr[i],end=" ")
        i+=1
    if n%2!=0:
        print(arr[i])

lis=[7,1,2,3,4,5,6]
alternativesort(lis,len(lis))
#[1,2,3,4,5,6,7]