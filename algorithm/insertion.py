def insertion (list, num) :
    li = list
    index = len(list) - 1
    length = len(list)
    if length == 0:
        li.append(num)
        return li
    elif length == 1:
        if num >= li[0]:
            li.append(num)
        else:
            li.insert(0,num)
    else:
        while True:
            if num >= li[index]:
                li.insert(index +1, num)
                print index
                break
            else:
                index -= 1
    return li


def insertionSort (list):
    li = list
    if len(list) == 1:
        return list
    current = 0
    for x in range(1,len(list)):
        print "this is x: {}".format(x)
        y = x
        while y != -1:
            print "this is x inside: {}".format(y)
            if li[y] < li[y-1]:
                swap(li,y,y-1)
                y -= 1
            else:
                break
    return li








def swap(list,indexa,indexb):
    copya = list[indexa]
    list[indexa] = list[indexb]
    list[indexb] = copya

print insertionSort([3,4,1])