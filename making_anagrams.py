#!/usr/bin/python
#
# https://www.hackerrank.com/challenges/ctci-making-anagrams
#
#

from string import ascii_lowercase

def number_needed(a, b):
	deletions = 0
	a_dict = {}

	for letter in ascii_lowercase:
		a_dict[letter] = 0

	for letter in a:
		a_dict[letter] = a_dict[letter] + 1

	for letter in b:
		if a_dict[letter] > 0:
			a_dict[letter] = a_dict[letter] - 1

		else:
			deletions += 1

	for letter, count in a_dict.iteritems():
		deletions += count

	return deletions

print number_needed("cde", "abc")
print number_needed("cdeeeeee", "abc")

