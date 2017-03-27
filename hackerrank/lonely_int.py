#!/bin/python

def lonely_integer(a):
	s = 0
	for num in a:
		s = s ^ num

	return s

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)

