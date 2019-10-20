# josephus problem
# kills the person next to you
# returns the last survival
def josephusBrute(numPeople):
    list = range(1,numPeople+1)
    y = 1;
    while len(list) != 1:
        for x in list:
            if list.index(x) == len(list) -1:
                list.pop(0)
                break
            list.pop(list.index(x)+1)
            y += 1
    return list
# for x in range(1,100):
#     print "position {} and survival:{}".format(x,josephus(x))

