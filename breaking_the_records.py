# Breaking the Records

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here
    maxBreaks = -math.inf
    minBreaks = math.inf
    maxCounts = -1
    minCounts = -1

    for score in scores:
        if(score > maxBreaks):
            maxBreaks = score
            maxCounts += 1
        if(score < minBreaks):
            minBreaks = score
            minCounts += 1

    return [maxCounts, minCounts]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
