with open('input.txt') as f:
    input = f.read().splitlines()

wd = []  # working directory
ps = {}  # paths

for line in input:
    if line.startswith('$ cd'):
        _, _, d = line.split(' ')  # $ cd /
        if d == '/':
            wd = ['.']
        elif d == '..':
            wd.pop()
        else:
            wd.append(d)
        p = '/'.join(wd)
        if p not in ps:
            ps[p] = 0
    elif line[0].isdigit():
        s, _ = line.split(' ')  # 62158 sfwnts.hbj
        for i in range(len(wd)):
            p = '/'.join(wd[0:i + 1])
            ps[p] += int(s)

total = sum([s for _, s in ps.items() if s <= 100000])
print(total)

assert total == 2031851
