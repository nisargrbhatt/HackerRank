# Sales by Match

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # Write your code here
    sock_pair_map = []
    pairs_found = 0
    for sock in ar:
        if(sock in sock_pair_map):
            continue
        sock_pair_map.append(sock)
        sock_count = ar.count(sock)
        if(sock_count > 1):
            pairs = math.floor(sock_count/2)
            pairs_found += pairs
    return pairs_found


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
