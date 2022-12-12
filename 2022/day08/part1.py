with open('input.txt') as f:
    input = f.read().splitlines()

gh = [[int(x) for x in list(line)] for line in input]
gv = list(zip(*gh))
gx, gy = len(gh[0]), len(gh)
v = 0

for row in range(gy):
    for col in range(gx):
        t = gh[row][col]  # tree
        r = gh[row][col + 1:]  # right
        d = gv[col][row + 1:]  # down
        f = gh[row][:col][::-1]  # left
        u = gv[col][:row][::-1]  # up
        for n in [r, d, f, u]:
            # visible from at least one side
            if not n or max(n) < t:
                v += 1
                break

print(v)

assert v == 1827
