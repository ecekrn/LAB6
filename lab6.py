mlist = []

sumup = lambda n: (n-3)/n**2
x = int(input("please enter a number: "))
while (x != 0):
    mlist.append(sumup(int(x)))
    x = int(x-1)

sumOfList = sum(mlist)
print(sumOfList)


print("2ND QUESTION")


def multiplier (n):
    """ this funtion multiplies some stuff"""
    if (n == 0):

        return 1

    else:
        global y
        y = ((n) / (n + 2)) - 10

        return  y * multiplier(n-1)

r=multiplier(2)
print(multiplier.__doc__, r )