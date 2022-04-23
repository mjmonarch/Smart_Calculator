names = input().split()

unique_names = sorted(set(names))
print(*unique_names, sep='\n')
