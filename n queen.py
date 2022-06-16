def check(place,row,col,size):
    for i in range(col):
        if place[row][i]==1:
            return False
    while row>=0 and col>=0:
        if place[row][col] ==1:
            return False
        row-=1 
        col-=1 
    while row<size and col>=0:
        if place[row][col] == 1:
            return False
        row+=1
        col-=1 
    return True
    
def placing(place,col,size):
    if col>=size:
        return True
    for i in range(size):
        if check(place,i,col,size):
            place[i][col] = 1 
            if placing(place,col+1,size):
                return True
            place[i][col]=0
    return False
size=int(input())
place=[[0 for j in range(size)] for i in range(size)]
if placing(place, 0,size) == True:
    for i in range(size):
        for j in range(size):
            print(place[i][j],end= " ")
        print()
else:
    print("no ans")