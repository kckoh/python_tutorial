# -*- coding: utf-8 -*-

#basic types
# print "int 3.14 = ", int(3.14)
# print "5.0/ 2 + 3 = " , 5.0/ 2 +3

#String
# s = "Camel"
# print "Size of %s => %d", (s,len(s))
# theWord = "阿麗思道"
# s = '가'
# print theWord, s

#list
# list = ["Yes","Genesis", "Pink Floyd", "ELP"]
# for lists in list:
#     print lists

# abc = ["A","B", "C"]
# while abc:
#     print "Left", abc.pop(0), "remain", len(abc) #pop(index)


dim = 7, 7
mat = {}

# Tuples are immutable
# Each tuple represents
# a position in the matrix
mat[3, 7] = 3
mat[4, 6] = 5
mat[6, 3] = 7
mat[5, 4] = 6
mat[2, 9] = 4
mat[1, 0] = 9

for lin in range(dim[0]):
    for col in range(dim[1]):
        # Method get(key, value)
        # returns the key value
        # in dictionary or
        # if the key doesn't exists
        # returns the second argument
        print mat.get((lin, col), 0),
    print

