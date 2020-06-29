#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    q="abcdefghijklmnopqrstuvwxyz"
    w = q.upper()
    t = ""
    for i in s:
        if i not in q and i not in w:
            t=t+i
        else:
            if i not in q:
                ind = (w.index(i)+k)%len(q)
                t=t+w[ind]
            else:
                ind = (q.index(i)+k)%len(q)
                t=t+q[ind]
    return t



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
