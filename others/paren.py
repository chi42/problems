#!/usr/bin/python

def balance_parens(l):
	# start from the back
	close_count = 0
	for i in xrange(len(l) - 1, -1, -1):
		if l[i] == ')':
			close_count += 1

		elif l[i] == '(':
			if close_count == 0:
				# mark unmatched open paren for deletion
				l[i] = None
			else:
				close_count -= 1

	copy_idx = 0
	open_count = 0
	for i in xrange(len(l)):
		if l[i] == '(':
			open_count +=1

		elif l[i] == ')':
			if open_count == 0:
				# mark close paren for deletion
				l[i] = None
			else:
				open_count -= 1

		if l[i] != None:
			# backfill the holes left by deleted parens
			if copy_idx != i:
				l[copy_idx] = l[i]

			copy_idx += 1

	if open_count != 0:
		raise Exception("i've done something wrong: %s" % open_count)

	return copy_idx

def test(s):
	l = list(s)
	length = balance_parens(l)

	res_str = ''.join(l[:length])
	print "input: '%s' output: '%s'" % (s, res_str)

test(")(")
test(")()()(")
test("(((")
test(")))")
test(")))")
test("()(()()")
test("()(()))()")

