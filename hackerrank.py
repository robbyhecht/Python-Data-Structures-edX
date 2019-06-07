# CHECK IF A NUMBER IS IN A GIVEN ARRAY

def findNumber(arr, k):
    if k in arr:
        print("YES")
    else: print("NO")


arr = [1, 2, 3, 4, 8, 6]
findNumber(arr, -1)

# FIND ODD NUMBERS IN A GIVEN RANGE

def rangefunc(l,r):
    x = range(l, r+1)
    odds = list()
    for num in x:
        if num % 2 is not 0:
            odds.append(num)
    print(odds)

rangefunc(3, 13)