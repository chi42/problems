#!/usr/bin/python

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

###############################3
#       1 
#    2     3
#  4     7   6
# 5     

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

short_tree = n1

###############################3
#           4
#       2       6
#    1    3   5    7
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n4.left= n2
n4.right = n6

n2.left = n1
n2.right = n3

n6.left = n5
n6.right = n7

short_sorted_tree = n4

