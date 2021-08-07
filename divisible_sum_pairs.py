# Divisible Sum Pairs

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisibleSumPairs(n, k, ar):
    # Write your code here
    pairs = 0
    ar.sort()
    print("Array: ", ar)
    for index in range(0, len(ar)):
        print(f"Index: {index}")
        for nextIndex in range(index+1, len(ar)):
            print(f"\tnextIndex: {nextIndex}")
            print(f"\tFirst Condition: {ar[index] < ar[nextIndex]}")
            print(f"\tSecond Condition: {(ar[index]+ar[nextIndex]) % k == 0}")
            if((ar[index]+ar[nextIndex]) % k == 0):
                pairs += 1
    return pairs


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
