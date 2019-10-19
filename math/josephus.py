def josephus(numPeople):
    list = range(1,numPeople+1)
    index = []
    count = 2;
    while len(list) != 1:
        for x in list:
            print x
            if list.index(x) == len(list) -1:
                print list.pop(0)
                print list
            else:
                print list.pop(list.index(x+1))
                print list
    print list
josephus(7)