#!/usr/bin/python
#
#
# a ring buffer, or circular queue

class Buffer:
	def __init__(self, size):
		# you can use another variable to hold size, to know when the
		# array is empty, or you can burn an array entry
		self.ring_size = size + 1
		self.ring = [0] * (self.ring_size)

		# for the sake of this example, push at head, pop at tail
		self.head = 0
		self.tail = 0

	def push(self, value):
		new_head = (self.head + 1) % self.ring_size
		if new_head == self.tail:
			return False

		self.ring[self.head] = value
		self.head = new_head

		return True

	def pop(self):
		if self.head == self.tail:
			raise Exception("empty queue")

		val = self.ring[self.tail]
		self.tail = (self.tail + 1) % self.ring_size

		return val

	def empty(self):
		return self.tail == self.head

	def __len__(self):
		head_offset = self.head
		if self.head < self.tail:
			head_offset += self.ring_size

		return head_offset - self.tail

b = Buffer(10)
print b.empty()
print len(b)

for i in range(7):
	print "\npush %s, status: %s, empty: %s, len: %s" % (i, b.push(i), b.empty(), len(b))
	print "head: %s, tail: %s" % (b.head, b.tail)


for i in range(4):
	print "\npop %s, empty: %s, len: %s" % (b.pop(), b.empty(), len(b))
	print "head: %s, tail: %s" % (b.head, b.tail)

for i in range(7):
	print "\npush %s, status: %s, empty: %s, len: %s" % (i, b.push(i), b.empty(), len(b))
	print "head: %s, tail: %s" % (b.head, b.tail)

for i in range(10):
	print "\npop %s, empty: %s, len: %s" % (b.pop(), b.empty(), len(b))
	print "head: %s, tail: %s" % (b.head, b.tail)
