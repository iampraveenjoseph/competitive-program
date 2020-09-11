
final=[]
def reverse(string,mid):
    word=''
    for i in range(len(string)-mid-1,-1,-1):
        word+=string[i]
    #print(word)
    result=string[mid:]+word
    return(result)

    

string="Fruit like mango and apple are common but Grapes are rare"
num="39"
t=string.split(' ')
index1, index2=int(num[0])-1,int(num[1])-1
word1,word2=t[index1],t[index2]
#daoT
mid1=len(word1)//2
mid2=len(word2)//2
res1=reverse(word1,mid1)
res2=reverse(word2,mid2)
final.append(res1)
final.append(res2)
#print(final)
print(' '.join(final))
#ngonam pesarG