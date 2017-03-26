#!/usr/bin/python
#
# https://www.hackerrank.com/challenges/ctci-array-left-rotation
#
# A left rotation operation on an array of size n shifts each of the array's
# elements 1 unit to the left. For example, if left rotations are performed on
# array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].
#
# Given an array of n integers and a number, d, perform left rotations on the
# array. Then print the updated array as a single line of space-separated
# integers.

#
# [0,1,2,3,4]
# [1,2,3,4,0]
# [2,3,4,0,1]

def array_left_rotation(a, n, k):
    """
    Copy out the front k digits.
    Move the last k-n digits to the front
    Write the old front k digits to the bacfk
    O(N) time, O(N) space
    space is linear because we have to copy at most n-1 digit references
    """
    k_mod = k % n
    if k_mod == 0:
        return a

    front_slice = a[:k_mod]

    for i in range(n - k_mod):
        a[i] = a[i + k_mod]

    for val in front_slice:
        i += 1
        a[i] = val

    return a

def array_left_rotation2(a, n, k):
    """
    [0,1,2,3,4,5] rotate 2
    [2,3,4,5,0,1]

    0 -> 4  i + (n - k)
    1 -> 5  i + (n - k)
    2 -> 0  (i + (n - k)) % 6
    3 -> 1  (i + (n - k)) % 6
    4 -> 2  (i + (n - k)) % 6
    5 -> 3

    O(N) time and space. does less copies though. everything copied once
    """

    k_mod = k % n
    if k_mod == 0:
        return a

    new_a = [0] * n

    for i in range(n):
        new_a[(i + (n - k_mod)) % n] = a[i]

    return new_a

def array_left_rotation3(a, n, k):
    # this doesn't work
    k_mod = k % n
    if k_mod == 0:
        return a

    i = 0
    prev_val = a[0]
    for dont_care in range(n):
        next_i = (i + (n - k_mod)) % n
        print "%s -> %s" % (i, next_i)

        temp = a[next_i]
        a[next_i] = prev_val

        prev_val = temp
        i = next_i

    return a


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k)
print ' '.join(map(str, answer))


print array_left_rotation([0,1,2,3,4,5], 6, 2)
print array_left_rotation2([0,1,2,3,4,5], 6, 2)
#print array_left_rotation3([0,1,2,3,4,5], 6, 2)
