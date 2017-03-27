#!/usr/bin/python
#
# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach

import sys
#import queue

# no queue lib in hackerrank!!??!?! make my own i guess...

class QNode:
	def __init__(self, data):
		self.data = data
		self.nxt = None
		self.pre = None

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def put(self, data):
		n = QNode(data)

		if self.head == None:
			self.head = n
			self.tail = n
		else:
			n.nxt = self.head
			self.head.pre = n

			self.head = n

	def pprint(self):
		n = self.head
		while n:
			has_nxt = n.nxt != None
			has_pre = n.pre != None
			print "%s (%s, %s)" % (n.data, has_pre, has_nxt)

			n = n.nxt

	def get(self):
		if not self.tail:
			raise Exception('empty queue')

		result = self.tail
		pre = self.tail.pre

		if pre == None:
			self.head = None
			self.tail = None
		else:
			pre.nxt = None
			self.tail = pre

		return result.data

	def empty(self):
		if self.head == None:
			return True

		return False

class Node:
	def __init__(self, num):
		self.num = num
		# for sparse trees this is better, for a fully connected
		# graph this is twice as bad as a n x n table
		self.neighbors = []

class Graph:
	def __init__(self, num_nodes):
		self.num_nodes = num_nodes
		self.nodes_list = [None] * num_nodes

	def connect(self, x, y):
		if self.nodes_list[x] == None:
			self.nodes_list[x] = Node(x)
		if self.nodes_list[y] == None:
			self.nodes_list[y] = Node(y)

		node_x = self.nodes_list[x]
		node_y = self.nodes_list[y]

		node_x.neighbors.append(node_y)
		node_y.neighbors.append(node_x)


	def find_all_distances(self, start):
		distances = [-1] * self.num_nodes
		start_node = self.nodes_list[start]

		#n_queue = queue.Queue()
		n_queue = Queue()
		n_queue.put((start_node, 0))

		# this is just a marker value
		distances[start] = -999

		while not n_queue.empty():
			node, dist = n_queue.get()
			new_dist = dist + 6

			if not node:
				continue

			for n in node.neighbors:
				if distances[n.num] == -1:
					distances[n.num] = new_dist
					n_queue.put((n, new_dist))

		for d in distances:
			if d != -999:
				sys.stdout.write("%s " % d)

		sys.stdout.write("\n")

t = input()
for i in range(t):
	n, m = [int(x) for x in raw_input().split()]
	graph = Graph(n)
	for i in xrange(m):
		x,y = [int(x) for x in raw_input().split()]
		graph.connect(x-1, y-1)

	s = input()
	graph.find_all_distances(s-1)

