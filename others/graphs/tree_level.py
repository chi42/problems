#!/usr/bin/python
#
# Given a binary tree, print the tree content, with
# one tree level per line
#
# i.e.
#       a
#    /     \
#   b       c
#   |       |
#   e       f
#
# print:
# a
# bc
# ef

import queue
import sys

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def print_tree(root):
	q = queue.Queue()
	q.put((root, 0))

	prev_level = 0
	while not q.empty():
		node, level = q.get()

		if level != prev_level:
			sys.stdout.write("\n")
			prev_level = level

		if node.left:
			q.put((node.left, level + 1))
		if node.right:
			q.put((node.right, level + 1))

		sys.stdout.write("%s " % node.data)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.left = n2
n1.right = n3

n2.left = n4
n4.left = n5

n3.left = n7
n3.right = n6

print_tree(n1)

