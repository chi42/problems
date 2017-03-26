#!/usr/bin/python
#
# https://www.hackerrank.com/challenges/ctci-contacts

class Contacts:
	def __init__(self):
		self.prefix_tree = {'ren': 0}

	def add_contact(self, contact):
		cur = self.prefix_tree

		for letter in contact:
			if letter not in cur:
				cur[letter] = {'ren': 0}

			cur = cur[letter]
			cur['ren'] = cur['ren'] + 1

	def count_contacts(self, prefix):
		cur = self.prefix_tree

		for letter in prefix:
			if letter not in cur:
				return 0

			cur = cur[letter]

		return cur['ren']

	def do_op(self, op, contact):
		if op== 'add':
			self.add_contact(contact)

		if op == 'find':
			print self.count_contacts(contact)

conta = Contacts()
while True:
	op, contact = raw_input().strip().split(' ')
	conta.do_op(op, contact)
