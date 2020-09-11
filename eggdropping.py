import sys
INT_MAX=sys.maxsize
def eggdrop(egg,floor):
    
    eggFloor = [[0 for x in range(floor+ 1)] for x in range(egg + 1)]
    #print(eggFloor)

    for i in range(1,egg+1):
        eggFloor[i][0]=0
        eggFloor[i][1]=1
    #print(eggFloor)
    for j in range(1,floor+1):
        eggFloor[1][j]=j
    #print(eggFloor)
    for i in range(2,egg+1):
        for j in range(2,floor+1):
            eggFloor[i][j]=INT_MAX
            for x in range(1,j+1):
                result=1+max(eggFloor[i-1][x-1],eggFloor[i][j-x])
                if result<eggFloor[i][j]:
                    eggFloor[i][j]=result
    print(eggFloor[egg][floor])               
            
egg=int(input("Enter the Number of Eggs :"))
floor=int(input("Enter the Number of floor :"))        

eggdrop(egg,floor)