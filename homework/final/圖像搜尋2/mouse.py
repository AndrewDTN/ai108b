def printmap(m):
    for x in range(6):
        for y in range(8):
            if y == 7:
                print (m[x][y])
            else:
                print (m[x][y], end='')

def findpath(m,x,y):
    print ('----------------')
    print ("x=",x , "y=",y)
    printmap(m)
    if x>=6 or y>=8 :return False
    if m[x][y] == '*' :return False
    if m[x][y] == '+' :return False
    if m[x][y] == ' ' :m[x][y] = '.'
    if m[x][y] == '.' and x==5 or y==7 :return True

    if x<5 and m[x+1][y] == ' ':
        m[x][y] == '.'
        if findpath(m,x+1,y) :return True
    if y<7 and m[x][y+1] == ' ' :
        m[x][y] == '.'
        if findpath(m,x,y+1) :return True
    if y>0 and m[x][y-1] == ' ':
        m[x][y] == '.'
        if findpath(m,x,y-1) :return True
    if x>0 and m[x-1][y] == ' ':
        m[x][y] == '.'
        if findpath(m,x-1,y) :return True
    
    


map=([' ','*','*','*','*','*','*','*']
    ,[' ',' ',' ',' ','*',' ','*',' ']
    ,['*','*',' ',' ',' ',' ',' ',' ']
    ,[' ','*','*','*','*',' ',' ',' ']
    ,[' ',' ',' ',' ',' ',' ','*','*']
    ,['*','*','*','*','*',' ','*','*'])


findpath(map,0,0)
print ('----------------')
printmap(map)