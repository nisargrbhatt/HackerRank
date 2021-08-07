# Drawing Book

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    # Write your code here
    if(n == p):
        return 0

    if(p <= (n/2)):
        return int(p/2)
    else:
        distance = n-p
        if(n % 2 == 0):
            return math.ceil(distance/2)
        else:
            return int(distance/2)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
