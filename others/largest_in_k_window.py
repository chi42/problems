#!/usr/bin/python
#
#
# Given a window k, find the largest integer for every window in the array

from collections import deque

def find_largest_in_k(ar, k):

	# this is wrong. think about it

	for i in range(len(ar)):
		while True:
			value, index = dq[0]
			if index <= i - k:
				dq.popleft()
			else:
				break

		while not dq.empty():
			value, index = dq[-1]
			if value > ar[i]:
				# pop from right
				dq.pop()
			else:
				break

		# append to the right
		dq.append()

