def searchFormat(problems):

	if len(problems) > 5:
		return 'Error: Too many problems.'

	operations = [problem.split(' ') for problem in problems]
	for operation in operations:
		if '+' in operation or '-' in operation:
			for content in operation:
				if content.isdigit():
					if len(content) > 4:
						return 'Error: Numbers cannot be more than four digits.'
				elif content == '+' or content == '-':
					continue
				else:
					return 'Error: Numbers must only contain digits.'
		else:
			return "Error: Operator must be '+' or '-'."
	else:
		return operations


def break_down_contents(operations):

	firstNums = [x[0] for x in operations]
	secondNums = [x[2] for x in operations]
	operators = [x[1] for x in operations]

	tops = [];	bottoms = [];	dashes = [];	solutions = []

	for first, second, op in zip(firstNums, secondNums, operators):
		length = max(len(first), len(second)) + 2
		tops.append(first.rjust(length));	bottoms.append(op + second.rjust(length-1))
		dashes.append("-" * length)
		if op == '+':
			solutions.append(f'{int(first) + int(second)}'.rjust(length))
		elif op == '-':
			solutions.append(f'{int(first) - int(second)}'.rjust(length))

	return tops, bottoms, dashes, solutions


def arithmetic_arranger(problems, solve=False):

	arranged_problems = ''
	operations = searchFormat(problems)

	if 'Error' in operations:
		return operations

	tops, bottoms, dashes, solutions = break_down_contents(operations)

	n = 1
	for top in tops:
		if n != 1:
			arranged_problems += '    '
		n += 1
		arranged_problems += top
	else:
		n = 1
		arranged_problems += '\n'

	for bottom in bottoms:
		if n != 1:
			arranged_problems += '    '
		n += 1
		arranged_problems += bottom
	else:
		n = 1
		arranged_problems += '\n'

	for dash in dashes:
		if n != 1:
			arranged_problems += '    '
		n += 1
		arranged_problems += dash
	else:
		n = 1

	if solve:
		arranged_problems += '\n'
		for solution in solutions:
			if n != 1:
				arranged_problems += '    '
			n += 1
			arranged_problems += solution

	return arranged_problems