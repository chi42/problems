#!/usr/bin/python
#
# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree?h_r=next-challenge&h_v=zen

class node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def is_valid(data, max_data, min_data):
	if max_data and data >= max_data:
		return False

	if min_data and data <= min_data:
		return False

	return True

def check_binary_search_tree_(root):
	stack = [(root, None, None)]

	while len(stack) > 0:
		cur, max_data, min_data = stack.pop()

		if not is_valid(cur.data, max_data, min_data):
			return False

		if cur.left:
			stack.append((cur.left, cur.data, min_data))

		if cur.right:
			stack.append((cur.right, max_data, cur.data))

	return True


# if you traverse a tree inorder and the tree is sorted, you print
# the sorted elements
def check_binary_search_tree_2(root):
	is_first = True
	prev_value = None

	stack = []
	cur = root

	while len(stack) > 0 or cur:
		if cur:
			stack.append(cur)
			cur = cur.left
		else:
			cur = stack.pop()
			if not is_first:
				if cur.data <= prev_value:
					return False
			else:
				is_first = False

			prev_value = cur.data
			cur = cur.right

	return True
