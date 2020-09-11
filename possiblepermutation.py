result=[]
def permutation(data,i,length):
    if i==length:
        result.append(''.join(data))
    else:
        for j in range(i,length):
            data[i],data[j]=data[j],data[i]
            permutation(data,i+1,length)
            data[i],data[j]=data[j],data[i]
data=str(input("Enter the string :"))
permutation(list(data),0,len(data))
for word in result:
    print(word)
