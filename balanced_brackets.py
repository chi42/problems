#!/usr/bin/python

def is_matched(expression):
	stack = []
	for l in expression:
		if l in ['{', '(', '[']:
			stack.append(l)

		else:
			if len(stack) <= 0:
				return False

			matching = stack.pop()
			if l == '}' and matching != '{':
				return False
			if l == ']' and matching != '[':
				return False
			if l == ')' and matching != '(':
				return False

	if len(stack) != 0:
		return False
	else:
		return True

inputs = [
	"}][}}(}][))]",
	"[](){()}",
	"()",
	"({}([][]))[]()",
	"{)[](}]}]}))}(())(",
]

for i in inputs:
	print is_matched(i)
