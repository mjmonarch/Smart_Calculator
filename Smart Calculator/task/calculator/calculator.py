# -------------------------------------- STAGE 1 --------------------------------------
# args = [int(x) for x in input().split()]
# print(sum(args))

# -------------------------------------- STAGE 2 --------------------------------------
# inp = input()
# while inp != '/exit':
# 	if inp:
# 		args = [int(x) for x in inp.split()]
# 		print(sum(args))
# 	inp = input()
# print("Bye!")

# -------------------------------------- STAGE 3 --------------------------------------
# inp = input()
# while inp != '/exit':
# 	if inp:
# 		if inp == '/help':
# 			print("The program calculates the sum of numbers")
# 		else:
# 			args = [int(x) for x in inp.split()]
# 			print(sum(args))
# 	inp = input()
# print("Bye!")

# -------------------------------------- STAGE 4 --------------------------------------
# def get_func(sequence):
# 	func = sequence[0]
# 	if len(sequence) > 1:
# 		for elem in sequence[1:]:
# 			if elem == '-':
# 				if func == '-':
# 					func = '+'
# 				else:
# 					func = '-'
# 	if func == '-':
# 		return lambda a, b: a - b
# 	elif func == '+':
# 		return lambda a, b: a + b
#
#
# def do_action(num1, num2, func):
# 	return func(num1, num2)
#
#
# inp = input()
# while inp != '/exit':
# 	if inp:
# 		if inp == '/help':
# 			print("The program calculates the result of basic addict///subtract operation on numbers. -- means +")
# 		else:
# 			elements = inp.split()
# 			result = int(elements[0])
# 			for i, elem in enumerate(elements[1:], 1):
# 				if i % 2 == 1:
# 					func = get_func(elem)
# 				else:
# 					result = do_action(result, int(elem), func)
# 			print(result)
# 	inp = input()
# print("Bye!")

# -------------------------------------- STAGE 5 --------------------------------------
# import re
#
#
# def get_func(sequence):
# 	func = sequence[0]
# 	if len(sequence) > 1:
# 		for elem in sequence[1:]:
# 			if elem == '-':
# 				if func == '-':
# 					func = '+'
# 				else:
# 					func = '-'
# 	if func == '-':
# 		return lambda a, b: a - b
# 	elif func == '+':
# 		return lambda a, b: a + b
#
#
# def do_action(num1, num2, func):
# 	return func(num1, num2)
#
#
# inp = input()
# while inp != '/exit':
# 	if inp:
# 		if not re.match(r'/', inp):
# 			if re.match(r'[+-]?\d+(\s+[-+]+\s+[+-]?\d+)*$', inp):
# 				if inp == '/help':
# 					print("The program calculates the result of basic addict///subtract operation on numbers. -- means +")
# 				else:
# 					elements = inp.split()
# 					result = int(elements[0])
# 					for i, elem in enumerate(elements[1:], 1):
# 						if i % 2 == 1:
# 							func = get_func(elem)
# 						else:
# 							result = do_action(result, int(elem), func)
# 					print(result)
# 			else:
# 				print("Invalid expression")
# 		elif inp == '/help':
# 			print("The program calculates the result of basic addict/subtract operation on numbers. -- means +")
# 		else:
# 			print("Unknown command")
# 	inp = input()
# print("Bye!")

# -------------------------------------- STAGE 6 --------------------------------------
import re


def get_func(sequence):
	func = sequence[0]
	if len(sequence) > 1:
		for elem in sequence[1:]:
			if elem == '-':
				if func == '-':
					func = '+'
				else:
					func = '-'
	if func == '-':
		return lambda a, b: a - b
	elif func == '+':
		return lambda a, b: a + b


def do_action(num1, num2, func):
	return func(num1, num2)


inp = input().strip()
memory = {}
while inp != '/exit':
	if inp:
		if not re.match(r'/', inp):
			if not re.search(r'=', inp):
				if re.match(r'[+-]?(\d+|[a-zA-Z]+)(\s+[-+]+\s+[+-]?(\d+|[a-zA-Z]+))*$', inp):
					elements = inp.split()
					error = False
					try:
						result = int(elements[0])
					except ValueError:
						if elements[0] in memory.keys():
							result = memory[elements[0]]
						else:
							print("Unknown variable")
							error = True
					if not error:
						for i, elem in enumerate(elements[1:], 1):
							if i % 2 == 1:
								func = get_func(elem)
							else:
								try:
									result = do_action(result, int(elem), func)
								except ValueError:
									if elem in memory.keys():
										result = do_action(result, memory[elem], func)
									else:
										print("Unknown variable")
										error = True
										break
						if not error:
							print(result)
				else:
					print("Invalid expression")
			else:
				seq = re.match(r'([a-zA-Z]+)\s*=\s*(\d+|[a-zA-Z]+)$', inp)
				if seq:
					var_1 = seq.group(1)
					var_2 = seq.group(2)
					try:
						memory[var_1] = int(var_2)
					except ValueError:
						if var_2 not in memory.keys():
							print("Unknown variable")
						else:
							memory[var_1] = memory[var_2]
				else:
					print("Invalid identifier")
		elif inp == '/help':
			print("The program calculates the result of basic addict/subtract operation on numbers. -- means +")
		else:
			print("Unknown command")
	inp = input().strip()
print("Bye!")