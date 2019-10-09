import timeit

start = timeit.default_timer()

# Sum 0 to 10000000 to use for loop
s = 0
x = 10000
for x in range(1, x):
    s = s + x
print s

s = 0
a = 0
#while loop
while a < x + 1:
    s = s + a
    a = a + 1
print s

#Faster way
total = (x*(x+1)/2)
print total
stop = timeit.default_timer()
print('Time: ', stop - start)