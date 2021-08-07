# Counting Valleys

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here
    currentLevel = 0
    count = 0
    levels = path.strip()

    for index in range(steps):
        if(levels[index] == 'U'):
            currentLevel += 1
        elif levels[index] == 'D':
            currentLevel -= 1
            if(currentLevel == -1):
                count += 1

    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
