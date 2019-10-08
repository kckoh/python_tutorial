def factorial (num):
    if num is 1:
        return 1
    else:
        return num * factorial(num -1 )

print factorial(3)