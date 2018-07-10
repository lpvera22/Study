
import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap = 0
    ora = 0
    for i in apples:
        if (a + i) >= s and (a + i) <= t:
            ap += 1
    print(ap)
    for j in oranges:
        if (b + j) >= s and (b + j) <= t:
            ora += 1
    print(ora)


if __name__ == '__main__':


    s = 7

    t = 11



    a = 5

    b = 15



    m = 3

    n = 2

    apples = [-2, 2, 1]

    oranges = [5 ,-6]

    countApplesAndOranges(s, t, a, b, apples, oranges)
