import math

# u = ['robby', 'sam', 1, 'robby', 'beth', 'robby']

# def usernamesSystem(u):
#     '''adds names to new list if they are strings. using count method works to add trailing numbers except trying to figure out how to find original name inside of a name with trailing number'''
#     nameList = list()
#     for name in u:
#         if type(name) is str:
#             if name not in nameList:
#                 nameList.append(name)
#             elif name in nameList:
#                 nameList.append(name + str(nameList.count(name)))
#     return(nameList)

# print(usernamesSystem(u))


nums = [7, 12, 35, 16] 7 9 8 12

def minSum(num, k):
    while k > 0:
        biggest = max(num)
        newNum = math.ceil(biggest / 2)
        for i in range(len(num)):
            if num[i] == biggest:
                num[i] = newNum
        k -= 1
    return sum(num)


# -make empty list
# use k as a counter
# don't forget to find sum instead of list
    # ---round up non-integers
    # ---start with biggest number
    # ---use max to find biggest number
    # 
    

print(minSum(nums, 3))
