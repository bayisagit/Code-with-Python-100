import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

def dec2bin(n):
    bin = ''
    while True:
        if n == 0:
            bin += '0'
            set(bin)
            bin = bin[::-1]
            return bin
            break
        elif n == 1:
            bin += '1'
            set(bin)
            bin = bin[::-1]
            return bin
            break
        else:
            if n % 2 == 1:
                bin += '1'
                n = int(n/2)
            else:
                bin += '0'
                n = int(n/2)

a = list(dec2bin(n))

current_count = 0
max_count = 0

for num in a:
    if num == '1':
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0
print(max_count)