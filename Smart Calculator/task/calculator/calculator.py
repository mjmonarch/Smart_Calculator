# -------------------------------------- STAGE 1 --------------------------------------
# args = [int(x) for x in input().split()]
# print(sum(args))

# -------------------------------------- STAGE 2 --------------------------------------
inp = input()
while inp != '/exit':
	if inp:
		args = [int(x) for x in inp.split()]
		print(sum(args))
	inp = input()
print("Bye!")