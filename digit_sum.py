def digit_sum(n):
    numStr = str(n)
    numStr_length = len(numStr)
    total = 0

    for i in range(numStr_length):
        total += int(numStr[i])

    return total


print (digit_sum(1234))


def ranger(x):
    for i in range(x):
        print (i)


ranger(5)