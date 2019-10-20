m1 = [[0,12,1] ]
m2 = [[1,2,3]]

# must have the right rows and columns
def add(m1,m2):
    transposed = []
    for x in range(len(m1)):
        col = []
        for y in range(len(m1[0])):
            col.append(m1[x][y] + m2[x][y])
        transposed.append(col)
    return transposed


def getIndex (m1):
    rows = 0
    cols = 0

    for x in m1:
        cols = cols + 1
    for y in m1[0]:
        rows+=1

    index = (rows,cols)
    return index


m3 = [[1,2,3]]
m4 = [[2],[2]]
def multiply (m1,m2):
    transposed = []
    m1index = getIndex(m1)
    m2index = getIndex(m2)
    if m1index[1] == m2index[0]:
        index = (m1index[0], m2index[1])
    else:
        index = (0,0)

    for x in m1:
        col = []
        for y in x:
            for x1 in m4:
                for y1 in x1:
                    col.append(y*y1)
        print col
        transposed.append(col)

    return transposed


multiply(m3,m4)