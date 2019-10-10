# implement a function that returns true if the number is prime (false otherwise). Test from 1 to 100.
# def prime(num):
#     prime = [2,3,5,7]
#     if num in prime:
#         return True
#     for primeNum in prime:
#         if num % primeNum ==0:
#             return False
#     return True

# primelist = [2,3,5,7,11,13,17,19,23,
# 29,31,37,41,43,47,53,59,61,67,
# 71,73,79,83,89,97]
# count = 0;
# for x in range(2, 100):
#     if prime(x) == True:
#         count+=1
#         if x in primelist:
#             print "check"
#         else:
#             print x

# Implement a function that takes a list of lists of any length and returns a list of one dimension.
# def lists(li):
#     oneList = []
#     for lis in li:
#         if type(lis) is int:
#             oneList.append(lis)
#         elif len(lis) >= 1:
#             for anotherL in lis:
#                 oneList.append(anotherL)
#         else:
#             oneList.append(lis)
#     return oneList

# list = [123,[1,2],[55,4],1,4,5]
# print lists(list)

# Write a function that: Gets a phrase as a parameter. Returns a new sentence with each word with the letters reversed.

# def reversedPhrase(string):
#     space = string.split()
#     reversedWord = ""

#     for i in space:
#         reversedWord = reversedWord  + i[::-1] + ' '
#     return reversedWord

# string = "hello world from a kc!"
# print reversedPhrase(string)


