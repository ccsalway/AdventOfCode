with open('input.txt') as f:
    input = f.read().splitlines()

gh = [[int(x) for x in list(line)] for line in input]
gv = list(zip(*gh))
gx, gy = len(gh[0]), len(gh)
vs = []

for row in range(gy):
    for col in range(gx):
        t = gh[row][col]  # tree
        r = gh[row][col + 1:]  # right
        d = gv[col][row + 1:]  # down
        f = gh[row][:col][::-1]  # left
        u = gv[col][:row][::-1]  # up
        ts = 1
        for n in [r, d, f, u]:
            # visual space
            s = 0
            for x in n:
                s += 1
                if x >= t:
                    break
            ts *= s
        vs.append(ts)

result = max(vs)
print(result)

assert result == 335580
