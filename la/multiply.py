m1 = [[0,12,1],[0,1,2] ]
m2 = [[1,2,3],[1,3,4]]

def add(m1,m2):
    transposed = []
    for x in range(len(m1)):
        col = []
        for y in range(len(m1[0])):
            col.append(m1[x][y] + m2[x][y])
        transposed.append(col)
    return transposed

def checkIndex(m1):
    s = []
    width = len(m1)
    for x in range(width):
        s.append( len(m1[x]) )
    print (s)


checkIndex(m1)
