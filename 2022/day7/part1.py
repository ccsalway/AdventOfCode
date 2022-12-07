with open('input.txt') as f:
    input = f.read().splitlines()

cwd = []
ds = {}

for line in input:
    if line.startswith('$ cd'):
        _, _, d = line.split(' ')
        if d == '/':
            cwd = ['.']
        elif d == '..':
            cwd.pop()
        else:
            cwd.append(d)
        path = '/'.join(cwd)
        if path not in ds:
            ds[path] = 0
    elif line[0].isdigit():
        s, _ = line.split(' ')
        for i in range(len(cwd)):
            path = '/'.join(cwd[0:i + 1])
            ds[path] += int(s)

total = sum([s for d,s in ds.items() if s <= 100000])
assert total == 2031851
print(total)
