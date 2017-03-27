#!/usr/bin/python
#
# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid?h_r=next-challenge&h_v=zen

def count_ones(grid, start_point, ones_dict):
	stack = [start_point]
	counter = 1

	row_count = len(grid)
	col_count = len(grid[0])

	while len(stack) > 0:
		r, c = stack.pop()

		neighbors = [
			(r, c+1),
			(r, c-1),
			(r+1, c),
			(r+1, c+1),
			(r+1, c-1),
			(r-1, c),
			(r-1, c+1),
			(r-1, c-1)
		]

		for point in neighbors:
			if point in ones_dict:
				stack.append(point)
				del ones_dict[point]
				counter += 1

	return counter

def get_biggest_region(grid):
	ones_dict = {}
	max_region = 0

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				ones_dict[(i, j)] = True

	while len(ones_dict) > 0:
		start_point, dont_care = ones_dict.popitem()
		val = count_ones(grid, start_point, ones_dict)

		if val > max_region:
			max_region = val

	return max_region

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)

