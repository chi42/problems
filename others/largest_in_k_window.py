#!/usr/bin/python
#
#
# Given a window k, find the largest integer for every window in the array
#
# this runs in o(n) with o(k) space

from collections import deque

def find_largest_in_k(ar, k):
	dq = deque()
	# the newest item is on the right.
	# the bigest items are on the left
	# when you get a new element:
	#   remove the expired item off the left
	#   if the new value is bigger then a value on the right, remove the
	#	   value on the right. Continue until empty or right is bigger then
	#	   the current. What this means, is the list is always sorted

	for i in range(len(ar)):
		if len(dq) > 0:
			value, index = dq[0]
			if index <= i - k:
				dq.popleft()

		while len(dq) > 0:
			value, index = dq[-1]
			if ar[i] >= value:
				# pop from right
				dq.pop()
			else:
				break

		# append to the right
		dq.append((ar[i], i))

		value, index = dq[0]
		print value

array = [1,2,3,4,5,6]
find_largest_in_k(array, 3)

print '----'
array = [6,5,4,3,2,1]
find_largest_in_k(array, 3)


print '----'
array = [6,5,4,3,2,1]
find_largest_in_k(array, 4)

print '----'
array = [6,8,4,7,2,9]
find_largest_in_k(array, 4)

print '----'
array = [6,8,4,7,2,9]
find_largest_in_k(array, 2)

print '----'
array = [1,9,5,4,12,9, 2, 3, 2, 10, 11]
find_largest_in_k(array, 3)
