input1=["A","B","C"]
input2=["B","C","O"]
#result=set(input1)-set(input2)
#result1=set(input2)-set(input1)
#result=result.union(result1)
res_list = [] 
for i in input1: 
    if i not in input2: 
        res_list.append(i) 
for i in input2: 
    if i not in input1: 
        res_list.append(i) 
print(res_list)

#print(result)
count=[]
s,res=0,0
for ele in res_list:
    co=ord(ele)
    count.append(co)
#print(count)
for num in count:
    s+=num
#print(s)
#print(len(str(s)))
if len(str(s))>1:
    while s>0:
        n=s%10
        res+=n
        s=s//10
    print(res)
#print(list(result))
