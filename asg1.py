# assignment 1 
# count how many elements in array(a) are bigger than an integer(n)

import random

def CountNums(a, n):
    count = 0
    for r in a:
        count += 1 if r > n else 0
    return count

if __name__ == '__main__':
    a = [random.randint(10, 100) for i in range(10)]
    n = random.randint(10, 100)
    c = CountNums(a, n)
    print('array a: {}'.format(a))
    print('integer n: {}'.format(n))
    print('count: {}'.format(c))