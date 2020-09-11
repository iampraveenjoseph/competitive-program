
#elementlist=[]
#for i in range(len(input1)):
    #element=str(input1[i])
    #elementlist.append(element)
def anagram(input1):
    elementlist=[]
    for i in range(len(input1)):
        element=str(input1[i])
        elementlist.append(element)
    dic={}
    for ele in elementlist:
        key=''.join(sorted(ele))
        
        if key in dic.keys():
            dic[key].append(ele)
        else:
            dic[key]=[]
            dic[key].append(ele)

    resultlist=[]
    #print(len(dic))
    #print(dic[key])
    
    for key,value in dic.items():
        if len(value)>1:
            for i in range(len(dic[key])):
                e=int(dic[key][i])
                resultlist.append(e)
            #print(resultlist)
            return(max(resultlist)-min(resultlist))
            
            
        

        #print(max(resultlist))
        #print(min(resultlist))
            
       
        

input1=[89017,12321,56780]

if anagram(input1):
    print(anagram(input1))
else:
    print(-1)   