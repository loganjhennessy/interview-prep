#The program calclulates the possible solution to a certain diagonal problem, parameter n refers to the number of rows and columns, l refers to the number of diagonal lines.

#The numbers inside the result list refer to three states:
# 0: no line
# 1: diagonal line from up-left corner to lower-right corner
# 2: diagonal line from up-right corver to lower-left corner

def legal_extension(result,n): #check if the extension is legal
    i=len(result)
    if i>n**2:                 #check if the length of list exceeds
        return False
    if (i-1)%n>0:                      #case 1 and case 2 cannot be
        if result[i-1]+result[i-2]==3: #adjacent to each other
            return False
    if (i-1)//n>0:
        if result[i-1]+result[i-n-1]==3:
            return False
        if (i-1)%n>0:      #the upper-left box of case 1 cannot be
            if result[i-1]==1 and result[i-n-2]==1:   #case 1
                return False
        if i%n<n:          #the upper-right box of case 2 cannot be
            if result[i-1]==2 and result[i-n]==2:     #case 2
                return False
    return True

def extend(result, n, l):
    lines_n=0
    for item in result:
        if item!=0:
            lines_n=lines_n+1
    if len(result)==n**2 and lines_n==l:
        for i in range(1,n+1):
            print(result[n*(i-1):n*i])
        exit()
    for k in [0,1,2]:
        result.append(k)
        if legal_extension(result,n):
            extend(result,n,l)
        result.pop()

n=5
result=[]
extend(result,n,l=16)
