#!/usr/bin/python
#
# https://www.hackerrank.com/challenges/ctci-recursive-staircase

def stair_climb(num_stairs):
	stairs = [0] * (num_stairs + 1)

	# marker
	stairs[0] = 1

	for stair in xrange(1, num_stairs + 1):
		count = 0
		for step_size in (1, 2, 3):
			if stair - step_size >= 0:
				count += stairs[stair - step_size]

		stairs[stair] = count

	return stairs[num_stairs]

s = int(raw_input().strip())
for a0 in xrange(s):
	n = int(raw_input().strip())
	print stair_climb(n)

