# Cats and a Mouse

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.


def catAndMouse(x, y, z):
    diffByX = abs(x-z)
    diffByY = abs(y-z)
    if(diffByX == diffByY):
        return 'Mouse C'
    elif(diffByX > diffByY):
        return 'Cat B'
    elif(diffByY > diffByX):
        return 'Cat A'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
