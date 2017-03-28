#!/usr/bin/python
#
# in order traversal of a tree:
# 1) recursion
# 2) stack with double pop
# 3) stack with single pop

import ex_trees

def inorder_rec(node):
	if node == None:
		return

	inorder_rec(node.left)
	print node.data
	inorder_rec(node.right)

def inorder_double(node):
	stack = [(node, False)]

	while len(stack) > 0:
		cur, do_print = stack.pop()

		if do_print == True:
			print cur.data
		else:
			if cur.right:
				stack.append((cur.right, False))

			stack.append((cur, True))

			if cur.left:
				stack.append((cur.left, False))

# do the left subtree, then print self, then do the right subtree
def inorder_single(node):

	cur = node
	stack = []

	while len(stack) > 0 or cur != None:
		if cur:
			stack.append(cur.left)
		else:
			cur = stack.pop()
			print cur.data

			cur = cur.right

inorder_rec(ex_trees.short_tree)
print 'next'
inorder_rec(ex_trees.short_sorted_tree)

print "---- double pop"
inorder_double(ex_trees.short_tree)
print 'next'
inorder_double(ex_trees.short_sorted_tree)

print "---- single pop"
inorder_double(ex_trees.short_tree)
print 'next'
inorder_double(ex_trees.short_sorted_tree)
