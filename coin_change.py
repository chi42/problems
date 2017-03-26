#!/usr/bin/python
#
# https://www.hackerrank.com/challenges/ctci-coin-change

import sys

def make_change(coins, n):
	mem = [0] * (n + 1)

	# start marker
	mem[0] = 1

	for coin in coins:
		for i in xrange(coin, n + 1):
			mem[i] = mem[i - coin] + mem[i]

		#print "======coin %s" % coin
		#print mem

	return mem[n]

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)
