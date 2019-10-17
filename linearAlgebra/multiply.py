m1 = [[0,12,1],[0,1,2] ]
m2 = [[1,2,3],[1,3,4],[1,1,1],[1]]

def add(m1,m2):
    transposed = []
    for x in range(len(m1)):
        col = []
        for y in range(len(m1[0])):
            col.append(m1[x][y] + m2[x][y])
        transposed.append(col)
    return transposed

def checkIndex(m1,m2):
    s = []
    a = []
    width1 = len(m1)
    width2 = len(m2)
    lens = len(m1)
    for x in range(width1):
        s.append( len(m1[x]) )

    for x in range(width2):
        a.append( len(m2[x]) )

    if s[width1 -1] is a[0]:
        print s[width1 -1], a[0]
    else:
        print "cannot multiply"

checkIndex(m1,m2)
