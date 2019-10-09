def factorial (num):
    if num is 1:
        return 1
    else:
        return num * factorial(num -1 )

# print factorial(3)

def rgb(r,g,b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int) :
            print "#%x%x%x" % (r,g,b)
        else:
            print "r,g,b has to be integer"
rgb(100,10.5,300)