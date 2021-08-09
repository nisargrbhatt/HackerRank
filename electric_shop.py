# Electronics Shop

import os
import sys

#
# Complete the getMoneySpent function below.
#


def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    result = -1
    possibleSets = []
    for keyboard in keyboards:
        for drive in drives:
            if((keyboard+drive) <= b):
                possibleSets.append((keyboard+drive))

    if(len(possibleSets) > 0):
        possibleSets.sort(reverse=True)
        result = possibleSets[0]

    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)

    # fptr.write(str(moneySpent) + '\n')

    # fptr.close()
