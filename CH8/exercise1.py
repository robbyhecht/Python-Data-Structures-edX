# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

thisList = [1, 3, "s", 7, True]
def chop(newList):
    newList = newList[1:-1]
    return None

def middle(newList):
    newList = newList[1:-1]
    return newList

a = [1,2,3]
def same():
    b = a
    b[0] = 17
    return a

t1 = [1,2]
def ts(t1):
    t2 = t1.append(3)
    print(t1)[1,2,3]
    # print(t2)

result = chop(thisList)
otherResult = middle(thisList)
same = same()
print(result)
print(otherResult)
print(same)

t = [1, 2, 3, 4, 7]
x = 6
t = t + [x]
t.append(x)
print(t)
orig = t[:]
t.sort()
print(t)
print(orig)