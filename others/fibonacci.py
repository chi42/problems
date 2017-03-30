#!/usr/bin/pytho
#
#

def fibonacci(num):
	if num <= 0:
		return 0

	if num == 1:
		return 1

	return fibonacci(num - 1) + fibonacci(num - 2)

def fib_quick(num):
	if num <= 0:
		return 0

	if num == 1:
		return 1

	fib_p1 = 1
	fib_p2 = 0
	fib_n = 0

	for i in xrange(2, num + 1):
		fib_n = fib_p1 + fib_p2

		fib_p2 = fib_p1
		fib_p1 = fib_n

	return fib_n


print fib_quick(1)
print fib_quick(2)
print fib_quick(3)
print fib_quick(4)
print fib_quick(5)
print fib_quick(6)

